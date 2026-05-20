# Fluxo de Dados

Pipeline completo do GovHub BR: desde a ingestão de sistemas governamentais até a visualização em dashboards.

## Visão Geral

```mermaid
graph LR
    subgraph "1. Extract"
        AF[Airflow DAGs]
    end

    subgraph "2. Bronze"
        MN[MinIO]
    end

    subgraph "3. Load"
        PG_STG[(PG staging)]
    end

    subgraph "4. Transform"
        DBT[dbt Silver/Gold]
    end

    subgraph "5. Consumo"
        SS[Superset]
        TR[Trino + Ranger]
        JH[JupyterHub]
    end

    AF -->|"raw files"| MN
    AF -->|"load"| PG_STG
    PG_STG --> DBT
    DBT -->|"silver/gold"| SS
    DBT -->|"dados sensíveis"| TR
    TR --> JH
```

## Etapas Detalhadas

### Etapa 1: Extract + Load (Airflow)

DAGs do Apache Airflow executam 3 tasks sequenciais:

```mermaid
sequenceDiagram
    participant Scheduler as Airflow Scheduler
    participant DAG as DAG de Ingestão
    participant API as API Gov (ex: TransfereGov)
    participant MinIO as MinIO (Bronze)
    participant PG as PostgreSQL (staging)
    participant dbt as dbt

    Scheduler->>DAG: Trigger (schedule)
    DAG->>API: 1. Extract: request dados
    API-->>DAG: Response (JSON/CSV)
    DAG->>MinIO: Upload raw file
    Note over MinIO: Bronze layer (raw, imutável)
    DAG->>PG: 2. Load: MinIO → staging tables
    DAG->>dbt: 3. Trigger dbt run
```

**Fontes**:

| Sistema | Método | Formato |
|---------|--------|---------|
| TransfereGov | API REST | JSON |
| Siape | Certificado digital | CSV |
| Siafi | API + certificado | JSON |
| ComprasGov | API REST | JSON |
| Siorg | API REST | JSON |

### Etapa 2: Bronze → Silver (dbt)

dbt lê dados das staging tables no PostgreSQL (carregadas pelo Airflow a partir do MinIO) e aplica limpeza e normalização.

```mermaid
sequenceDiagram
    participant PG_STG as PostgreSQL (staging)
    participant dbt as dbt
    participant PG_S as PostgreSQL (Silver)

    PG_STG->>dbt: Read staging tables
    dbt->>dbt: Clean, deduplicate, normalize
    dbt->>PG_S: Materialized tables (silver schema)
    dbt->>dbt: Run tests (not_null, unique, etc.)
```

**Transformações típicas**:

- Remoção de duplicatas
- Normalização de tipos (datas, moedas)
- Padronização de nomes de órgãos
- Validação de integridade referencial

### Etapa 3: Silver → Gold (dbt)

dbt agrega e enriquece dados para consumo direto.

```mermaid
sequenceDiagram
    participant PG_S as PostgreSQL (Silver)
    participant dbt as dbt
    participant PG_G as PostgreSQL (Gold)

    PG_S->>dbt: Read silver tables
    dbt->>dbt: Aggregate, calculate metrics
    dbt->>PG_G: Materialized tables (gold schema)
```

**Exemplos de modelos Gold**:

- `fato_transferencias` — Transferências por órgão/período
- `fato_servidores` — Indicadores de pessoal
- `fato_compras` — Métricas de compras públicas
- `dim_orgaos` — Dimensão consolidada de órgãos

### Etapa 4: Consumo (Superset / Trino / JupyterHub)

```mermaid
sequenceDiagram
    participant User as Usuário
    participant SS as Superset
    participant TR as Trino + Ranger
    participant JH as JupyterHub
    participant PG as PostgreSQL (Gold)

    User->>SS: Acessa dashboard (dados públicos)
    SS->>PG: SQL query direto
    PG-->>SS: Resultados
    SS-->>User: Visualização interativa

    User->>JH: Análise de dados sensíveis
    JH->>TR: Query via Trino
    TR->>PG: SQL com row-level security
    PG-->>TR: Resultados filtrados
    TR-->>JH: Dados governados
```

## Schedule de Execução

| DAG | Frequência | Fontes |
|-----|-----------|--------|
| `ingestao_transferegov` | Diária | TransfereGov API |
| `ingestao_siape` | Semanal | Siape (certificado) |
| `ingestao_siafi` | Diária | Siafi API |
| `ingestao_comprasgov` | Diária | ComprasGov API |
| `ingestao_siorg` | Semanal | Siorg API |
| `dbt_run` | Diária (pós-ingestão) | — |
| `dbt_test` | Diária (pós-dbt_run) | — |

## Qualidade de Dados

Garantida em múltiplas camadas:

| Camada | Mecanismo |
|--------|-----------|
| Ingestão | Retries, idempotência, logging |
| Silver | dbt tests: `not_null`, `unique`, `accepted_values` |
| Gold | dbt tests: `relationships`, custom SQL tests |
| Governança | OpenMetadata: linhagem, freshness, ownership |
