# Brasil Participativo — Documentação Técnica

Documentação técnica da plataforma [Brasil Participativo](https://brasilparticipativo.presidencia.gov.br/), a plataforma nacional de participação social digital do governo federal brasileiro.

## Sobre

O Brasil Participativo é construído como um **fork direto do [Decidim](https://decidim.org/)** (framework open source de democracia participativa em Ruby on Rails), desenvolvido e mantido pelo [LAPPIS/UnB](https://lappis.rocks/).

Esta documentação cobre:

- **Visão Geral** — arquitetura, relação com o Decidim, repositórios
- **Guia do Desenvolvedor** — setup local, estrutura do código, contribuição, criação de componentes
- **Guia do Operador** — deploy em Kubernetes, configuração, administração
- **Módulos Decidim** — 9 módulos nativos ativos (propostas, reuniões, formulários, etc.)
- **Componentes Customizados** — 8 gems desenvolvidas pelo LAPPIS/UnB

## Acesso

📖 **Site publicado**: [rochacarla.github.io/doc-bp](https://rochacarla.github.io/doc-bp/)

## Repositórios Relacionados

| Repositório | Descrição |
|-------------|-----------|
| [decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) | Core da plataforma (fork do Decidim) |
| [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo) | Componentes customizados (gems Ruby) |

## Desenvolvimento Local

### Pré-requisitos

- Python 3.11+
- pip

### Instalação

```bash
pip install mkdocs mkdocs-material
```

### Servidor de desenvolvimento

```bash
mkdocs serve
```

Acesse em [http://localhost:8000/doc-bp/](http://localhost:8000/doc-bp/).

### Build

```bash
mkdocs build
```

## Deploy

O deploy é feito automaticamente via **GitHub Actions** para o GitHub Pages ao fazer push na branch `main`.

## Stack da Documentação

- [MkDocs](https://www.mkdocs.org/) — gerador de sites estáticos
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) — tema com features avançadas
- [Mermaid](https://mermaid.js.org/) — diagramas como código

## Licença

Este projeto de documentação é mantido pelo LAPPIS/UnB.
