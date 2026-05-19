# Guia: Criar um Novo Fork Temático

Passo a passo para criar uma nova instância do pipeline GovHub para um contexto específico.

## Quando criar um fork?

Crie um fork quando:

- Há um **novo domínio de dados** (outro ministério, estado, autarquia)
- As **fontes de dados** são diferentes do pipeline federal
- Os **dashboards** precisam ser específicos para o contexto
- A **equipe** é dedicada a este contexto

## Passo a Passo

### 1. Fork no GitHub

1. Acesse [`data-application-gov-hub`](https://github.com/GovHub-br/data-application-gov-hub)
2. Clique em **Fork**
3. Nomeie: `data-application-<contexto>` (ex: `data-application-saude`, `data-application-educacao`)
4. Mantenha na organização `GovHub-br` (ou sua própria)

### 2. Clonar e configurar

```bash
git clone git@github.com:GovHub-br/data-application-<contexto>.git
cd data-application-<contexto>

# Adicionar upstream para sincronização futura
git remote add upstream git@github.com:GovHub-br/data-application-gov-hub.git
```

### 3. Criar DAGs de ingestão

Crie novas DAGs em `airflow/dags/` para suas fontes:

```python
# airflow/dags/ingestao_<sua_fonte>.py

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "govhub",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ingestao_<sua_fonte>",
    default_args=default_args,
    schedule_interval="0 6 * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["ingestao", "<contexto>"],
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data,
    )

    upload = PythonOperator(
        task_id="upload_to_minio",
        python_callable=upload_raw_to_minio,
    )

    extract >> upload
```

### 4. Criar models dbt

Siga a arquitetura Medallion:

```
dbt/models/
├── staging/
│   └── stg_<sua_fonte>.sql        # Source → staging
├── silver/
│   └── <entidade_limpa>.sql       # Staging → clean
└── gold/
    ├── fato_<metrica>.sql         # Silver → fato
    └── dim_<dimensao>.sql         # Silver → dimensão
```

**Exemplo staging**:

```sql
-- dbt/models/staging/stg_minha_fonte.sql
{{ config(materialized='view') }}

SELECT *
FROM {{ source('bronze', 'minha_fonte_raw') }}
```

**Exemplo silver**:

```sql
-- dbt/models/silver/minha_entidade.sql
{{ config(materialized='table', schema='silver') }}

SELECT
    id,
    TRIM(nome) AS nome,
    CAST(valor AS NUMERIC(15,2)) AS valor,
    NOW() AS loaded_at
FROM {{ ref('stg_minha_fonte') }}
WHERE id IS NOT NULL
```

**Exemplo gold**:

```sql
-- dbt/models/gold/fato_minha_metrica.sql
{{ config(materialized='table', schema='gold') }}

SELECT
    dimensao,
    DATE_TRUNC('month', data) AS mes,
    COUNT(*) AS total,
    SUM(valor) AS valor_total
FROM {{ ref('minha_entidade') }}
GROUP BY 1, 2
```

### 5. Adicionar testes dbt

```yaml
# dbt/models/schema.yml
models:
  - name: minha_entidade
    columns:
      - name: id
        tests:
          - not_null
          - unique
```

### 6. Criar dashboards

1. Subir ambiente local: `docker-compose up -d`
2. Acessar Superset: http://localhost:8088
3. Criar datasets apontando para Gold layer
4. Criar charts e dashboards
5. Exportar dashboards para `superset/dashboards/`

### 7. Documentar

Adicione um README no repositório com:

- Descrição do contexto
- Fontes de dados integradas
- Como rodar localmente
- Dashboards disponíveis

## Manter Sincronizado

Periodicamente, incorporar melhorias do pipeline base:

```bash
git fetch upstream
git merge upstream/main

# Resolver conflitos se houver
# Testar: make test
# Comitar
```

## Boas Práticas

- **Mantenha a estrutura Medallion** (Bronze/Silver/Gold)
- **Reutilize macros** do repo base quando possível
- **Contribua de volta** melhorias genéricas via PR upstream
- **Documente fontes** de dados com schema.yml do dbt
- **Testes obrigatórios** para toda tabela Silver/Gold
- **Nomeie consistentemente**: `ingestao_<fonte>`, `silver.<entidade>`, `gold.fato_<metrica>`
