# Fluxo de Dados

Pipeline completo do GovHub BR: desde a ingestão de sistemas governamentais até a visualização em dashboards.

## Visão Geral

```mermaid
graph LR
    subgraph "1. Ingestão"
        AF[Airflow DAGs]
    end

    subgraph "2. Bronze"
        MN[MinIO]
    end

    subgraph "3. Silver"
        S[dbt - Clean]
    end

    subgraph "4. Gold"
        G[dbt - Aggregate]
    end

    subgraph "5. Consumo"
        SS[Superset]
        JH[JupyterHub]
    end

    AF -->|Raw files| MN
    MN -->|dbt source| S
    S -->|Models| G
    G -->|PostgreSQL| SS
    G -->|PostgreSQL| JH
```

## Etapas Detalhadas

### Etapa 1: Ingestão (Airflow)

DAGs do Apache Airflow extraem dados de APIs e sistemas governamentais.

```mermaid
sequenceDiagram
    participant Scheduler as Airflow Scheduler
    participant DAG as DAG de Ingestão
    participant API as API Gov (ex: TransfereGov)
    participant MinIO as MinIO (Bronze)

    Scheduler->>DAG: Trigger (schedule)
    DAG->>API: Request dados
    API-->>DAG: Response (JSON/CSV)
    DAG->>MinIO: Upload raw file
    Note over MinIO: Bronze layer (raw, imutável)
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

dbt lê dados brutos do MinIO (via staging) e aplica limpeza e normalização.

```mermaid
sequenceDiagram
    participant MinIO as MinIO (Bronze)
    participant dbt as dbt
    participant PG as PostgreSQL (Silver)

    MinIO->>dbt: External source (raw)
    dbt->>dbt: Clean, deduplicate, normalize
    dbt->>PG: Materialized tables (silver schema)
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

### Etapa 4: Consumo (Superset / JupyterHub)

```mermaid
sequenceDiagram
    participant User as Usuário
    participant SS as Superset
    participant PG as PostgreSQL (Gold)

    User->>SS: Acessa dashboard
    SS->>PG: SQL query
    PG-->>SS: Resultados
    SS-->>User: Visualização interativa
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
