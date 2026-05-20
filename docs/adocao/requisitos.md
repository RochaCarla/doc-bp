# Requisitos para Adoção

Pré-requisitos de infraestrutura e equipe para implantar o GovHub BR no seu órgão.

## Público

Esta seção é voltada para **equipes de TI do governo** que desejam implantar o GovHub para integrar dados do seu órgão ou contexto.

## Infraestrutura Mínima

### Cluster Kubernetes

| Recurso | Mínimo | Recomendado |
|---------|--------|-------------|
| Nodes | 3 | 5+ |
| CPU total | 16 cores | 32+ cores |
| Memória total | 32 GB | 64+ GB |
| Storage (SSD) | 500 GB | 1+ TB |
| Kubernetes versão | 1.26+ | 1.28+ |

### Componentes Obrigatórios

| Componente | Necessário para | Alternativa |
|------------|----------------|-------------|
| Kubernetes | Runtime de todos os serviços | — |
| Helm 3 | Deploy dos charts | — |
| Git | Versionamento e GitOps | — |
| Certificados TLS | HTTPS em produção | Let's Encrypt |
| DNS | Acesso aos serviços | — |

### Conectividade

- Acesso à internet para download de imagens Docker
- Acesso às APIs governamentais (TransfereGov, ComprasGov, Siorg)
- Certificados digitais para Siape/Siafi (se aplicável)
- VPN ou rede interna para acesso ao cluster

## Equipe Mínima

| Perfil | Responsabilidade | Quantidade |
|--------|------------------|------------|
| DevOps/SRE | Cluster K8s, Argo CD, monitoramento | 1-2 |
| Engenheiro de Dados | DAGs Airflow, models dbt | 1-2 |
| Analista de Dados | Dashboards Superset, análises | 1 |

## Conhecimentos Necessários

| Área | Básico | Intermediário |
|------|--------|---------------|
| Kubernetes | `kubectl`, pods, services | Helm, operators, RBAC |
| Docker | Build, run, compose | Multi-stage builds |
| Git | Clone, commit, push | Rebase, GPG, workflows |
| SQL | SELECT, JOIN, GROUP BY | Window functions, CTEs |
| Python | Scripts básicos | Airflow operators |

## Decisões Prévias

Antes de iniciar o deploy, defina:

1. **Quais fontes de dados** integrar (começar com 1-2 públicas é recomendado)
2. **Modelo de deploy**: cluster próprio vs. compartilhado
3. **Modelo de fork**: fork leve (schemas PG) vs. instância separada
4. **Política de acesso**: quem verá quais dados
5. **Ambiente**: preprod + prod ou apenas prod

## Checklist Pré-Deploy

- [ ] Cluster K8s operacional e acessível
- [ ] `kubectl`, `helm`, `argocd` CLI instalados
- [ ] Repositório Git criado para o fork
- [ ] DNS configurado para os serviços
- [ ] Certificados TLS disponíveis
- [ ] Credenciais de API das fontes escolhidas
- [ ] Equipe com acesso ao cluster

## Próximo Passo

→ [Deploy Inicial](deploy-inicial.md)
