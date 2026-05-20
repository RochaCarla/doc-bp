# Apache Airflow

Orquestração de pipelines de ingestão de dados governamentais.

## Visão Geral

O Airflow é responsável por:

1. Extrair dados de APIs/sistemas governamentais
2. Depositar dados brutos no MinIO (Bronze)
3. Triggerar transformações dbt após ingestão

## DAGs

### Estrutura

```
airflow/
├── dags/
│   ├── ingestao_transferegov.py
│   ├── ingestao_siape.py
│   ├── ingestao_siafi.py
│   ├── ingestao_comprasgov.py
│   ├── ingestao_siorg.py
│   └── dbt_transform.py
└── plugins/
    └── operators/
        └── minio_upload_operator.py
```

### Schedule

| DAG | Schedule | Descrição |
|-----|----------|-----------|
| `ingestao_transferegov` | `0 6 * * *` | Diária às 6h |
| `ingestao_siape` | `0 4 * * 1` | Semanal (segunda) |
| `ingestao_siafi` | `0 6 * * *` | Diária às 6h |
| `ingestao_comprasgov` | `0 7 * * *` | Diária às 7h |
| `ingestao_siorg` | `0 4 * * 1` | Semanal (segunda) |
| `dbt_transform` | Trigger (pós-ingestão) | Após sucesso das DAGs |

### Exemplo de DAG (3 passos)

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "govhub",
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ingestao_transferegov",
    default_args=default_args,
    schedule_interval="0 6 * * *",
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["ingestao", "transferegov"],
) as dag:

    # 1. Extract: API → MinIO (Bronze)
    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_transferegov_data,
    )

    # 2. Load: MinIO → PostgreSQL (staging tables)
    load = PythonOperator(
        task_id="load",
        python_callable=load_minio_to_postgres,
    )

    # 3. Trigger dbt: staging → Silver/Gold
    trigger_dbt = TriggerDagRunOperator(
        task_id="trigger_dbt",
        trigger_dag_id="dbt_transform",
        wait_for_completion=True,
    )

    extract >> load >> trigger_dbt
```

## Conexões

| Connection ID | Tipo | Destino |
|---------------|------|---------|
| `minio_default` | S3 | MinIO (object storage) |
| `postgres_default` | PostgreSQL | Banco analítico |
| `transferegov_api` | HTTP | API TransfereGov |
| `siape_cert` | HTTP + Cert | Siape (certificado) |
| `siafi_api` | HTTP + Cert | Siafi |
| `comprasgov_api` | HTTP | ComprasGov API |

## Monitoramento

- **Logs**: Acessíveis na UI do Airflow
- **Alertas**: Email/Slack em falha de DAG
- **Métricas**: Duração, taxa de sucesso, retries
- **Health check**: `/health` endpoint

## Acesso Local

```bash
docker-compose up -d
# Airflow UI: http://localhost:8080
# User: airflow / Password: airflow
```

## Deploy (Produção)

Gerenciado via Argo CD (repo `continuous-deployment/airflow/`).

```yaml
# values.prod.yaml (overlay)
airflow:
  executor: KubernetesExecutor
  workers:
    replicas: 2
  scheduler:
    replicas: 1
```
