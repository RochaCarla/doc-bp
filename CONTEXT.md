# GovHub BR — Documentação

Plataforma open source de integração de dados governamentais brasileiros. Este repositório contém a documentação técnica (MkDocs).

## Language

### Sistemas Fonte

**TransfereGov**:
Sistema do governo federal que gerencia convênios e contratos de repasse entre União e entes subnacionais (estados, municípios, ONGs).
_Avoid_: Siconv (nome antigo do sistema)

**Siape**:
Sistema de administração de pessoal civil e militar — cadastro de servidores e folha de pagamento da União.
_Avoid_: sistema de RH

**Siafi**:
Sistema Integrado de Administração Financeira — registra a execução orçamentária e financeira da União.
_Avoid_: sistema financeiro

**ComprasGov**:
Plataforma de compras públicas do governo federal — licitações, contratos, atas de registro de preço.
_Avoid_: ComprasNet (nome antigo)

**Siorg**:
Sistema de Informações Organizacionais — estrutura organizacional do governo federal (órgãos, unidades, cargos).

### Arquitetura de Dados

**Camada Bronze**:
Dados brutos ingeridos das fontes governamentais, armazenados como arquivos no MinIO sem transformação.
_Avoid_: raw layer, landing zone

**Camada Silver**:
Dados limpos, deduplicados e normalizados em schemas PostgreSQL, prontos para modelagem.
_Avoid_: clean layer, staging

**Camada Gold**:
Dados agregados, métricas e views prontos para consumo por BI e análise.
_Avoid_: consumption layer, mart

**Fork leve**:
Instância lógica do GovHub para um contexto específico (órgão, tema). Compartilha cluster e infra, isolado por schemas PostgreSQL. Contém apenas novas DAGs e models dbt.
_Avoid_: fork completo, instância separada

### Pipeline

**DAG de ingestão**:
Pipeline Airflow com 3 tasks sequenciais: extract (API → MinIO), load (MinIO → PostgreSQL staging), trigger dbt (transformação Silver/Gold).
_Avoid_: ETL (genérico demais)

**dbt docs**:
Documentação auto-gerada pelo dbt com detalhes de colunas, tipos e linhagem. Hospedado em https://dbt.ipea.gov-hub.io/#!/overview. Fonte de verdade para dicionário de dados a nível de coluna.

### Governança

**Acesso governado**:
Caminho de consulta via Trino + Ranger para dados sensíveis (ex: Siape/folha). Aplica row-level security e column masking. Não é o caminho padrão — Superset acessa PostgreSQL diretamente.
_Avoid_: controle de acesso (genérico, não distingue os dois níveis)

**OpenMetadata**:
Catálogo de dados e linhagem. Deployed com configuração parcial — catálogo básico funcional, owners e domínios por fork a completar.

## Example Dialogue

> **Dev**: "Quero adicionar dados de um novo órgão ao GovHub."
>
> **Domain Expert**: "Você vai criar um fork leve. Isso significa um novo repo com DAGs de ingestão para as APIs do órgão e models dbt que escrevem em schemas PG dedicados — tipo `meuorgao_silver`, `meuorgao_gold`. A infra (cluster, MinIO, Airflow, Superset) é compartilhada."
>
> **Dev**: "E como controlo quem vê os dados sensíveis?"
>
> **Domain Expert**: "Dados públicos vão pro Superset direto via PostgreSQL. Dados sensíveis — tipo folha de pagamento do Siape — passam pelo acesso governado: Trino + Ranger aplicam row-level security antes de chegar no JupyterHub."
>
> **Dev**: "Onde vejo o schema completo de cada tabela?"
>
> **Domain Expert**: "No dbt docs. A documentação do MkDocs explica o domínio e as entidades conceituais. Para detalhe de coluna, tipo e linhagem, vai no dbt docs."
