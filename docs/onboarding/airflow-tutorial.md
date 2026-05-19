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
from datetime import datetime, timedelta

default_args = {
    "owner": "govhub",
    "retries": 2,
    "retry_delay": timedelta(minutes=2),
}


def extract():
    """Simula extração de dados."""
    print("Extraindo dados...")
    data = {"registros": 42, "fonte": "exemplo"}
    return data


def load(**context):
    """Simula carga no MinIO."""
    data = context["ti"].xcom_pull(task_ids="extract")
    print(f"Carregando {data['registros']} registros no MinIO")


with DAG(
    "minha_primeira_dag",
    default_args=default_args,
    description="Tutorial - primeira DAG",
    schedule_interval=None,  # Trigger manual
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["tutorial"],
) as dag:

    task_extract = PythonOperator(
        task_id="extract",
        python_callable=extract,
    )

    task_load = PythonOperator(
        task_id="load",
        python_callable=load,
    )

    task_extract >> task_load
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
