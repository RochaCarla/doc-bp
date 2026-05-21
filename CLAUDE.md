# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Documentation site for **Brasil Participativo** — national participatory democracy platform of the Brazilian federal government, built as a direct fork of Decidim. Focus is on the core (`decidim-govbr`), with custom components documented as peripheral. Two target audiences: external developers (contributing, local setup) and government operators (deploy, configuration, administration).

- **Core repo**: [gitlab.com/lappis-unb/decidimbr/decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr)
- **Components repo**: [gitlab.com/lappis-unb/decidimbr/components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo)

## Build & Development Commands

```bash
# Install dependencies
poetry install

# Local dev server (hot-reload)
poetry run mkdocs serve

# Build static site
poetry run mkdocs build
```

No tests or linter configured in this repo. CI runs `poetry run mkdocs build` on push/PR to main and deploys to GitHub Pages on merge.

## Architecture

- **Build tool**: MkDocs with Material theme, managed via Poetry (Python 3.11+)
- **Config**: `mkdocs.yml` — defines nav structure, theme, plugins, markdown extensions
- **Content**: all docs live under `docs/` as Markdown files
- **Output**: built to `site/` (gitignored)
- **Deploy**: GitHub Actions → GitHub Pages (automatic on main)

### MkDocs Plugins & Extensions

- **Mermaid diagrams**: use ` ```mermaid ` fenced blocks
- **Admonition**: `!!! note`, `!!! warning`, etc.
- **Tabbed content**: `pymdownx.tabbed` with alternate style
- **Search**: configured for Portuguese (`lang: pt`)

## Conventions

- **Language**: all content is in Brazilian Portuguese (pt-BR)
- **Commit messages**: Conventional Commits (`feat:`, `fix:`, `docs:`, `chore:`, etc.)
- **Navigation**: any new page must be added to the `nav:` section in `mkdocs.yml`
- **Diagrams**: prefer Mermaid over static images for architecture/flow diagrams
