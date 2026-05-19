# JupyterHub

Ambiente de notebooks para análise interativa e pesquisa no GovHub BR.

## Papel na Arquitetura

JupyterHub permite análises exploratórias conectadas ao PostgreSQL (Silver/Gold) e ao MinIO (Bronze), para cientistas de dados e pesquisadores.

## Acesso

| Ambiente | URL | Credenciais |
|----------|-----|-------------|
| Local | `http://localhost:8888` | token no terminal |
| Produção | Via VPN | Autenticação do cluster |

## Kernels Disponíveis

| Kernel | Bibliotecas |
|--------|-------------|
| Python 3.11 | pandas, sqlalchemy, matplotlib, seaborn, scikit-learn |

## Conexão com Dados

### PostgreSQL (Silver/Gold)

```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("postgresql://govhub:govhub_dev@postgres:5432/govhub")

# Ler tabela Gold
df = pd.read_sql("SELECT * FROM gold.fato_transferencias LIMIT 1000", engine)
```

### MinIO (Bronze)

```python
import boto3
import json

s3 = boto3.client("s3", endpoint_url="http://minio:9000",
                  aws_access_key_id="minioadmin",
                  aws_secret_access_key="minioadmin")

obj = s3.get_object(Bucket="bronze-transferegov", Key="2026-05-19/transferencias.json")
data = json.loads(obj["Body"].read())
```

## Convenções de Notebooks

- Prefixo numérico para ordem: `01_exploracao.ipynb`, `02_analise.ipynb`
- Documentar hipóteses e conclusões em Markdown cells
- Não commitar outputs pesados (usar `.gitignore` ou `nbstripout`)

## Deploy

Gerenciado via Argo CD:

```
continuous-deployment/
└── jupyterhub/
    ├── values.yaml
    └── values.prod.yaml
```

## Referências

- [JupyterHub Docs](https://jupyterhub.readthedocs.io/)
- Repo: [`continuous-deployment/jupyterhub`](https://github.com/GovHub-br/continuous-deployment/tree/main/jupyterhub)
