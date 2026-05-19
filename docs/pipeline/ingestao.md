# Ingestão de Dados

Documentação das fontes de dados governamentais integradas pelo GovHub BR.

## Fontes

| Sistema | Domínio | Método | Frequência |
|---------|---------|--------|-----------|
| TransfereGov | Transferências voluntárias | API REST | Diária |
| Siape | Pessoal civil e militar | Certificado digital | Semanal |
| Siafi | Administração financeira | API + certificado | Diária |
| ComprasGov | Compras públicas | API REST | Diária |
| Siorg | Estrutura organizacional | API REST | Semanal |

## TransfereGov

**Domínio**: Convênios e transferências voluntárias da União.

| Aspecto | Detalhe |
|---------|---------|
| URL base | `https://api.transferegov.gov.br/` |
| Autenticação | API Key |
| Formato | JSON |
| Paginação | Offset-based |
| Rate limit | A verificar |

**Dados coletados**:

- Programas de transferência
- Convênios celebrados
- Valores transferidos
- Órgãos concedentes e convenentes
- Status e situação

## Siape

**Domínio**: Sistema Integrado de Administração de Pessoal.

| Aspecto | Detalhe |
|---------|---------|
| Acesso | Certificado digital (e-CPF/e-CNPJ) |
| Formato | CSV |
| Volume | Grande (milhões de registros) |
| Sensibilidade | Dados pessoais — anonimizar |

**Dados coletados**:

- Quantitativo de servidores por órgão
- Distribuição por cargo/carreira
- Indicadores de pessoal (agregados)

!!! warning "Dados Sensíveis"
    Dados do Siape contêm informações pessoais. A ingestão deve
    anonimizar/agregar antes de armazenar na camada Silver.

## Siafi

**Domínio**: Sistema Integrado de Administração Financeira.

| Aspecto | Detalhe |
|---------|---------|
| Acesso | API + certificado |
| Formato | JSON |
| Domínio | Execução orçamentária e financeira |

**Dados coletados**:

- Execução orçamentária
- Empenhos, liquidações, pagamentos
- Dotação por órgão/programa

## ComprasGov

**Domínio**: Portal de compras do governo federal.

| Aspecto | Detalhe |
|---------|---------|
| URL base | `https://compras.dados.gov.br/` |
| Autenticação | Aberta (dados públicos) |
| Formato | JSON / CSV |

**Dados coletados**:

- Contratos vigentes
- Licitações
- Atas de registro de preço
- Fornecedores

## Siorg

**Domínio**: Sistema de Informações Organizacionais.

| Aspecto | Detalhe |
|---------|---------|
| URL base | `https://siorg.gov.br/` |
| Autenticação | Aberta |
| Formato | JSON |

**Dados coletados**:

- Estrutura organizacional (órgãos, unidades)
- Hierarquia administrativa
- Competências e atribuições

## Padrões de Ingestão

### Idempotência

Todas as DAGs são idempotentes — re-execuções não duplicam dados:

```python
# Padrão: particionamento por data
output_path = f"bronze/{source}/{execution_date}/data.json"
# MinIO overwrite = True (mesmo path = mesma execução)
```

### Tratamento de Erros

```python
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
    "on_failure_callback": alert_on_failure,
}
```

### Certificados

Certificados digitais (Siape, Siafi) são gerenciados como Kubernetes Secrets:

```bash
kubectl -n airflow create secret generic siape-cert \
    --from-file=cert.pem=./certificado.pem \
    --from-file=key.pem=./chave.pem
```
