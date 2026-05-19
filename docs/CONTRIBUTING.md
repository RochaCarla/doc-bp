# Contribuindo com o GovHub BR

Obrigado pelo interesse em contribuir! O GovHub BR é um projeto open source que busca transformar dados governamentais em ativos estratégicos.

## Como Contribuir

1. **Abra uma issue** para reportar problemas ou sugerir melhorias
2. **Fork** o repositório
3. **Crie uma branch** (`feat/`, `fix/`, `docs/`)
4. **Faça suas alterações** com commits assinados (GPG)
5. **Abra um PR** descrevendo o porquê das mudanças

## Áreas de Contribuição

| Área | Descrição | Repo |
|------|-----------|------|
| Pipeline | Novas DAGs, models dbt | `data-application-gov-hub` |
| Dashboards | Novos painéis Superset | `data-application-gov-hub` |
| Infra | Manifests K8s, Helm | `continuous-deployment` |
| Documentação | Melhorias nos docs | `gov-hub` ou este repo |
| Pesquisa | POCs, IA, OCR | `govhub-research` |
| Governança | OpenMetadata config | `openmetadata-declarative-governance` |

## Padrões

- **Branches**: `feat/`, `fix/`, `refactor/`, `docs/`
- **Commits**: [Conventional Commits](https://www.conventionalcommits.org/)
- **GPG**: Commits assinados obrigatórios
- **Code style**: Seguir `make lint`
- **Testes**: `make test` deve passar

## Ambiente

Veja [Setup Local](onboarding/setup-local.md) para configurar seu ambiente de desenvolvimento.

## Contato

- Issues no GitHub
- Email: lablivreunb@gmail.com
