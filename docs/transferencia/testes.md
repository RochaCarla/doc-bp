# Testes e qualidade

Como a qualidade do `decidim-govbr` é verificada e como manter a suíte de testes.

## Suíte de testes

| Suíte | Pasta | Arquivos | Como rodar |
|-------|-------|---------:|-----------|
| RSpec | `spec/` | 135 | `bundle exec rspec` |
| Minitest | `test/` | 1 | `bundle exec rails test` |

Distribuição dos testes RSpec:

| Pasta | Arquivos | O que testa |
|-------|---------:|-------------|
| `spec/commands` | 53 | Regras de negócio (commands) |
| `spec/forms` | 14 | Validações de formulário |
| `spec/models` | 13 | Models |
| `spec/requests` | 7 | Requisições HTTP de ponta a ponta |
| `spec/controllers` | 7 | Controllers |
| `spec/permissions` | 6 | Permissões |
| `spec/services` | 5 | Serviços (ex.: `ExternalAuthService`) |
| `spec/lib` | 5 | Serializadores e extensões |
| `spec/views` | 4 | Views |
| `spec/presenters` | 4 | Presenters |
| `spec/types` | 3 | Tipos GraphQL |
| `spec/jobs` | 3 | Jobs |
| `spec/helpers` | 3 | Helpers |
| `spec/cells` | 3 | Cells |
| `spec/system` | 2 | Navegador (Capybara + Chrome) |
| `spec/mailers` | 2 | E-mails |
| `spec/queries` | 1 | Consultas |

Apoio: `spec/factories.rb` (FactoryBot), `spec/support/`, `spec/shared/`, `spec/rails_helper.rb`. Os testes usam as fábricas e helpers de teste do Decidim (`decidim-dev`).

Indicadores da suíte estão em [Estatísticas › Qualidade](../estatisticas/qualidade.md#testes-e-analise-estatica).

## Rodar localmente

```bash
# preparar o banco de teste
RAILS_ENV=test bundle exec rails db:create db:schema:load

# tudo
bundle exec rspec
bundle exec rails test

# um arquivo ou um exemplo
bundle exec rspec spec/services/external_auth_service_spec.rb
bundle exec rspec spec/services/external_auth_service_spec.rb:42
```

Testes de sistema precisam do Chrome. No CI ele é instalado com `bin/setup_chrome`.

## Pipeline de integração contínua

Definido em `.gitlab-ci.yml`:

| Job | Estágio | Verifica | Bloqueia? |
|-----|---------|----------|-----------|
| `Lint` | `lint` | RuboCop | Sim |
| `SAST` | `test` | Brakeman (envia relatório por e-mail) | Não |
| `SCA` | `test` | Trivy (dependências) | Não |
| `Testing` | `test` | `rails test` e `rspec` com PostgreSQL 13.2 e Redis 6 | Sim |
| `Build` | `build` | Build da imagem Docker | Sim |

## Regras para a equipe

- Toda correção de defeito vem com um teste que falhava antes.
- Toda sobrescrita nova de arquivo do Decidim vem com teste do comportamento alterado. As [sobrescritas](sobrescritas.md) são o maior risco na atualização do Decidim, e os testes são a forma de saber se o comportamento se manteve.
- Mudanças em integrações (gov.br, OP-BP, EJ) têm teste de request com o serviço externo simulado.

## Lacunas

| Lacuna | Recomendação |
|--------|--------------|
| Cobertura não medida | Ativar o SimpleCov no job `Testing` e publicar o relatório como artefato |
| Poucos testes de sistema (2) | Cobrir as jornadas críticas: login gov.br (simulado), envio e voto em proposta, resposta a formulário, vínculo OP-BP |
| 492 sobrescritas e 135 arquivos de teste | Priorizar testes nas sobrescritas mais alteradas ([inventário](sobrescritas.md#as-40-sobrescritas-mais-alteradas)) |
| 2.581 ocorrências pendentes no `.rubocop_todo.yml` | Reduzir aos poucos, a cada arquivo tocado |
| Brakeman e Trivy não bloqueiam | Tornar bloqueantes para severidade alta |
| Sem testes de carga | Antes de grandes processos, rodar teste de carga na home, no login e na votação |
