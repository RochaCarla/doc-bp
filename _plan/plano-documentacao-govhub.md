# Plano de Documentação — GovHub BR

## Sobre o Projeto

**GovHub BR** é uma iniciativa open source para integrar, qualificar e disponibilizar dados governamentais de forma estruturada, promovendo eficiência administrativa, transparência e melhor tomada de decisão.

**Organização**: https://github.com/GovHub-br
**Site**: https://gov-hub.io
**Apoio**: Lab Livre (UnB) + IPEA/Dides

### Fontes de Dados

Sistemas estruturantes do governo federal:

- **TransfereGov** — Transferências voluntárias
- **Siape** — Pessoal civil e militar
- **Siafi** — Administração financeira
- **ComprasGov** — Compras públicas
- **Siorg** — Estrutura organizacional

---

## Arquitetura Atual

```mermaid
graph TB
    subgraph "Fontes"
        TG[TransfereGov]
        SI[Siape]
        SF[Siafi]
        CG[ComprasGov]
        SO[Siorg]
    end

    subgraph "Ingestão & Orquestração"
        AF[Apache Airflow]
    end

    subgraph "Armazenamento"
        MN[MinIO - Object Storage]
        PG[(PostgreSQL - Metastore)]
    end

    subgraph "Transformação"
        DBT[dbt - Models]
    end

    subgraph "Visualização & Análise"
        SS[Apache Superset]
        JH[JupyterHub]
    end

    subgraph "Governança"
        OM[OpenMetadata]
    end

    TG --> AF
    SI --> AF
    SF --> AF
    CG --> AF
    SO --> AF
    AF --> MN
    AF --> PG
    MN --> DBT
    PG --> DBT
    DBT --> PG
    PG --> SS
    PG --> JH
    PG --> OM
```

### Arquitetura Medallion

| Camada | Descrição | Storage |
|--------|-----------|---------|
| **Bronze** | Dados brutos ingeridos (raw) | MinIO |
| **Silver** | Dados limpos e normalizados | PostgreSQL |
| **Gold** | Dados agregados e prontos para consumo | PostgreSQL |

### Stack Principal

| Componente | Tecnologia | Papel |
|------------|-----------|-------|
| Orquestração | Apache Airflow | ETL/ELT pipelines |
| Transformação | dbt | Data models e testes |
| Object Storage | MinIO | Armazenamento de dados brutos |
| Banco Analítico | PostgreSQL | Metastore e analytics |
| BI / Dashboards | Apache Superset | Visualização e exploração |
| Notebooks | JupyterHub | Análise interativa |
| Governança | OpenMetadata | Catálogo e linhagem de dados |
| Deploy | Argo CD (GitOps) | Kubernetes declarativo |
| Container | Docker / Kubernetes | Execução dos serviços |

---

## Repositórios

