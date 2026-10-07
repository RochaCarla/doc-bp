#!/usr/bin/env python3
"""Gera a aba "Estatísticas" da documentação a partir do repositório decidim-govbr.

Fontes:
  - histórico git (clone bare em .cache/estatisticas/), branches main e develop;
  - API pública do GitLab (merge requests, issues, pipelines, tags);
  - rubygems.org e endoflife.date (versões de Decidim, Ruby e Rails).

Uso:
  python3 scripts/estatisticas.py            # coleta e gera docs/estatisticas/
  GITLAB_TOKEN=... python3 scripts/estatisticas.py   # opcional, aumenta o limite da API

Só usa a biblioteca padrão do Python (3.9+).
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import subprocess
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROJECT_PATH = "lappis-unb/decidimbr/decidim-govbr"
REPO_URL = f"https://gitlab.com/{PROJECT_PATH}.git"
API = "https://gitlab.com/api/v4"
BRANCHES = ["main", "develop"]
ECOSYSTEM = [
    ("decidim-homes", "lappis-unb/decidimbr/components-brasil-participativo/decidim-module-homes"),
    ("decidim-enhanced_process_groups_and_scopes",
     "lappis-unb/decidimbr/components-brasil-participativo/decidim-module-enhanced_process_groups_and_scopes"),
    ("decidim-ej", "lappis-unb/decidimbr/components-brasil-participativo/decidim-ej"),
    ("decidim-extra_user_fields", "lappis-unb/decidimbr/decidim-extra_user_fields"),
    ("decidim-mobile", "lappis-unb/decidimbr/bp-mobile/decidim-module-mobile"),
]
MONTHS_PT = ["jan", "fev", "mar", "abr", "mai", "jun", "jul", "ago", "set", "out", "nov", "dez"]
CC_RE = re.compile(r"^(?P<type>[A-Za-z]+)(\([^)]*\))?!?:\s*\S")
TYPE_ALIASES = {"tests": "test", "refact": "refactor", "feature": "feat", "fixes": "fix", "docs": "docs"}
PLACEHOLDER_EMAIL = re.compile(r"(@(exemplo|example)\.(com|org)$)|(\.local(domain)?$)|(^root@)")
STABLE_TAG = re.compile(r"^v?\d+\.\d+\.\d+$")


# --------------------------------------------------------------------------- utilitários

def parse_dt(value: str | None) -> datetime | None:
    if not value:
        return None
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def month_key(dt: datetime) -> str:
    return f"{dt.year}-{dt.month:02d}"


def month_label(key: str) -> str:
    year, month = key.split("-")
    return f"{MONTHS_PT[int(month) - 1]}/{year[2:]}"


def last_months(now: datetime, count: int) -> list[str]:
    keys = []
    year, month = now.year, now.month
    for _ in range(count):
        keys.append(f"{year}-{month:02d}")
        month -= 1
        if month == 0:
            year, month = year - 1, 12
    return list(reversed(keys))


def percentile(values: list[float], pct: float) -> float | None:
    if not values:
        return None
    ordered = sorted(values)
    k = (len(ordered) - 1) * pct
    lower, upper = math.floor(k), math.ceil(k)
    if lower == upper:
        return ordered[int(k)]
    return ordered[lower] + (ordered[upper] - ordered[lower]) * (k - lower)


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def pct(part: float, total: float) -> float | None:
    return (100.0 * part / total) if total else None


def fmt_int(value) -> str:
    return "—" if value is None else f"{int(value):,}".replace(",", ".")


def fmt_pct(value) -> str:
    return "—" if value is None else f"{value:.0f}%"


def fmt_days(value) -> str:
    if value is None:
        return "—"
    if value < 1:
        return f"{value * 24:.0f} h"
    return f"{value:.1f} dias".replace(".", ",")


def fmt_date(dt: datetime | None) -> str:
    return "—" if dt is None else dt.strftime("%d/%m/%Y")


def norm_name(name: str) -> str:
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode().lower()
    tokens = re.findall(r"[a-z0-9]+", ascii_name)
    return "".join(sorted(tokens))


# --------------------------------------------------------------------------- HTTP

class Http:
    def __init__(self, token: str | None):
        self.token = token

    def get(self, url: str, params: dict | None = None):
        if params:
            url = f"{url}?{urllib.parse.urlencode(params)}"
        headers = {"User-Agent": "doc-bp-estatisticas"}
        if self.token and url.startswith(API):
            headers["PRIVATE-TOKEN"] = self.token
        for attempt in range(5):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=60) as resp:
                    return json.loads(resp.read().decode()), resp.headers
            except urllib.error.HTTPError as err:
                if err.code in (429, 500, 502, 503, 504) and attempt < 4:
                    time.sleep(2 ** attempt * 2)
                    continue
                raise
            except urllib.error.URLError:
                if attempt < 4:
                    time.sleep(2 ** attempt * 2)
                    continue
                raise
        raise RuntimeError(url)

    def paginate(self, path: str, params: dict) -> list:
        items, page = [], 1
        while page:
            data, headers = self.get(f"{API}{path}", {**params, "per_page": 100, "page": page})
            items.extend(data)
            nxt = headers.get("X-Next-Page")
            page = int(nxt) if nxt else 0
        return items

    def total(self, path: str, params: dict) -> int | None:
        _, headers = self.get(f"{API}{path}", {**params, "per_page": 1})
        value = headers.get("X-Total")
        return int(value) if value else None


def project_api_path(path: str) -> str:
    return "/projects/" + urllib.parse.quote(path, safe="")


# --------------------------------------------------------------------------- git

def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, text=True).stdout


def sync_repo(cache: Path) -> Path:
    repo = cache / "decidim-govbr.git"
    if not repo.exists():
        cache.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", "--bare", "--quiet", REPO_URL, str(repo)], check=True)
    git(repo, "fetch", "--quiet", "--prune", "--tags", REPO_URL, "+refs/heads/*:refs/heads/*")
    return repo


def collect_git(repo: Path, since: datetime) -> dict:
    sep = "\x1f"
    raw = git(repo, "log", *BRANCHES, "--no-merges", f"--format=%H{sep}%an{sep}%ae{sep}%aI{sep}%s")
    commits = []
    for line in raw.splitlines():
        sha, name, email, date, subject = line.split(sep, 4)
        commits.append({"sha": sha, "name": name, "email": email.lower(), "date": parse_dt(date), "subject": subject})

    merges = int(git(repo, "rev-list", "--count", "--merges", *BRANCHES).strip())
    first = git(repo, "log", *BRANCHES, "--reverse", "--format=%aI", "--max-parents=0").splitlines()

    hotspots = Counter()
    current = None
    for line in git(repo, "log", *BRANCHES, "--no-merges", f"--since={since.isoformat()}",
                    "--name-only", "--format=@@%H").splitlines():
        if line.startswith("@@"):
            current = line
        elif line.strip() and current:
            hotspots[line.strip()] += 1

    files = git(repo, "ls-tree", "-r", "--name-only", "main").splitlines()

    def show(path: str) -> str:
        try:
            return git(repo, "show", f"main:{path}")
        except subprocess.CalledProcessError:
            return ""

    return {
        "commits": commits,
        "merges": merges,
        "first_commit": parse_dt(first[0]) if first else None,
        "hotspots": hotspots,
        "files": files,
        "show": show,
    }


def resolve_identities(commits: list[dict]) -> dict[str, str]:
    """Agrupa variações de nome/e-mail da mesma pessoa (union-find)."""
    parent: dict[str, str] = {}

    def find(x: str) -> str:
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        parent[find(a)] = find(b)

    for c in commits:
        name_node = "n:" + norm_name(c["name"])
        find(name_node)
        if c["email"] and not PLACEHOLDER_EMAIL.search(c["email"]):
            union("e:" + c["email"], name_node)

    clusters: dict[str, Counter] = defaultdict(Counter)
    for c in commits:
        clusters[find("n:" + norm_name(c["name"]))][c["name"]] += 1

    display = {}
    for root, names in clusters.items():
        with_space = [n for n, _ in names.most_common() if " " in n.strip()]
        display[root] = with_space[0] if with_space else names.most_common(1)[0][0]

    for c in commits:
        root = find("n:" + norm_name(c["name"]))
        c["author_id"] = root
        c["author"] = display[root]
    return display


# --------------------------------------------------------------------------- métricas

def bus_factor(counter: Counter, share: float = 0.5) -> int:
    total = sum(counter.values())
    acc = 0
    for i, (_, n) in enumerate(counter.most_common(), start=1):
        acc += n
        if acc >= total * share:
            return i
    return 0


def commit_type(subject: str) -> str | None:
    if subject.startswith("Revert"):
        return "revert"
    m = CC_RE.match(subject)
    if not m:
        return None
    t = m.group("type").lower()
    return TYPE_ALIASES.get(t, t)


def commit_metrics(g: dict, now: datetime, since: datetime) -> dict:
    commits = g["commits"]
    by_year = Counter(c["date"].year for c in commits)
    by_month = Counter(month_key(c["date"]) for c in commits)
    recent = [c for c in commits if c["date"] >= since]
    previous = [c for c in commits if since - timedelta(days=365) <= c["date"] < since]

    cc_by_year = {}
    for year in sorted(by_year):
        year_commits = [c for c in commits if c["date"].year == year]
        ok = sum(1 for c in year_commits if commit_type(c["subject"]) not in (None, "revert"))
        cc_by_year[year] = pct(ok, len(year_commits))
    types_recent = Counter(commit_type(c["subject"]) or "fora do padrão" for c in recent)
    reverts_by_year = Counter(c["date"].year for c in commits if c["subject"].startswith("Revert"))
    weekday = Counter(c["date"].weekday() for c in recent)

    return {
        "total": len(commits) + g["merges"],
        "non_merge": len(commits),
        "merges": g["merges"],
        "first_commit": g["first_commit"],
        "recent": len(recent),
        "previous": len(previous),
        "by_year": dict(sorted(by_year.items())),
        "by_month": by_month,
        "cc_by_year": cc_by_year,
        "cc_recent": pct(sum(1 for c in recent if commit_type(c["subject"]) not in (None, "revert")), len(recent)),
        "types_recent": types_recent,
        "reverts_by_year": dict(sorted(reverts_by_year.items())),
        "weekday_recent": weekday,
        "hotspots": g["hotspots"].most_common(15),
    }


def contributor_metrics(commits: list[dict], now: datetime, since: datetime) -> dict:
    all_time = Counter(c["author_id"] for c in commits)
    recent = Counter(c["author_id"] for c in commits if c["date"] >= since)
    names = {c["author_id"]: c["author"] for c in commits}
    first_year = {}
    for c in sorted(commits, key=lambda c: c["date"]):
        first_year.setdefault(c["author_id"], c["date"].year)
    active_by_year = defaultdict(set)
    for c in commits:
        active_by_year[c["date"].year].add(c["author_id"])
    years = sorted(active_by_year)
    rows = []
    for y in years:
        prev = active_by_year.get(y - 1, set())
        retained = len(active_by_year[y] & prev)
        rows.append({
            "year": y,
            "active": len(active_by_year[y]),
            "new": sum(1 for a, fy in first_year.items() if fy == y),
            "retained_pct": pct(retained, len(prev)) if prev else None,
        })
    total_recent = sum(recent.values())
    total_all = sum(all_time.values())
    return {
        "total": len(all_time),
        "recent": len(recent),
        "by_year": rows,
        "bus_factor_all": bus_factor(all_time),
        "bus_factor_recent": bus_factor(recent),
        "top_all": [(names[a], n, pct(n, total_all)) for a, n in all_time.most_common(10)],
        "top_recent": [(names[a], n, pct(n, total_recent)) for a, n in recent.most_common(10)],
        "new_recent": sum(1 for a in recent if first_year[a] >= since.year and
                          min(c["date"] for c in commits if c["author_id"] == a) >= since),
    }


def mr_metrics(mrs: list[dict], now: datetime, since: datetime) -> dict:
    for mr in mrs:
        mr["_created"] = parse_dt(mr["created_at"])
        mr["_merged"] = parse_dt(mr.get("merged_at"))
        mr["_closed"] = parse_dt(mr.get("closed_at"))
        merger = mr.get("merge_user") or mr.get("merged_by") or {}
        mr["_self_merged"] = bool(mr["_merged"] and merger and merger.get("id") == mr["author"]["id"])

    states = Counter(mr["state"] for mr in mrs)
    by_year = defaultdict(lambda: {"created": 0, "merged": 0, "closed": 0, "ttm": [], "commented": 0,
                                   "self": 0, "authors": set(), "targets": Counter()})
    for mr in mrs:
        y = by_year[mr["_created"].year]
        y["created"] += 1
        y["authors"].add(mr["author"]["id"])
        y["targets"][mr["target_branch"]] += 1
        if mr["state"] == "merged":
            y["merged"] += 1
            y["ttm"].append((mr["_merged"] - mr["_created"]).total_seconds() / 86400)
            y["self"] += mr["_self_merged"]
        elif mr["state"] == "closed":
            y["closed"] += 1
        if mr.get("user_notes_count", 0) > 0:
            y["commented"] += 1

    year_rows = []
    for year in sorted(by_year):
        y = by_year[year]
        decided = y["merged"] + y["closed"]
        year_rows.append({
            "year": year, "created": y["created"], "merged": y["merged"], "closed": y["closed"],
            "acceptance": pct(y["merged"], decided), "ttm_median": median(y["ttm"]),
            "ttm_p90": percentile(y["ttm"], 0.9), "commented": pct(y["commented"], y["created"]),
            "self_merged": pct(y["self"], y["merged"]), "authors": len(y["authors"]),
            "targets": dict(y["targets"]),
        })

    recent = [mr for mr in mrs if mr["_created"] >= since]
    recent_merged = [mr for mr in recent if mr["state"] == "merged"]
    recent_decided = [mr for mr in recent if mr["state"] in ("merged", "closed")]
    created_month = Counter(month_key(mr["_created"]) for mr in mrs)
    merged_month = Counter(month_key(mr["_merged"]) for mr in mrs if mr["_merged"])
    open_mrs = sorted((mr for mr in mrs if mr["state"] == "opened"), key=lambda m: m["_created"])
    return {
        "total": len(mrs),
        "states": dict(states),
        "years": year_rows,
        "recent": {
            "created": len(recent),
            "merged": len(recent_merged),
            "acceptance": pct(len(recent_merged), len(recent_decided)),
            "ttm_median": median([(m["_merged"] - m["_created"]).total_seconds() / 86400 for m in recent_merged]),
            "ttm_p90": percentile([(m["_merged"] - m["_created"]).total_seconds() / 86400 for m in recent_merged], 0.9),
            "commented": pct(sum(1 for m in recent if m.get("user_notes_count", 0) > 0), len(recent)),
            "self_merged": pct(sum(m["_self_merged"] for m in recent_merged), len(recent_merged)),
            "authors": len({m["author"]["id"] for m in recent}),
            "targets": dict(Counter(m["target_branch"] for m in recent)),
        },
        "created_month": created_month,
        "merged_month": merged_month,
        "open": [{"iid": m["iid"], "title": m["title"], "age": (now - m["_created"]).days,
                  "target": m["target_branch"], "draft": m.get("draft", False)} for m in open_mrs],
    }


def issue_metrics(issues: list[dict], now: datetime, since: datetime) -> dict:
    for it in issues:
        it["_created"] = parse_dt(it["created_at"])
        it["_closed"] = parse_dt(it.get("closed_at"))
    by_year = defaultdict(lambda: {"opened": 0, "closed": 0, "ttc": []})
    for it in issues:
        by_year[it["_created"].year]["opened"] += 1
        if it["_closed"]:
            by_year[it["_closed"].year]["closed"] += 1
            by_year[it["_created"].year]["ttc"].append((it["_closed"] - it["_created"]).total_seconds() / 86400)
    open_issues = [it for it in issues if it["state"] == "opened"]
    ages = [(now - it["_created"]).days for it in open_issues]
    buckets = Counter()
    for a in ages:
        if a <= 30:
            buckets["até 30 dias"] += 1
        elif a <= 90:
            buckets["31 a 90 dias"] += 1
        elif a <= 365:
            buckets["91 dias a 1 ano"] += 1
        else:
            buckets["mais de 1 ano"] += 1
    recent_closed = [it for it in issues if it["_closed"] and it["_closed"] >= since]
    labels = Counter(label for it in open_issues for label in it.get("labels", []))
    return {
        "total": len(issues),
        "open": len(open_issues),
        "closed": len(issues) - len(open_issues),
        "years": [{"year": y, "opened": v["opened"], "closed": v["closed"], "ttc_median": median(v["ttc"])}
                  for y, v in sorted(by_year.items())],
        "recent_opened": sum(1 for it in issues if it["_created"] >= since),
        "recent_closed": len(recent_closed),
        "recent_ttc_median": median([(it["_closed"] - it["_created"]).total_seconds() / 86400 for it in recent_closed]),
        "open_age_buckets": {k: buckets.get(k, 0) for k in ["até 30 dias", "31 a 90 dias", "91 dias a 1 ano", "mais de 1 ano"]},
        "open_over_year_pct": pct(buckets.get("mais de 1 ano", 0), len(open_issues)),
        "open_labels": labels.most_common(10),
        "authors_recent": len({it["author"]["id"] for it in issues if it["_created"] >= since}),
    }


def pipeline_metrics(pipelines: list[dict]) -> dict:
    groups = {"develop": [], "main": [], "todas": pipelines}
    for p in pipelines:
        if p["ref"] in ("develop", "main"):
            groups[p["ref"]].append(p)
    result = {}
    for name, items in groups.items():
        st = Counter(p["status"] for p in items)
        result[name] = {"total": len(items), "success": st.get("success", 0), "failed": st.get("failed", 0),
                        "canceled": st.get("canceled", 0),
                        "other": len(items) - st.get("success", 0) - st.get("failed", 0) - st.get("canceled", 0),
                        "success_rate": pct(st.get("success", 0), st.get("success", 0) + st.get("failed", 0))}
    return result


def tag_metrics(tags: list[dict], since: datetime) -> dict:
    rows = []
    for t in tags:
        date = parse_dt((t.get("commit") or {}).get("committed_date") or (t.get("commit") or {}).get("created_at"))
        rows.append({"name": t["name"], "date": date, "stable": bool(STABLE_TAG.match(t["name"]))})
    rows.sort(key=lambda r: r["date"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)
    stable = [r for r in rows if r["stable"]]
    recent_stable = [r for r in stable if r["date"] and r["date"] >= since]
    by_year = Counter(r["date"].year for r in stable if r["date"])
    return {
        "total": len(rows),
        "stable": len(stable),
        "latest": rows[0] if rows else None,
        "latest_stable": stable[0] if stable else None,
        "recent_stable": len(recent_stable),
        "stable_by_year": dict(sorted(by_year.items())),
    }


def quality_checks(g: dict, now: datetime, http: Http) -> dict:
    files = g["files"]
    fileset = set(files)
    root_files = {f for f in files if "/" not in f}

    def has(pattern: str) -> list[str]:
        rx = re.compile(pattern, re.I)
        return sorted(f for f in files if rx.search(f))

    lock = g["show"]("Gemfile.lock")
    gemfile = g["show"]("Gemfile")
    ci = g["show"](".gitlab-ci.yml")
    contributing = g["show"]("CONTRIBUTING.md")
    rubocop_todo = g["show"](".rubocop_todo.yml")

    def lock_version(gem: str) -> str | None:
        m = re.search(rf"^    {re.escape(gem)} \(([^)]+)\)", lock, re.M)
        return m.group(1) if m else None

    ruby_version = g["show"](".ruby-version").strip() or None
    rails_version = lock_version("rails")
    decidim_version = lock_version("decidim")

    def eol(product: str, version: str | None) -> dict:
        if not version:
            return {}
        cycle = ".".join(version.split(".")[:2])
        try:
            data, _ = http.get(f"https://endoflife.date/api/{product}.json")
        except Exception:  # noqa: BLE001 - fonte externa opcional
            return {"cycle": cycle}
        for row in data:
            if row["cycle"] == cycle:
                eol_date = row["eol"] if isinstance(row["eol"], str) else None
                return {"cycle": cycle, "eol": fmt_date(datetime.fromisoformat(eol_date)) if eol_date else None, "latest_cycle": data[0]["cycle"],
                        "supported": (eol_date is None) or (datetime.fromisoformat(eol_date).date() > now.date())}
        return {"cycle": cycle}

    try:
        decidim_latest, _ = http.get("https://rubygems.org/api/v1/versions/decidim/latest.json")
        decidim_latest = decidim_latest.get("version")
    except Exception:  # noqa: BLE001
        decidim_latest = None

    minors_behind = None
    if decidim_version and decidim_latest:
        a, b = decidim_version.split("."), decidim_latest.split(".")
        if a[0] == b[0]:
            minors_behind = int(b[1]) - int(a[1])

    jobs = {}
    for m in re.finditer(r"^([A-Za-z][\w-]*):\n((?:[ \t].*\n|\n)*)", ci, re.M):
        body = m.group(2)
        stage = re.search(r"^\s+stage:\s*(\S+)", body, re.M)
        if stage:
            jobs[m.group(1)] = {"stage": stage.group(1),
                                "allow_failure": bool(re.search(r"^\s+allow_failure:\s*true", body, re.M))}

    git_deps = []
    for m in re.finditer(r"^\s*gem ['\"]([^'\"]+)['\"]([^\n]*)", gemfile, re.M):
        name, rest = m.group(1), m.group(2)
        if "git:" in rest or "github:" in rest or "gitlab:" in rest:
            branch = re.search(r"branch:\s*['\"]([^'\"]+)", rest)
            pinned = re.search(r"(tag|ref):", rest)
            git_deps.append({"gem": name, "branch": branch.group(1) if branch else None, "pinned": bool(pinned)})

    todo_cops = re.findall(r"^[A-Z][A-Za-z]+/[A-Za-z]+:", rubocop_todo, re.M)
    todo_offenses = sum(int(n) for n in re.findall(r"# Offense count: (\d+)", rubocop_todo))

    app_rb = [f for f in files if f.startswith("app/") and f.endswith(".rb")]
    specs = [f for f in files if f.startswith("spec/") and f.endswith("_spec.rb")]
    minitests = [f for f in files if f.startswith("test/") and f.endswith("_test.rb")]

    return {
        "license": has(r"^(LICEN[CS]E|COPYING)[^/]*$"),
        "readme": has(r"^README[^/]*$"),
        "contributing": has(r"^CONTRIBUTING[^/]*$"),
        "code_of_conduct": has(r"^CODE[-_]OF[-_]CONDUCT[^/]*$"),
        "security": has(r"^SECURITY[^/]*$"),
        "changelog": has(r"^(CHANGELOG|HISTORY|CHANGES)[^/]*$"),
        "mr_templates": has(r"^\.gitlab/merge_request_templates/"),
        "issue_templates": has(r"^\.gitlab/issue_templates/"),
        "contributing_issue_link_ok": (PROJECT_PATH + "/-/issues") in contributing if contributing else None,
        "committed_reports": sorted(f for f in root_files if re.search(r"(brakeman|report).*\.(html|json)$", f, re.I)),
        "gemfile_lock": "Gemfile.lock" in fileset,
        "js_lock": [f for f in ("yarn.lock", "package-lock.json") if f in fileset],
        "ci_jobs": jobs,
        "git_deps": git_deps,
        "rubocop_todo_cops": len(todo_cops),
        "rubocop_todo_offenses": todo_offenses,
        "app_rb": len(app_rb),
        "specs": len(specs),
        "minitests": len(minitests),
        "test_ratio": (len(specs) + len(minitests)) / len(app_rb) if app_rb else None,
        "simplecov": "simplecov" in lock,
        "ruby": {"version": ruby_version, **eol("ruby", ruby_version)},
        "rails": {"version": rails_version, **eol("rails", rails_version)},
        "decidim": {"version": decidim_version, "latest": decidim_latest, "minors_behind": minors_behind},
    }


def ecosystem_metrics(http: Http, since: datetime) -> list[dict]:
    rows = []
    for gem, path in ECOSYSTEM:
        base = project_api_path(path)
        try:
            info, _ = http.get(f"{API}{base}")
            commits = http.paginate(f"{base}/repository/commits", {"since": since.isoformat(), "all": "true"})
            merged = http.total(f"{base}/merge_requests", {"state": "merged"})
        except urllib.error.HTTPError:
            rows.append({"gem": gem, "path": path, "error": True})
            continue
        rows.append({
            "gem": gem, "path": path,
            "commits_recent": len(commits),
            "authors_recent": len({c["author_email"].lower() for c in commits}),
            "merged_mrs": merged,
            "last_activity": parse_dt(info.get("last_activity_at")),
            "stars": info.get("star_count"), "forks": info.get("forks_count"),
        })
    return rows


# --------------------------------------------------------------------------- avaliação

GREEN, YELLOW, RED, GRAY = ":green_circle:", ":yellow_circle:", ":red_circle:", ":white_circle:"


def grade(value, good, ok, higher_is_better=True):
    if value is None:
        return GRAY
    if higher_is_better:
        return GREEN if value >= good else YELLOW if value >= ok else RED
    return GREEN if value <= good else YELLOW if value <= ok else RED


def yes(flag) -> str:
    return ":white_check_mark:" if flag else ":x:"


# --------------------------------------------------------------------------- renderização

def xychart(title: str, labels: list[str], series: list[tuple[str, list[float]]], y_label: str) -> str:
    top = max([max(vals) for _, vals in series if vals] + [1])
    top = int(math.ceil(top * 1.1))
    lines = ["```mermaid", "xychart-beta", f'    title "{title}"',
             "    x-axis [" + ", ".join(f'"{l}"' for l in labels) + "]",
             f'    y-axis "{y_label}" 0 --> {top}']
    for kind, vals in series:
        lines.append(f"    {kind} [" + ", ".join(str(round(v, 1)) for v in vals) + "]")
    lines.append("```")
    return "\n".join(lines)


def pie(title: str, items: list[tuple[str, float]]) -> str:
    lines = ["```mermaid", f'pie showData title {title}']
    lines += [f'    "{k}" : {v}' for k, v in items if v]
    lines.append("```")
    return "\n".join(lines)


def table(headers: list[str], rows: list[list], align: str | None = None) -> str:
    align = align or "l" * len(headers)
    sep = ["---:" if a == "r" else "---" for a in align]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep) + " |"]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return "\n".join(out)


def header(title: str, meta: dict) -> str:
    return (f"<!-- Gerado por scripts/estatisticas.py em {meta['generated']}. Não edite à mão. -->\n\n"
            f"# {title}\n\n"
            f'!!! info "Coleta de {meta["generated_date"]}"\n'
            f"    Branches `main` e `develop` do [decidim-govbr](https://gitlab.com/{PROJECT_PATH}) e API pública do GitLab. "
            f"\"Últimos 12 meses\" = {meta['since_date']} a {meta['generated_date']}. "
            "Para atualizar, rode `python3 scripts/estatisticas.py`.\n\n")


def render_index(d: dict, meta: dict) -> str:
    c, ct, mr, iss, pl, tg, q = d["commits"], d["contributors"], d["mrs"], d["issues"], d["pipelines"], d["tags"], d["quality"]
    trend = pct(c["recent"] - c["previous"], c["previous"]) if c["previous"] else None
    trend_txt = "—" if trend is None else f"{trend:+.0f}% vs. 12 meses anteriores"
    latest = tg["latest_stable"]
    out = [header("Estatísticas do Projeto", meta)]
    out.append(
        "Indicadores de atividade, colaboração e qualidade do `decidim-govbr`, organizados segundo métricas da "
        "comunidade [CHAOSS](https://chaoss.community/) e critérios do selo de boas práticas da "
        "[OpenSSF](https://www.bestpractices.dev/).\n")
    out.append('<div class="grid cards" markdown>\n')
    cards = [
        (":material-source-commit:", "Commits", f"**{fmt_int(c['total'])}** no total",
         f"{fmt_int(c['recent'])} nos últimos 12 meses ({trend_txt})", "commits.md"),
        (":material-source-pull:", "Merge requests", f"**{fmt_int(mr['states'].get('merged'))}** integrados",
         f"Mediana de {fmt_days(mr['recent']['ttm_median'])} até o merge (12 meses)", "merge-requests.md"),
        (":material-account-group:", "Contribuidores", f"**{fmt_int(ct['total'])}** pessoas",
         f"{fmt_int(ct['recent'])} ativas nos últimos 12 meses", "contribuicoes.md"),
        (":material-shield-check:", "Qualidade", f"Pipelines da `develop`: **{fmt_pct(pl['develop']['success_rate'])}** de sucesso",
         f"Fator de ausência (12 meses): {ct['bus_factor_recent']}", "qualidade.md"),
    ]
    for icon, title, big, small, link in cards:
        out.append(f"-   {icon}{{ .lg .middle }} **{title}**\n\n    ---\n\n    {big}\n\n    {small}\n\n"
                   f"    [:octicons-arrow-right-24: Detalhes]({link})\n")
    out.append("</div>\n")

    out.append("## Resumo\n")
    out.append(table(["Indicador", "Valor"], [
        ["Primeiro commit", fmt_date(c["first_commit"])],
        ["Commits (total / últimos 12 meses)", f"{fmt_int(c['total'])} / {fmt_int(c['recent'])}"],
        ["Contribuidores (total / ativos em 12 meses)", f"{fmt_int(ct['total'])} / {fmt_int(ct['recent'])}"],
        ["Merge requests (integrados / fechados sem merge / abertos)",
         f"{fmt_int(mr['states'].get('merged'))} / {fmt_int(mr['states'].get('closed'))} / {fmt_int(mr['states'].get('opened'))}"],
        ["Issues (abertas / fechadas)", f"{fmt_int(iss['open'])} / {fmt_int(iss['closed'])}"],
        ["Versões (tags estáveis / total de tags)", f"{fmt_int(tg['stable'])} / {fmt_int(tg['total'])}"],
        ["Última versão estável", f"`{latest['name']}` em {fmt_date(latest['date'])}" if latest else "—"],
        ["Pipelines nos últimos 12 meses", fmt_int(pl["todas"]["total"])],
        ["Estrelas / forks no GitLab", f"{fmt_int(d['project'].get('star_count'))} / {fmt_int(d['project'].get('forks_count'))}"],
        ["Linguagens (GitLab)", ", ".join(f"{k} {v:.0f}%" for k, v in d["languages"].items())],
    ]))
    out.append("\n## Painel de indicadores\n")
    out.append("Situação dos principais indicadores nos últimos 12 meses. As faixas estão em "
               "[Qualidade](qualidade.md#como-ler-os-indicadores).\n")
    out.append(table(["", "Indicador", "Valor"], indicator_rows(d)[:8], "lll"))
    out.append("\n## Ecossistema de componentes\n")
    rows = []
    for e in d["ecosystem"]:
        if e.get("error"):
            rows.append([f"`{e['gem']}`", "—", "—", "—", "—"])
            continue
        rows.append([f"[`{e['gem']}`](https://gitlab.com/{e['path']})", fmt_int(e["commits_recent"]),
                     fmt_int(e["authors_recent"]), fmt_int(e["merged_mrs"]), fmt_date(e["last_activity"])])
    out.append(table(["Componente", "Commits (12 meses)", "Autores (12 meses)", "MRs integrados", "Última atividade"],
                     rows, "lrrrl"))
    out.append("\n\nComponentes instalados no Gemfile do core. Contagem em todas as branches de cada repositório.\n")
    return "\n".join(out) + "\n"


def indicator_rows(d: dict) -> list[list]:
    c, ct, mr, iss, pl, tg, q = d["commits"], d["contributors"], d["mrs"], d["issues"], d["pipelines"], d["tags"], d["quality"]
    r = mr["recent"]
    rows = [
        [grade(ct["bus_factor_recent"], 4, 2), "Fator de ausência (pessoas que somam 50% dos commits)", str(ct["bus_factor_recent"])],
        [grade(ct["recent"], 10, 5), "Contribuidores ativos", fmt_int(ct["recent"])],
        [grade(pl["develop"]["success_rate"], 90, 70), "Sucesso de pipelines na `develop`", fmt_pct(pl["develop"]["success_rate"])],
        [grade(r["ttm_median"], 3, 10, higher_is_better=False), "Mediana de tempo até o merge", fmt_days(r["ttm_median"])],
        [grade(r["commented"], 70, 40), "MRs com ao menos um comentário", fmt_pct(r["commented"])],
        [grade(r["self_merged"], 10, 30, higher_is_better=False), "MRs integrados pelo próprio autor", fmt_pct(r["self_merged"])],
        [grade(iss["recent_ttc_median"], 30, 90, higher_is_better=False), "Mediana de tempo para fechar issues", fmt_days(iss["recent_ttc_median"])],
        [grade(c["cc_recent"], 80, 50), "Commits no padrão Conventional Commits", fmt_pct(c["cc_recent"])],
        [grade(iss["open_over_year_pct"], 20, 50, higher_is_better=False), "Issues abertas há mais de 1 ano", fmt_pct(iss["open_over_year_pct"])],
        [grade(tg["recent_stable"], 4, 1), "Versões estáveis publicadas", fmt_int(tg["recent_stable"])],
        [GREEN if q["ruby"].get("supported") else RED if q["ruby"].get("supported") is False else GRAY,
         "Ruby com suporte", f"{q['ruby']['version']} (fim do suporte: {q['ruby'].get('eol', '—')})"],
        [GREEN if q["rails"].get("supported") else RED if q["rails"].get("supported") is False else GRAY,
         "Rails com suporte", f"{q['rails']['version']} (fim do suporte: {q['rails'].get('eol', '—')})"],
        [grade(q["decidim"]["minors_behind"], 0, 2, higher_is_better=False), "Defasagem do Decidim (versões menores)",
         f"{q['decidim']['version']} → {q['decidim']['latest']} ({q['decidim']['minors_behind']} atrás)"],
    ]
    return rows


def render_commits(d: dict, meta: dict) -> str:
    c = d["commits"]
    now = meta["now"]
    months = last_months(now, 24)
    out = [header("Commits", meta)]
    out.append("Commits das branches `main` e `develop`, sem duplicar os que estão nas duas. "
               "Commits de merge são contados à parte.\n")
    out.append(table(["Total", "Sem merge", "Merges", "Últimos 12 meses", "12 meses anteriores"],
                     [[fmt_int(c["total"]), fmt_int(c["non_merge"]), fmt_int(c["merges"]),
                       fmt_int(c["recent"]), fmt_int(c["previous"])]], "rrrrr"))
    out.append("\n## Por ano\n")
    years = list(c["by_year"].keys())
    out.append(xychart("Commits por ano (sem merge)", [str(y) for y in years],
                       [("bar", [c["by_year"][y] for y in years])], "Commits"))
    out.append("\n## Últimos 24 meses\n")
    out.append(xychart("Commits por mês (sem merge)", [month_label(m) for m in months],
                       [("bar", [c["by_month"].get(m, 0) for m in months])], "Commits"))
    out.append('\n??? note "Dados mensais"\n')
    out.append("    " + table(["Mês", "Commits"], [[month_label(m), c["by_month"].get(m, 0)] for m in months], "lr")
               .replace("\n", "\n    ") + "\n")
    out.append("## Padrão das mensagens\n")
    out.append("Percentual de commits cujo título segue o formato [Conventional Commits]"
               "(https://www.conventionalcommits.org/pt-br/) (`tipo(escopo): descrição`), adotado pelo projeto.\n")
    out.append(table(["Ano", "Conventional Commits", "Reverts"],
                     [[y, fmt_pct(c["cc_by_year"].get(y)), fmt_int(c["reverts_by_year"].get(y, 0))] for y in years], "lrr"))
    out.append("\n### Tipos de commit nos últimos 12 meses\n")
    types = c["types_recent"].most_common(8)
    others = sum(c["types_recent"].values()) - sum(v for _, v in types)
    if others:
        types.append(("outros", others))
    out.append(pie("Tipos de commit (12 meses)", types))
    out.append("\n## Arquivos mais alterados (12 meses)\n")
    out.append("Arquivos que mais aparecem em commits. Muitas alterações no mesmo arquivo indicam pontos de "
               "concentração de mudanças (*hotspots*), candidatos a refatoração ou a mais testes.\n")
    out.append(table(["Arquivo", "Commits"], [[f"`{f}`", n] for f, n in c["hotspots"]], "lr"))
    out.append("\n")
    return "\n".join(out) + "\n"


def render_mrs(d: dict, meta: dict) -> str:
    mr = d["mrs"]
    now = meta["now"]
    months = last_months(now, 24)
    r = mr["recent"]
    out = [header("Merge Requests", meta)]
    out.append(table(["Total", "Integrados", "Fechados sem merge", "Abertos"],
                     [[fmt_int(mr["total"]), fmt_int(mr["states"].get("merged")),
                       fmt_int(mr["states"].get("closed")), fmt_int(mr["states"].get("opened"))]], "rrrr"))
    out.append("\n## Últimos 12 meses\n")
    out.append(table(["Indicador", "Valor", "O que mede"], [
        ["MRs abertos", fmt_int(r["created"]), "Volume de propostas de mudança"],
        ["MRs integrados", fmt_int(r["merged"]), "Mudanças aceitas"],
        ["Taxa de aceitação", fmt_pct(r["acceptance"]), "Integrados ÷ (integrados + fechados sem merge)"],
        ["Mediana até o merge", fmt_days(r["ttm_median"]), "Tempo típico entre abrir e integrar"],
        ["90º percentil até o merge", fmt_days(r["ttm_p90"]), "Tempo dos MRs mais demorados"],
        ["MRs com comentário", fmt_pct(r["commented"]), "Indício de revisão (comentários de qualquer pessoa)"],
        ["Integrados pelo próprio autor", fmt_pct(r["self_merged"]), "MRs sem uma segunda pessoa no merge"],
        ["Autores distintos", fmt_int(r["authors"]), "Quantas pessoas propuseram mudanças"],
    ], "lrl"))
    out.append("\n## Por mês\n")
    out.append("Barras: MRs abertos no mês. Linha: MRs integrados no mês.\n")
    out.append(xychart("Merge requests por mês", [month_label(m) for m in months],
                       [("bar", [mr["created_month"].get(m, 0) for m in months]),
                        ("line", [mr["merged_month"].get(m, 0) for m in months])], "MRs"))
    out.append("\n## Por ano\n")
    out.append(table(["Ano", "Abertos", "Integrados", "Aceitação", "Mediana até merge", "P90 até merge",
                      "Com comentário", "Auto-merge", "Autores"],
                     [[y["year"], y["created"], y["merged"], fmt_pct(y["acceptance"]), fmt_days(y["ttm_median"]),
                       fmt_days(y["ttm_p90"]), fmt_pct(y["commented"]), fmt_pct(y["self_merged"]), y["authors"]]
                      for y in mr["years"]], "lrrrrrrrr"))
    out.append("\n## Branch de destino\n")
    out.append("Para quais branches os MRs foram abertos em cada ano. O fluxo atual é MR para `develop` e promoção de `develop` para `main`.\n")
    branches = sorted({b for y in mr["years"] for b in y["targets"]},
                      key=lambda b: -sum(y["targets"].get(b, 0) for y in mr["years"]))[:4]
    out.append(table(["Ano", *[f"`{b}`" for b in branches]],
                     [[y["year"], *[y["targets"].get(b, 0) for b in branches]] for y in mr["years"]],
                     "l" + "r" * len(branches)))
    out.append("\n## Abertos agora\n")
    if mr["open"]:
        out.append(table(["MR", "Título", "Destino", "Idade"],
                         [[f"[!{m['iid']}](https://gitlab.com/{PROJECT_PATH}/-/merge_requests/{m['iid']})",
                           m["title"].replace("|", "\\|"), f"`{m['target']}`", f"{m['age']} dias"] for m in mr["open"]],
                         "llll"))
    else:
        out.append("Nenhum MR aberto.")
    out.append("\n")
    return "\n".join(out) + "\n"


def render_contrib(d: dict, meta: dict) -> str:
    ct, iss = d["contributors"], d["issues"]
    out = [header("Contribuições", meta)]
    out.append('!!! note "Identidades"\n    Uma mesma pessoa pode ter feito commits com nomes ou e-mails diferentes. '
               "As variações são agrupadas automaticamente (mesmo e-mail ou mesmo nome normalizado). "
               "A contagem é uma aproximação.\n")
    out.append("## Pessoas contribuindo\n")
    years = ct["by_year"]
    out.append(xychart("Contribuidores ativos por ano", [str(y["year"]) for y in years],
                       [("bar", [y["active"] for y in years]), ("line", [y["new"] for y in years])], "Pessoas"))
    out.append("\nBarras: pessoas com ao menos um commit no ano. Linha: pessoas que fizeram o primeiro commit no ano.\n")
    out.append(table(["Ano", "Ativas", "Novas", "Retenção"],
                     [[y["year"], y["active"], y["new"], fmt_pct(y["retained_pct"])] for y in years], "lrrr"))
    out.append("\n*Retenção*: parcela das pessoas ativas no ano anterior que continuaram contribuindo.\n")
    out.append("## Concentração das contribuições\n")
    out.append(f"O **fator de ausência** (*Contributor Absence Factor*, CHAOSS) é o menor número de pessoas que "
               f"somam metade dos commits. Quanto menor, maior o risco de o projeto parar se essas pessoas saírem.\n")
    out.append(table(["Período", "Fator de ausência", "Contribuidores"],
                     [["Todo o histórico", ct["bus_factor_all"], ct["total"]],
                      ["Últimos 12 meses", ct["bus_factor_recent"], ct["recent"]]], "lrr"))
    out.append("\n=== \"Últimos 12 meses\"\n\n")
    out.append("    " + table(["#", "Pessoa", "Commits", "Participação"],
                              [[i, n, c, fmt_pct(p)] for i, (n, c, p) in enumerate(ct["top_recent"], 1)], "rlrr")
               .replace("\n", "\n    "))
    out.append("\n\n=== \"Todo o histórico\"\n\n")
    out.append("    " + table(["#", "Pessoa", "Commits", "Participação"],
                              [[i, n, c, fmt_pct(p)] for i, (n, c, p) in enumerate(ct["top_all"], 1)], "rlrr")
               .replace("\n", "\n    "))
    out.append("\n\n## Issues\n")
    out.append("Só issues públicas aparecem na API sem autenticação.\n")
    out.append(table(["Abertas", "Fechadas", "Abertas em 12 meses", "Fechadas em 12 meses",
                      "Mediana para fechar (12 meses)", "Autores (12 meses)"],
                     [[fmt_int(iss["open"]), fmt_int(iss["closed"]), fmt_int(iss["recent_opened"]),
                       fmt_int(iss["recent_closed"]), fmt_days(iss["recent_ttc_median"]),
                       fmt_int(iss["authors_recent"])]], "rrrrrr"))
    out.append("\n### Por ano\n")
    out.append(xychart("Issues abertas e fechadas por ano", [str(y["year"]) for y in iss["years"]],
                       [("bar", [y["opened"] for y in iss["years"]]), ("line", [y["closed"] for y in iss["years"]])],
                       "Issues"))
    out.append("\nBarras: issues abertas no ano. Linha: issues fechadas no ano.\n")
    out.append(table(["Ano", "Abertas", "Fechadas", "Mediana para fechar"],
                     [[y["year"], y["opened"], y["closed"], fmt_days(y["ttc_median"])] for y in iss["years"]], "lrrr"))
    out.append("\n### Idade das issues abertas\n")
    out.append(pie("Issues abertas por idade", list(iss["open_age_buckets"].items())))
    if iss["open_labels"]:
        out.append("\n### Rótulos mais comuns nas issues abertas\n")
        out.append(table(["Rótulo", "Issues"], [[f"`{l}`", n] for l, n in iss["open_labels"]], "lr"))
    out.append("\n")
    return "\n".join(out) + "\n"


def render_quality(d: dict, meta: dict) -> str:
    q, pl, tg = d["quality"], d["pipelines"], d["tags"]
    out = [header("Qualidade e Boas Práticas", meta)]
    out.append("Indicadores de saúde de projeto de software livre, inspirados nas métricas da "
               "[CHAOSS](https://chaoss.community/) e nos critérios do "
               "[selo de boas práticas da OpenSSF](https://www.bestpractices.dev/pt-BR/criteria/0).\n")
    out.append("## Indicadores\n")
    out.append(table(["", "Indicador", "Valor"], indicator_rows(d), "lll"))
    out.append("\n### Como ler os indicadores\n")
    out.append("As faixas abaixo são referências adotadas nesta documentação para orientar a leitura. "
               "A CHAOSS define as métricas, mas não estabelece faixas.\n")
    out.append(table(["Indicador", ":green_circle:", ":yellow_circle:", ":red_circle:"], [
        ["Fator de ausência", "4 ou mais", "2 a 3", "1"],
        ["Contribuidores ativos (12 meses)", "10 ou mais", "5 a 9", "menos de 5"],
        ["Sucesso de pipelines", "90% ou mais", "70% a 89%", "menos de 70%"],
        ["Mediana até o merge", "até 3 dias", "até 10 dias", "mais de 10 dias"],
        ["MRs com comentário", "70% ou mais", "40% a 69%", "menos de 40%"],
        ["MRs integrados pelo autor", "até 10%", "até 30%", "mais de 30%"],
        ["Mediana para fechar issues", "até 30 dias", "até 90 dias", "mais de 90 dias"],
        ["Conventional Commits", "80% ou mais", "50% a 79%", "menos de 50%"],
        ["Issues abertas há mais de 1 ano", "até 20%", "até 50%", "mais de 50%"],
        ["Versões estáveis em 12 meses", "4 ou mais", "1 a 3", "nenhuma"],
        ["Ruby e Rails", "com suporte", "—", "sem suporte"],
        ["Defasagem do Decidim", "versão atual", "1 a 2 versões menores", "3 ou mais"],
    ], "llll"))

    out.append("\n## Integração contínua\n")
    out.append(table(["Job", "Estágio", "Bloqueia o pipeline?"],
                     [[f"`{name}`", f"`{j['stage']}`", "Não (`allow_failure`)" if j["allow_failure"] else "Sim"]
                      for name, j in q["ci_jobs"].items()], "lll"))
    out.append("\n### Pipelines nos últimos 12 meses\n")
    out.append(table(["Branch", "Pipelines", "Sucesso", "Falha", "Cancelados", "Outros", "Taxa de sucesso"],
                     [[f"`{name}`" if name != "todas" else "todas as branches", v["total"], v["success"], v["failed"],
                       v["canceled"], v["other"], fmt_pct(v["success_rate"])] for name, v in pl.items()], "lrrrrrr"))
    out.append("\nTaxa de sucesso = sucesso ÷ (sucesso + falha). Jobs com `allow_failure` não derrubam o pipeline.\n")

    out.append("## Testes e análise estática\n")
    out.append(table(["Item", "Valor"], [
        ["Arquivos Ruby em `app/`", fmt_int(q["app_rb"])],
        ["Arquivos de teste RSpec (`spec/`)", fmt_int(q["specs"])],
        ["Arquivos de teste Minitest (`test/`)", fmt_int(q["minitests"])],
        ["Arquivos de teste por arquivo de `app/`", "—" if q["test_ratio"] is None else f"{q['test_ratio']:.2f}".replace(".", ",")],
        ["Cobertura publicada", "Não (SimpleCov instalado, sem relatório no CI)" if q["simplecov"] else "Não"],
        ["Regras RuboCop desativadas em `.rubocop_todo.yml`", fmt_int(q["rubocop_todo_cops"])],
        ["Ocorrências pendentes no `.rubocop_todo.yml`", fmt_int(q["rubocop_todo_offenses"])],
    ], "lr"))

    out.append("\n## Dependências e plataforma\n")
    out.append(table(["Item", "Versão em uso", "Situação"], [
        ["Ruby", q["ruby"]["version"], f"fim do suporte em {q['ruby'].get('eol', '—')}; ciclo atual {q['ruby'].get('latest_cycle', '—')}"],
        ["Rails", q["rails"]["version"], f"fim do suporte em {q['rails'].get('eol', '—')}; ciclo atual {q['rails'].get('latest_cycle', '—')}"],
        ["Decidim", q["decidim"]["version"], f"versão mais recente: {q['decidim']['latest']}"],
        ["Gemfile.lock", yes(q["gemfile_lock"]), "Versões de gems travadas"],
        ["Lockfile JavaScript", ", ".join(q["js_lock"]) or ":x:", "Versões de pacotes travadas"],
    ], "lll"))
    if q["git_deps"]:
        out.append("\n### Gems instaladas direto de repositórios git\n")
        out.append("Gems apontadas para uma branch mudam a cada `bundle update`. A versão efetiva fica só no "
                   "`Gemfile.lock`.\n")
        out.append(table(["Gem", "Branch", "Tag ou commit fixo?"],
                         [[f"`{g['gem']}`", f"`{g['branch']}`" if g["branch"] else "padrão", yes(g["pinned"])]
                          for g in q["git_deps"]], "lll"))

    out.append("\n## Checklist de boas práticas\n")
    checks = [
        ("Licença de software livre", q["license"], "AGPLv3. O nome do arquivo não é o padrão (`LICENSE`), por isso "
         "o GitLab não detecta a licença" if q["license"] and "LICENSE" not in q["license"] else ""),
        ("README", q["readme"], ""),
        ("Guia de contribuição", q["contributing"],
         "Os links de issues apontam para outro projeto" if q["contributing_issue_link_ok"] is False else ""),
        ("Código de conduta", q["code_of_conduct"], ""),
        ("Política de segurança (`SECURITY.md`)", q["security"], "Sem canal documentado para relatar vulnerabilidades"),
        ("Registro de mudanças (`CHANGELOG`)", q["changelog"], f"{tg['total']} tags, sem notas de versão"),
        ("Template de merge request", q["mr_templates"], ""),
        ("Template de issue", q["issue_templates"], ""),
        ("Lint no CI", any(j["stage"] == "lint" for j in q["ci_jobs"].values()), ""),
        ("Testes automatizados no CI", any(j["stage"] == "test" and not j["allow_failure"] for j in q["ci_jobs"].values()), ""),
        ("Análise de segurança (SAST)", "SAST" in q["ci_jobs"],
         "Não bloqueia o pipeline" if q["ci_jobs"].get("SAST", {}).get("allow_failure") else ""),
        ("Análise de dependências (SCA)", "SCA" in q["ci_jobs"],
         "Não bloqueia o pipeline" if q["ci_jobs"].get("SCA", {}).get("allow_failure") else ""),
        ("Sem relatórios gerados versionados", not q["committed_reports"],
         ", ".join(f"`{f}`" for f in q["committed_reports"]) + " no repositório" if q["committed_reports"] else ""),
    ]
    out.append(table(["", "Prática", "Observação"],
                     [[yes(bool(flag)), name, note] for name, flag, note in checks], "lll"))
    out.append("\n## Limitações\n")
    out.append("- **Diversidade de organizações** (*Elephant Factor*, CHAOSS) não é calculada: quase todos os "
               "commits usam e-mails pessoais, que não indicam a instituição.\n"
               "- **Revisão de código** é estimada pelo número de comentários do MR, que inclui comentários do "
               "próprio autor. Aprovações não estão disponíveis sem autenticação.\n"
               "- **Issues confidenciais** não aparecem na API pública.\n"
               "- **Cobertura de testes** não é publicada pelo CI. A razão entre arquivos de teste e de código é só "
               "um indicativo.\n")
    return "\n".join(out) + "\n"


# --------------------------------------------------------------------------- main

def to_jsonable(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, (set, tuple)):
        return list(obj)
    if isinstance(obj, Counter):
        return dict(obj)
    raise TypeError(type(obj))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", default=str(ROOT / "docs" / "estatisticas"))
    parser.add_argument("--cache", default=str(ROOT / ".cache" / "estatisticas"))
    parser.add_argument("--token", default=None, help="token do GitLab (ou variável GITLAB_TOKEN)")
    args = parser.parse_args()

    import os
    http = Http(args.token or os.environ.get("GITLAB_TOKEN"))
    now = datetime.now(timezone.utc).replace(microsecond=0)
    since = now - timedelta(days=365)
    base = project_api_path(PROJECT_PATH)

    print("git: sincronizando repositório…", file=sys.stderr)
    g = collect_git(sync_repo(Path(args.cache)), since)
    resolve_identities(g["commits"])

    print("GitLab: projeto, MRs, issues, pipelines e tags…", file=sys.stderr)
    project, _ = http.get(f"{API}{base}")
    languages, _ = http.get(f"{API}{base}/languages")
    mrs = http.paginate(f"{base}/merge_requests", {"state": "all", "scope": "all"})
    issues = http.paginate(f"{base}/issues", {"state": "all", "scope": "all"})
    pipelines = http.paginate(f"{base}/pipelines", {"updated_after": since.isoformat()})
    tags = http.paginate(f"{base}/repository/tags", {})
    print("GitLab: componentes…", file=sys.stderr)
    ecosystem = ecosystem_metrics(http, since)

    data = {
        "project": {k: project.get(k) for k in ("star_count", "forks_count", "default_branch", "created_at")},
        "languages": languages,
        "commits": commit_metrics(g, now, since),
        "contributors": contributor_metrics(g["commits"], now, since),
        "mrs": mr_metrics(mrs, now, since),
        "issues": issue_metrics(issues, now, since),
        "pipelines": pipeline_metrics(pipelines),
        "tags": tag_metrics(tags, since),
        "quality": quality_checks(g, now, http),
        "ecosystem": ecosystem,
    }
    meta = {"now": now, "generated": now.isoformat(), "generated_date": fmt_date(now), "since_date": fmt_date(since)}

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    pages = {
        "index.md": render_index(data, meta),
        "commits.md": render_commits(data, meta),
        "merge-requests.md": render_mrs(data, meta),
        "contribuicoes.md": render_contrib(data, meta),
        "qualidade.md": render_quality(data, meta),
    }
    for name, content in pages.items():
        (out / name).write_text(content, encoding="utf-8")
    exported = {**data, "generated": meta["generated"]}
    exported["commits"] = {k: v for k, v in data["commits"].items()}
    (out / "dados.json").write_text(json.dumps(exported, default=to_jsonable, ensure_ascii=False, indent=2),
                                    encoding="utf-8")
    print(f"Páginas geradas em {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
