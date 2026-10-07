#!/usr/bin/env python3
"""Gera o inventário de sobrescritas do Decidim no decidim-govbr.

Compara cada arquivo de app/, lib/ e config/ do core (branch main) com o arquivo de mesmo caminho
nas gems do Decidim 0.27.2. Quando o caminho existe numa gem, o arquivo do core a sobrescreve.
Mede a diferença em linhas para estimar o esforço de atualização do Decidim.

Uso:
  python3 scripts/sobrescritas.py      # gera docs/transferencia/sobrescritas.md
"""

from __future__ import annotations

import difflib
import io
import subprocess
import sys
import tarfile
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from estatisticas import ROOT, sync_repo  # noqa: E402

DECIDIM_TAG = "v0.27.2"
UPSTREAM_URL = "https://github.com/decidim/decidim.git"
CORE_URL = "https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main"
SCOPES = ("app/", "lib/", "config/initializers/")


def core_files(repo: Path) -> dict[str, list[str]]:
    data = subprocess.run(["git", "-C", str(repo), "archive", "main", *[s.rstrip("/") for s in SCOPES]],
                          check=True, capture_output=True).stdout
    files = {}
    with tarfile.open(fileobj=io.BytesIO(data)) as tar:
        for member in tar.getmembers():
            if member.isfile():
                raw = tar.extractfile(member).read()
                files[member.name] = raw.decode("utf-8", errors="replace").splitlines()
    return files


def upstream_dir(cache: Path) -> Path:
    path = cache / f"decidim-{DECIDIM_TAG}"
    if not path.exists():
        subprocess.run(["git", "clone", "--quiet", "--depth", "1", "--branch", DECIDIM_TAG, UPSTREAM_URL, str(path)],
                       check=True)
    return path


def main() -> int:
    cache = ROOT / ".cache" / "estatisticas"
    repo = sync_repo(cache)
    upstream = upstream_dir(ROOT / ".cache")
    gems = sorted(p for p in upstream.iterdir() if p.is_dir() and p.name.startswith("decidim-"))

    files = core_files(repo)
    overrides = []
    own = defaultdict(int)
    for path, lines in sorted(files.items()):
        match = next((g for g in gems if (g / path).is_file()), None)
        if not match:
            own[path.split("/")[1] if path.startswith("app/") else path.split("/")[0]] += 1
            continue
        original = (match / path).read_text(encoding="utf-8", errors="replace").splitlines()
        diff = list(difflib.unified_diff(original, lines, lineterm="", n=0))
        added = sum(1 for d in diff if d.startswith("+") and not d.startswith("+++"))
        removed = sum(1 for d in diff if d.startswith("-") and not d.startswith("---"))
        overrides.append({"path": path, "gem": match.name, "added": added, "removed": removed,
                          "core_lines": len(lines), "upstream_lines": len(original)})

    by_gem = defaultdict(list)
    for o in overrides:
        by_gem[o["gem"]].append(o)
    identical = [o for o in overrides if o["added"] == 0 and o["removed"] == 0]
    total_changed = sum(o["added"] + o["removed"] for o in overrides)

    def kind(path: str) -> str:
        parts = path.split("/")
        return parts[1] if parts[0] == "app" and len(parts) > 2 else parts[0] + ("/" + parts[1] if len(parts) > 2 else "")

    now = datetime.now(timezone.utc)
    out = [
        "---\ntitle: Inventário de sobrescritas\n---\n",
        f"<!-- Gerado por scripts/sobrescritas.py em {now.isoformat(timespec='seconds')}. Não edite à mão. -->\n",
        "# Inventário de sobrescritas\n",
        f"Arquivos do `decidim-govbr` (branch `main`) que **substituem** arquivos do Decidim {DECIDIM_TAG[1:]}. "
        "O Rails carrega a versão do core no lugar da versão da gem, então cada um deles precisa ser revisado ao "
        "atualizar o Decidim. Veja o [Plano de atualização tecnológica](atualizacao.md).\n",
        f'!!! info "Gerado em {now.strftime("%d/%m/%Y")}"\n'
        f"    Comparação de `{'`, `'.join(SCOPES)}` com as gems do Decidim na tag `{DECIDIM_TAG}`. "
        "Para atualizar, rode `python3 scripts/sobrescritas.py`.\n",
        "## Resumo\n",
        "| Item | Quantidade |\n|---|---:|",
        f"| Arquivos sobrescritos | {len(overrides)} |",
        f"| Linhas diferentes do original (adicionadas + removidas) | {total_changed:,} |".replace(",", "."),
        f"| Sobrescritas idênticas ao original (podem ser removidas) | {len(identical)} |",
        f"| Arquivos próprios, sem equivalente no Decidim | {sum(own.values())} |",
        "\n## Por gem do Decidim\n",
        "Quanto mais linhas diferentes, maior o esforço de atualização.\n",
        "| Gem | Arquivos sobrescritos | Linhas diferentes |\n|---|---:|---:|",
    ]
    for gem, items in sorted(by_gem.items(), key=lambda x: -sum(o["added"] + o["removed"] for o in x[1])):
        out.append(f"| `{gem}` | {len(items)} | {sum(o['added'] + o['removed'] for o in items):,} |".replace(",", "."))

    by_kind = defaultdict(lambda: [0, 0])
    for o in overrides:
        by_kind[kind(o["path"])][0] += 1
        by_kind[kind(o["path"])][1] += o["added"] + o["removed"]
    out.append("\n## Por tipo de arquivo\n")
    out.append("| Tipo | Arquivos | Linhas diferentes |\n|---|---:|---:|")
    for k, (n, c) in sorted(by_kind.items(), key=lambda x: -x[1][1]):
        out.append(f"| `{k}` | {n} | {c:,} |".replace(",", "."))

    out.append("\n## As 40 sobrescritas mais alteradas\n")
    out.append("| Arquivo | Gem | + | − | Linhas no core |\n|---|---|---:|---:|---:|")
    for o in sorted(overrides, key=lambda o: -(o["added"] + o["removed"]))[:40]:
        out.append(f"| [`{o['path']}`]({CORE_URL}/{o['path']}) | `{o['gem']}` | {o['added']} | {o['removed']} | {o['core_lines']} |")

    if identical:
        out.append("\n## Sobrescritas idênticas ao original\n")
        out.append("Estes arquivos são iguais aos do Decidim 0.27.2. Podem ser removidos do core sem mudar o "
                   "comportamento, o que reduz o trabalho de atualização.\n")
        out += [f"- `{o['path']}` (`{o['gem']}`)" for o in identical]

    out.append("\n## Lista completa por gem\n")
    for gem, items in sorted(by_gem.items()):
        out.append(f'??? note "`{gem}` — {len(items)} arquivos"\n')
        out.append("    | Arquivo | + | − |\n    |---|---:|---:|")
        out += [f"    | `{o['path']}` | {o['added']} | {o['removed']} |" for o in sorted(items, key=lambda o: o["path"])]
        out.append("")

    out.append("## Arquivos próprios\n")
    out.append("Arquivos sem equivalente no Decidim (código exclusivo do Brasil Participativo), por pasta:\n")
    out.append("| Pasta | Arquivos |\n|---|---:|")
    out += [f"| `{k}` | {v} |" for k, v in sorted(own.items(), key=lambda x: -x[1])]

    dest = ROOT / "docs" / "transferencia" / "sobrescritas.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"{len(overrides)} sobrescritas, {len(identical)} idênticas, {total_changed} linhas diferentes → {dest}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