| Repositório | Descrição | Stack |
|-------------|-----------|-------|
| [`data-application-gov-hub`](https://github.com/GovHub-br/data-application-gov-hub) | Pipeline de dados principal | Airflow, dbt, Jupyter, Superset |
| [`gov-hub`](https://github.com/GovHub-br/gov-hub) | Site institucional e documentação | HTML |
| [`continuous-deployment`](https://github.com/GovHub-br/continuous-deployment) | Infra GitOps (K8s, Helm, Argo CD) | Python, YAML |
| [`data-application-cidades`](https://github.com/GovHub-br/data-application-cidades) | Fork — dados municipais | Airflow, dbt |
| [`data-application-minc`](https://github.com/GovHub-br/data-application-minc) | Fork — Ministério da Cultura | Airflow, dbt |
| [`govhub-research`](https://github.com/GovHub-br/govhub-research) | Pesquisa: IA, OCR, parsers | Python |
| [`openmetadata-declarative-governance`](https://github.com/GovHub-br/openmetadata-declarative-governance) | Governança declarativa | Python |
| [`data-governance-workshop`](https://github.com/GovHub-br/data-governance-workshop) | Workshop Ranger + Trino | HTML |

---

## Documentação a Criar

### Fase 1 — Arquitetura (Prioridade Alta)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/index.md` | Home: missão, diagrama geral, links rápidos |
| `docs/arquitetura/visao-geral.md` | Medallion, stack, repositórios, decisões |
| `docs/arquitetura/fluxo-de-dados.md` | Pipeline: ingestão → bronze → silver → gold → BI |
| `docs/arquitetura/medallion.md` | Detalhamento das camadas Bronze/Silver/Gold |
| `docs/arquitetura/componentes.md` | Airflow, dbt, MinIO, PostgreSQL, Superset, JupyterHub |

### Fase 2 — Pipeline de Dados (Prioridade Alta)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/pipeline/airflow.md` | DAGs, plugins, conexões, schedules |
| `docs/pipeline/dbt.md` | Models, seeds, tests, materializations |
| `docs/pipeline/ingestao.md` | Fontes (TransfereGov, Siape, etc.), conectores |
| `docs/pipeline/qualidade.md` | Testes dbt, validações, monitoramento |

### Fase 3 — Infraestrutura (Prioridade Alta)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/infraestrutura/kubernetes.md` | Cluster K8s, namespaces, recursos |
| `docs/infraestrutura/argocd.md` | GitOps, app-of-apps, sync waves, overlays |
| `docs/infraestrutura/minio.md` | Object storage, buckets, políticas |
| `docs/infraestrutura/postgres.md` | Metastore, schemas, backups |
| `docs/infraestrutura/secrets.md` | Gestão de segredos, certificados (SIAFI/SIAPE) |

### Fase 4 — Visualização & Governança (Prioridade Média)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/visualizacao/superset.md` | Dashboards, datasets, permissões |
| `docs/visualizacao/jupyterhub.md` | Notebooks, kernels, acesso |
| `docs/governanca/openmetadata.md` | Catálogo, linhagem, domínios, owners |
| `docs/governanca/acesso.md` | Políticas de acesso (Ranger/Trino se aplicável) |

### Fase 5 — Onboarding (Prioridade Média)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/onboarding/roteiro.md` | Roteiro geral para novos contribuidores |
| `docs/onboarding/setup-local.md` | Docker Compose, Make, primeiros passos |
| `docs/onboarding/git-workflow.md` | Branches, commits assinados, GPG, PRs |
| `docs/onboarding/airflow-tutorial.md` | Primeira DAG, conexões, testes |
| `docs/onboarding/dbt-tutorial.md` | Primeiro model, run, test |
| `docs/onboarding/superset-tutorial.md` | Primeiro dashboard |
| `docs/onboarding/troubleshooting.md` | Problemas comuns |

### Fase 6 — Forks Temáticos (Prioridade Alta)

| Arquivo | Conteúdo |
|---------|----------|
| `docs/forks/index.md` | Visão geral: conceito, stack, diagrama, forks ativos |
| `docs/forks/cidades.md` | Fork Cidades: fontes (IBGE, SICONV, FNDE, DataSUS), medallion, dashboards |
| `docs/forks/minc.md` | Fork MinC: fontes (SALIC, MapaCultural, SNIIC, IPHAN), medallion, dashboards |
| `docs/forks/guia-criar-fork.md` | Guia completo para criar novo fork: DAGs, dbt, dashboards, sync |

### Fase 7 — Contribuição & Comunidade

| Arquivo | Conteúdo |
|---------|----------|
| `docs/CONTRIBUTING.md` | Guia de contribuição, padrões |
| `docs/comunidade/pesquisa.md` | govhub-research: POCs, IA, OCR |

---

## Navegação (`mkdocs.yml`)

```yaml
nav:
  - Home: index.md
  - Arquitetura:
    - Visão Geral: arquitetura/visao-geral.md
    - Fluxo de Dados: arquitetura/fluxo-de-dados.md
    - Arquitetura Medallion: arquitetura/medallion.md
    - Componentes: arquitetura/componentes.md
  - Pipeline de Dados:
    - Apache Airflow: pipeline/airflow.md
    - dbt: pipeline/dbt.md
    - Ingestão de Dados: pipeline/ingestao.md
    - Qualidade de Dados: pipeline/qualidade.md
  - Infraestrutura:
    - Kubernetes: infraestrutura/kubernetes.md
    - Argo CD (GitOps): infraestrutura/argocd.md
    - MinIO: infraestrutura/minio.md
    - PostgreSQL: infraestrutura/postgres.md
    - Secrets & Segurança: infraestrutura/secrets.md
  - Visualização:
    - Apache Superset: visualizacao/superset.md
    - JupyterHub: visualizacao/jupyterhub.md
  - Governança:
    - OpenMetadata: governanca/openmetadata.md
    - Controle de Acesso: governanca/acesso.md
  - Onboarding:
    - Roteiro: onboarding/roteiro.md
    - Setup Local: onboarding/setup-local.md
    - Git Workflow: onboarding/git-workflow.md
    - Tutorial Airflow: onboarding/airflow-tutorial.md
    - Tutorial dbt: onboarding/dbt-tutorial.md
    - Tutorial Superset: onboarding/superset-tutorial.md
    - Troubleshooting: onboarding/troubleshooting.md
  - Forks Temáticos:
    - Visão Geral: forks/index.md
    - Cidades: forks/cidades.md
    - Ministério da Cultura: forks/minc.md
    - Criar Novo Fork: forks/guia-criar-fork.md
  - Comunidade:
    - Contribuir: CONTRIBUTING.md
    - Pesquisa: comunidade/pesquisa.md
```

---

## Estrutura do Repositório `data-application-gov-hub`

```
.
├── airflow/
│   ├── dags/          # DAGs de ingestão e transformação
│   └── plugins/       # Plugins customizados
├── dbt/
│   └── models/        # Models bronze/silver/gold
├── jupyter/
│   └── notebooks/     # Análises exploratórias
├── superset/
│   └── dashboards/    # Dashboards exportados
├── docker-compose.yml
├── Makefile
└── README.md
```

## Estrutura do Repositório `continuous-deployment`

```
.
├── airflow/           # Manifests do Airflow (K8s)
├── app-of-apps/       # Chart que gera Applications filhos
├── argocd/            # Instalação Argo CD + entrypoints
├── jupyterhub/        # Manifests JupyterHub
├── minio/             # Manifests MinIO (+ overlay prod)
├── postgres/          # Manifests PostgreSQL
├── superset/          # Manifests Superset
└── README.md
```

---

## Identidade Visual (`mkdocs.yml`)

Alinhada com o site oficial [gov-hub.io](https://gov-hub.io) e o repositório [`gov-hub`](https://github.com/GovHub-br/gov-hub).

### Paleta de Cores

| Propriedade | Valor | Uso |
|-------------|-------|-----|
| `primary` | `purple` | Header, tabs, links, tabelas |
| `accent` | `purple` | Hover, elementos interativos |
| Dark mode | `scheme: slate` | Toggle automático (light/dark/system) |

CSS custom vars:

```css
--md-primary-fg-color: #7c3aed;
--md-primary-fg-color--light: #a78bfa;
--md-primary-fg-color--dark: #5b21b6;
--md-accent-fg-color: #8b5cf6;
```

### Tipografia

| Tipo | Fonte | Referência |
|------|-------|-----------|
| Texto | **Inter** | Google Fonts (400, 500, 600, 700, 800) |
| Código | **JetBrains Mono** | Built-in Material theme |

### Theme Toggle

Três modos com ícones Material:

| Modo | Ícone | `scheme` |
|------|-------|----------|
| System | `material/brightness-4` | Auto-detect |
| Light | `material/weather-night` | `default` |
| Dark | `material/weather-sunny` | `slate` |

### Features do Theme

```yaml
features:
  - content.code.copy          # Copiar blocos de código
  - content.code.annotate      # Anotações em código
  - content.tooltips           # Tooltips em abreviações
  - navigation.footer          # Links prev/next no footer
  - navigation.indexes         # Index pages para seções
  - navigation.sections        # Seções expandidas no sidebar
  - navigation.tabs            # Tabs no header
  - navigation.top             # Botão "back to top"
  - navigation.tracking        # URL tracking no scroll
  - search.highlight           # Highlight dos termos buscados
  - search.share               # Compartilhar busca
  - search.suggest             # Sugestões de busca
  - toc.follow                 # TOC segue o scroll
```

### Markdown Extensions

```yaml
extensions:
  - abbr                       # Abreviações com tooltip
  - admonition                 # Callouts (note, warning, tip)
  - attr_list                  # Atributos HTML em Markdown
  - def_list                   # Listas de definição
  - footnotes                  # Notas de rodapé
  - md_in_html                 # Markdown dentro de HTML
  - pymdownx.betterem          # Ênfase melhorada
  - pymdownx.caret             # Superscript (^text^)
  - pymdownx.details           # Admonitions colapsáveis
  - pymdownx.emoji             # Emojis twemoji
  - pymdownx.highlight         # Syntax highlighting
  - pymdownx.inlinehilite      # Highlight inline
  - pymdownx.keys              # Teclas (++ctrl+c++)
  - pymdownx.mark              # Texto marcado (==text==)
  - pymdownx.smartsymbols      # Símbolos tipográficos
  - pymdownx.superfences       # Fenced code + Mermaid
  - pymdownx.tabbed            # Tabs em conteúdo
  - pymdownx.tasklist          # Checklists
  - pymdownx.tilde             # Strikethrough (~~text~~)
```

### CSS Customizado

Arquivo: `docs/stylesheets/custom.css`

- Header com `--md-primary-fg-color--dark`
- Footer dark (`#1a1a2e`)
- Tabelas com `th` roxo e bordas arredondadas
- Admonitions com `border-radius: 8px`
- Links sem underline (hover underline)
- Font smoothing (antialiased)

### Extra

```yaml
extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/GovHub-br

extra_css:
  - https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap
  - stylesheets/custom.css

copyright: Lab Livre 2025
```

### Deploy

- **GitHub Action**: `.github/workflows/deploy-docs.yml`
- **Branch**: `main` → build → `gh-pages`
- **URL**: `https://rochacarla.github.io/doc-govhub/`
- **Build**: `docker run --rm -v .:/docs squidfunk/mkdocs-material build`

---

## Verificação Final

1. `docker run --rm -v .:/docs squidfunk/mkdocs-material build` — build sem erros
2. `docker run --rm -p 8000:8000 -v .:/docs squidfunk/mkdocs-material serve -a 0.0.0.0:8000` — preview local
3. Validar todos os links internos
4. Testar diagramas Mermaid
5. Verificar toggle dark/light/system
6. Confirmar paleta purple e fonte Inter
7. Verificar que não há referências ao projeto antigo (DestaquesGovbr, Cogfy, Bedrock, Typesense, HuggingFace)
8. Confirmar alinhamento com repos reais do GitHub
