# Controle de Acesso

Políticas de acesso aos dados e serviços do GovHub BR.

## Níveis de Acesso

| Nível | Quem | O que pode |
|-------|------|-----------|
| Admin | Equipe core | Tudo |
| Contribuidor | Devs ativos | Pipeline, notebooks, PRs |
| Visualizador | Gestores, sociedade | Dashboards Superset |
| Público | Qualquer pessoa | Dados abertos (se publicados) |

## Acesso por Serviço

| Serviço | Autenticação | Notas |
|---------|-------------|-------|
| Airflow | User/password ou SSO | Acesso restrito a equipe pipeline |
| Superset | Roles (Admin/Alpha/Gamma) | Dashboards por permissão |
| JupyterHub | Auth do cluster | Pesquisadores e DS |
| MinIO | Access Key / Secret Key | Apenas via pipeline |
| PostgreSQL | User/password | Conexão via services internos |
| Argo CD | RBAC do cluster | Apenas equipe infra |

## Row-Level Security (Superset)

Para limitar dados por perfil de usuário:

```sql
-- Exemplo: gestor vê apenas seu órgão
SELECT * FROM gold.fato_transferencias
WHERE orgao_concedente = '{{ current_user.org_code }}'
```

## Dados Sensíveis

| Fonte | Sensibilidade | Tratamento |
|-------|---------------|-----------|
| Siape | Alta (dados pessoais) | Anonimização na camada Silver |
| Siafi | Média (financeiro) | Acesso restrito |
| TransfereGov | Baixa (público) | Sem restrições |
| ComprasGov | Baixa (público) | Sem restrições |
| Siorg | Baixa (público) | Sem restrições |

## Workshop: Apache Ranger + Trino

Para cenários avançados de controle de acesso, o GovHub mantém um workshop sobre:

- **Apache Ranger**: Políticas centralizadas de acesso
- **Trino**: Query engine federada com controle por coluna/row

Repo: [`data-governance-workshop`](https://github.com/GovHub-br/data-governance-workshop)
