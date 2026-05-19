# dbt (Data Build Tool)

Transformação de dados da camada Bronze (MinIO) para Silver e Gold (PostgreSQL).

## Visão Geral

O dbt é responsável por:

1. Ler dados brutos do Bronze (via external sources)
2. Limpar e normalizar → Silver
3. Agregar e calcular métricas → Gold
4. Testar qualidade em cada camada

## Estrutura de Models

```
dbt/
├── models/
│   ├── staging/           # Sources e staging
│   │   ├── stg_transferegov.sql
│   │   ├── stg_siape.sql
│   │   ├── stg_siafi.sql
│   │   ├── stg_comprasgov.sql
│   │   └── stg_siorg.sql
│   ├── silver/            # Dados limpos
│   │   ├── transferencias.sql
│   │   ├── servidores.sql
│   │   ├── execucao_financeira.sql
│   │   ├── contratos.sql
│   │   └── orgaos.sql
│   ├── gold/              # Métricas e fatos
│   │   ├── fato_transferencias.sql
│   │   ├── fato_servidores.sql
│   │   ├── fato_compras.sql
│   │   ├── dim_orgaos.sql
│   │   └── dim_tempo.sql
│   └── schema.yml         # Tests e documentação
├── seeds/                 # Dados estáticos
│   └── orgaos_referencia.csv
├── macros/                # Funções reutilizáveis
├── dbt_project.yml
└── profiles.yml
```

## Materializations

| Camada | Materialization | Motivo |
|--------|----------------|--------|
| Staging | `view` | Leve, apenas transformação |
| Silver | `table` | Performance em queries downstream |
| Gold | `table` ou `incremental` | Performance + eficiência |

## Exemplo de Model

### Silver

```sql
-- models/silver/transferencias.sql

{{ config(materialized='table', schema='silver') }}

SELECT
    id,
    TRIM(nome_programa) AS nome_programa,
    CAST(valor AS NUMERIC(15,2)) AS valor,
    CAST(data_celebracao AS DATE) AS data_celebracao,
    orgao_concedente,
    orgao_convenente,
    situacao,
    NOW() AS loaded_at
FROM {{ ref('stg_transferegov') }}
WHERE id IS NOT NULL
  AND valor > 0
```

### Gold

```sql
-- models/gold/fato_transferencias.sql

{{ config(materialized='table', schema='gold') }}

SELECT
    d.orgao_concedente,
    DATE_TRUNC('month', t.data_celebracao) AS mes,
    COUNT(*) AS total_transferencias,
    SUM(t.valor) AS valor_total,
    AVG(t.valor) AS valor_medio
FROM {{ ref('transferencias') }} t
LEFT JOIN {{ ref('dim_orgaos') }} d ON t.orgao_concedente = d.codigo
GROUP BY 1, 2
```

## Testes

### Schema Tests (schema.yml)

```yaml
models:
  - name: transferencias
    columns:
      - name: id
        tests:
          - not_null
          - unique
      - name: valor
        tests:
          - not_null
      - name: data_celebracao
        tests:
          - not_null

  - name: fato_transferencias
    columns:
      - name: orgao_concedente
        tests:
          - relationships:
              to: ref('dim_orgaos')
              field: codigo
```

### Custom Tests

```sql
-- tests/assert_valor_positivo.sql
SELECT *
FROM {{ ref('transferencias') }}
WHERE valor <= 0
```

## Comandos

```bash
# Executar todos os models
dbt run

# Executar apenas Gold
dbt run --select gold.*

# Rodar testes
dbt test

# Gerar documentação
dbt docs generate
dbt docs serve

# Full refresh (recriar tabelas)
dbt run --full-refresh
```

## Configuração

### profiles.yml

```yaml
govhub:
  target: dev
  outputs:
    dev:
      type: postgres
      host: localhost
      port: 5432
      user: govhub
      password: "{{ env_var('POSTGRES_PASSWORD') }}"
      dbname: govhub
      schema: public
      threads: 4
```

### dbt_project.yml

```yaml
name: govhub
version: '1.0.0'

model-paths: ["models"]
seed-paths: ["seeds"]
test-paths: ["tests"]
macro-paths: ["macros"]

models:
  govhub:
    staging:
      +materialized: view
    silver:
      +materialized: table
      +schema: silver
    gold:
      +materialized: table
      +schema: gold
```
