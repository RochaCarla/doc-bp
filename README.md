# Brasil Participativo — Documentação Técnica

Documentação técnica da plataforma [Brasil Participativo](https://brasilparticipativo.presidencia.gov.br/), a plataforma nacional de participação social digital do governo federal brasileiro.

## Sobre

O Brasil Participativo é construído como um **fork direto do [Decidim](https://decidim.org/)** (framework open source de democracia participativa em Ruby on Rails), desenvolvido e mantido pelo [LabLivre/UnB](https://lappis.rocks/).

Esta documentação é resultado do trabalho do LabLivre/UnB em um Termo de Execução Descentralizada (TED) com a Secretaria Nacional de Participação Social. Ela cobre:

- **Documentação**: visão geral, arquitetura, guia do desenvolvedor, guia de operação, banco de dados, módulos e componentes
- **Manual de Uso**: guias para gestores de processos participativos
- **Design System**: como o padrão gov.br foi aplicado na plataforma
- **Inovação**: diferenças em relação ao Decidim, com foco em desempenho
- **Estatísticas**: commits, merge requests, contribuições e indicadores de qualidade de software livre
- **Sobre**: origem e manutenção desta documentação

## Acesso

📖 **Site publicado**: [lablivre-unb.github.io/doc-bp](https://lablivre-unb.github.io/doc-bp/)

## Repositórios Relacionados

| Repositório | Descrição |
|-------------|-----------|
| [decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) | Core da plataforma (fork do Decidim) |
| [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo) | Componentes customizados (gems Ruby) |

## Desenvolvimento Local

### Com Docker (recomendado)

```bash
docker compose up
```

Acesse em [http://localhost:8000/doc-bp/](http://localhost:8000/doc-bp/). As alterações em `docs/` recarregam a página automaticamente.

Build estático, com a mesma verificação do CI:

```bash
docker compose run --rm docs build --strict
```

E-book em PDF (capa, folha de rosto, sumário, conteúdo completo e contracapa), em `dist/`:

```bash
./scripts/pdf.sh
```

No deploy, o PDF é gerado pelo CI e publicado em `documentacao-brasil-participativo.pdf`, na raiz do site.

### Sem Docker

```bash
pip install "mkdocs>=1.6,<2" "mkdocs-material==9.7.7" "mkdocs-print-site-plugin==2.9"
mkdocs serve
```

> As versões ficam fixas no `docker-compose.yml` e no workflow de deploy. O MkDocs 2.0 não é compatível com o tema e os overrides usados aqui.

### Páginas geradas

Algumas seções são geradas a partir do repositório `decidim-govbr` e da API pública do GitLab. Não edite essas páginas à mão; rode os scripts (Python 3.9+, só biblioteca padrão):

| Script | Gera |
|--------|------|
| `python3 scripts/estatisticas.py` | `docs/estatisticas/` (commits, MRs, contribuições, qualidade) |
| `python3 scripts/banco_de_dados.py` | `docs/banco-de-dados/` (dicionário de dados), exceto `consultas.md` |
| `python3 scripts/sobrescritas.py` | `docs/transferencia/sobrescritas.md` (arquivos do Decidim sobrescritos) |
| `python3 scripts/glossario.py` | `docs/visao-geral/glossario.md`, a partir do `CONTEXT.md` |

Os scripts clonam o repositório em `.cache/` (ignorado pelo git). Defina `GITLAB_TOKEN` para aumentar o limite da API.

## Deploy

O deploy é feito automaticamente via **GitHub Actions** para o GitHub Pages ao fazer push na branch `main`.

## Stack da Documentação

- [MkDocs](https://www.mkdocs.org/) — gerador de sites estáticos
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — tema com features avançadas
- [Mermaid](https://mermaid.js.org/) — diagramas como código
- [Design System gov.br](https://www.gov.br/ds/) — identidade visual (`docs/stylesheets/custom.css`, `overrides/`)

## Uso de IA

Esta documentação é produzida com apoio de IA generativa, sob responsabilidade da equipe. Veja a [declaração de uso de IA](docs/sobre/uso-de-ia.md), que traz também as regras para contribuições com IA.

## Licença

O conteúdo desta documentação (textos, diagramas e e-book) está licenciado sob a [Creative Commons Atribuição 4.0 Internacional (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/deed.pt-br); o texto legal está em [`LICENSE-CONTEUDO.txt`](LICENSE-CONTEUDO.txt). Logos e marcas institucionais não estão incluídos.

O código deste repositório (geradores em `scripts/`, tema e templates) está sob a [GNU Affero General Public License v3 (AGPLv3)](LICENSE), a mesma do Brasil Participativo.

Documentação mantida pelo LabLivre/UnB.
