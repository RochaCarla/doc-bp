# Tutorial: Primeiro Model no dbt

Guia passo a passo para criar seu primeiro model de transformação no GovHub BR.

## Pré-requisitos

- Ambiente local rodando (`docker-compose up -d`)
- PostgreSQL acessível
- dbt instalado (via `make setup`)

## 1. Verificar conexão

```bash
cd dbt/
dbt debug
```

Deve mostrar "All checks passed!"

## 2. Criar um model Silver

Crie `dbt/models/silver/exemplo_orgaos.sql`:

```sql
{{ config(materialized='table', schema='silver') }}

SELECT
    id,
    TRIM(nome) AS nome,
    LOWER(sigla) AS sigla,
    tipo,
    NOW() AS loaded_at
FROM {{ source('bronze', 'siorg_raw') }}
WHERE id IS NOT NULL
  AND nome IS NOT NULL
```

## 3. Adicionar testes

Em `dbt/models/schema.yml`, adicione:

```yaml
models:
  - name: exemplo_orgaos
    description: "Órgãos governamentais (tutorial)"
    columns:
      - name: id
        tests:
          - not_null
          - unique
      - name: nome
        tests:
          - not_null
```

## 4. Executar

```bash
# Rodar apenas o novo model
dbt run --select exemplo_orgaos

# Rodar testes
dbt test --select exemplo_orgaos

# Ver documentação
dbt docs generate
dbt docs serve
```

## 5. Verificar resultado

```bash
psql -h localhost -p 5432 -U govhub -d govhub -c "SELECT * FROM silver.exemplo_orgaos LIMIT 5;"
```

## 6. Próximos passos

- Criar model Gold que agrega a partir do Silver
- Adicionar mais testes (relationships, accepted_values)
- Explorar materializations (`incremental` para tabelas grandes)
- Estudar models existentes em `dbt/models/`

## Comandos Úteis

| Comando | Descrição |
|---------|-----------|
| `dbt run` | Executa todos os models |
| `dbt run --select silver.*` | Apenas Silver |
| `dbt test` | Roda todos os testes |
| `dbt source freshness` | Verifica freshness |
| `dbt docs generate && dbt docs serve` | Documentação local |
| `dbt run --full-refresh` | Recria tabelas |

## Referências

- [dbt Quickstart](https://docs.getdbt.com/quickstarts)
- [dbt Best Practices](https://docs.getdbt.com/best-practices)
