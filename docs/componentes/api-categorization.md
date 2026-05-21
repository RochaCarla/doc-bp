# decidim-api-categorization

**Tipo**: Componente customizado (LAPPIS/UnB)
**Repositório**: [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo)

Extensão da API GraphQL do Decidim para categorização de conteúdos, permitindo classificação programática de propostas e outros recursos.

## Funcionalidades

- **Endpoints de categorização** — API para atribuir categorias a recursos via GraphQL
- **Categorização em lote** — classificação de múltiplos recursos de uma vez
- **Integração com taxonomias** — uso das categorias e escopos do Decidim
- **Consultas filtradas** — queries GraphQL para buscar recursos por categoria

## Caso de Uso

Permite que sistemas externos ou scripts automatizados categorizem propostas em massa — útil quando há milhares de propostas que precisam ser classificadas por tema, região ou prioridade.

## API

O componente estende a API GraphQL do Decidim (acessível em `/api`). Consulte a documentação da API do Decidim para o formato de queries e mutations.

## Referência

- [Documentação oficial da API do Decidim](https://docs.decidim.org/en/develop/develop/api/)
