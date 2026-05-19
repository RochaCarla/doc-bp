# Qualidade de Dados

Estratégia de validação e monitoramento da qualidade dos dados no GovHub BR.

## Abordagem Multi-Camada

```mermaid
graph LR
    A[Ingestão] -->|Retries, logs| B[Bronze]
    B -->|dbt tests| C[Silver]
    C -->|dbt tests + business rules| D[Gold]
    D -->|OpenMetadata| E[Governança]
```

## Testes dbt

### Schema Tests

Aplicados automaticamente via `schema.yml`:

| Teste | Descrição | Camada |
|-------|-----------|--------|
| `not_null` | Coluna não pode ser nula | Silver, Gold |
| `unique` | Valores únicos | Silver |
| `accepted_values` | Valores dentro de conjunto esperado | Silver |
| `relationships` | Integridade referencial | Gold |

### Custom Tests

```sql
-- tests/assert_transferencias_valor_positivo.sql
-- Garante que não há transferências com valor negativo
SELECT *
FROM {{ ref('transferencias') }}
WHERE valor < 0

-- tests/assert_datas_validas.sql
-- Garante que datas estão em range razoável
SELECT *
FROM {{ ref('transferencias') }}
WHERE data_celebracao < '2000-01-01'
   OR data_celebracao > CURRENT_DATE + INTERVAL '1 day'
```

### Freshness

```yaml
# models/staging/schema.yml
sources:
  - name: bronze
    freshness:
      warn_after: {count: 24, period: hour}
      error_after: {count: 48, period: hour}
    loaded_at_field: _loaded_at
    tables:
      - name: transferegov_raw
      - name: comprasgov_raw
```

## Métricas de Qualidade

| Métrica | Definição | Threshold |
|---------|-----------|-----------|
| Completeness | % de campos não-nulos | > 95% |
| Uniqueness | % de registros únicos (por PK) | 100% |
| Timeliness | Idade do dado mais recente | < 48h |
| Validity | % dentro de valores aceitos | > 99% |
| Consistency | Integridade referencial | 100% |

## Execução

```bash
# Rodar todos os testes
dbt test

# Testes apenas de Silver
dbt test --select silver.*

# Testes de freshness
dbt source freshness

# Verbose (ver falhas)
dbt test --select silver.* --store-failures
```

## Monitoramento

### Alertas

- **dbt test failure**: Notificação via Airflow callback
- **Source freshness warning**: Alerta se dados atrasados > 24h
- **Source freshness error**: Alerta crítico se > 48h

### OpenMetadata

Integração com OpenMetadata para:

- Visualizar resultados de testes por dataset
- Rastrear tendências de qualidade ao longo do tempo
- Atribuir ownership a problemas de qualidade
- Dashboard de data quality score

## Boas Práticas

1. **Todo model Silver deve ter testes** de `not_null` e `unique` nas PKs
2. **Todo model Gold deve ter testes** de `relationships` com dimensões
3. **Freshness** configurado para todas as sources
4. **Custom tests** para regras de negócio específicas
5. **`--store-failures`** em produção para debug
