# Tutorial: Primeira DAG no Airflow

Guia passo a passo para criar sua primeira DAG de ingestão no GovHub BR.

## Pré-requisitos

- Ambiente local rodando (`docker-compose up -d`)
- Airflow acessível em http://localhost:8080

## 1. Criar o arquivo da DAG

Crie `airflow/dags/minha_primeira_dag.py`:

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "govhub",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


def extract():
    """1. Extract: simula extração de dados de uma API gov."""
    print("Extraindo dados da API...")
    data = {"registros": 42, "fonte": "exemplo"}
    # Em produção: salva como arquivo no MinIO (Bronze)
    return data


def load(**context):
    """2. Load: simula carga do MinIO para PostgreSQL."""
    data = context["ti"].xcom_pull(task_ids="extract")
    print(f"Carregando {data['registros']} registros no PostgreSQL (staging)")
    # Em produção: lê do MinIO e insere em staging tables no PG


with DAG(
    "minha_primeira_dag",
    default_args=default_args,
    description="Tutorial - primeira DAG (3 passos)",
    schedule_interval=None,  # Trigger manual
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["tutorial"],
) as dag:

    # 1. Extract: API → MinIO (Bronze)
    task_extract = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    # 2. Load: MinIO → PostgreSQL (staging)
    task_load = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    # 3. Trigger dbt: staging → Silver/Gold
    task_dbt = BashOperator(
        task_id="trigger_dbt",
        bash_command="cd /opt/dbt && dbt run --select staging.+",
    )

    task_extract >> task_load >> task_dbt
```

## 2. Verificar na UI

1. Acesse http://localhost:8080
2. Procure `minha_primeira_dag` na lista
3. Ative a DAG (toggle)
4. Clique em "Trigger DAG" (▶️)

## 3. Verificar execução

- **Graph**: Visualize a sequência de tasks
- **Logs**: Clique em cada task → Logs para ver output
- **XCom**: Verifique valores passados entre tasks

## 4. Próximos passos

- Adicionar upload real para MinIO (usar `minio_default` connection)
- Adicionar schedule (`@daily`, `0 6 * * *`)
- Adicionar alertas em caso de falha
- Estudar as DAGs existentes em `airflow/dags/`

## Referências

- [Airflow Tutorial Oficial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html)
- [Airflow Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html)
