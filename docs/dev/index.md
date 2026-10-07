---
icon: material/code-tags
---

# Guia do Desenvolvedor

Para quem vai escrever código no `decidim-govbr` ou em componentes do Brasil Participativo.

<div class="grid cards" markdown>

-   :material-docker:{ .lg .middle } **[Setup Local](setup.md)**

    ---

    Suba o ambiente com Docker Compose, crie a organização em `/system` e rode os testes.

-   :material-file-tree:{ .lg .middle } **[Estrutura do Código](estrutura.md)**

    ---

    Pastas do repositório, como o core sobrescreve o Decidim e onde está o código próprio.

-   :material-source-pull:{ .lg .middle } **[Como Contribuir](contribuir.md)**

    ---

    Branches, Conventional Commits, merge requests para `develop` e o pipeline de CI.

-   :material-puzzle-plus:{ .lg .middle } **[Criar Componente](criar-componente.md)**

    ---

    Quando a funcionalidade merece uma gem própria, como gerar, registrar e instalar.

</div>

## Antes de mudar um comportamento

1. Veja se o arquivo já foi sobrescrito em `app/` ou `lib/` ([Estrutura do Código](estrutura.md#como-as-customizacoes-sao-feitas)).
2. Confira o que já foi alterado em relação ao Decidim em [Inovação](../inovacao/index.md).
3. Para telas, siga o [Design System gov.br](../design-system/guia.md).
4. Para dados, consulte o [Banco de Dados](../banco-de-dados/index.md).

## Stack

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Ruby 3.0.4 |
| Framework | Rails 6.1.7 + Decidim 0.27.2 |
| Front-end | ERB, Cells, Webpacker 6, Design System gov.br |
| Banco | PostgreSQL |
| Jobs | Sidekiq + Redis, `whenever` |
| Testes | RSpec, Minitest, Capybara |
| Qualidade | RuboCop, Brakeman, Trivy |
