# Estrutura do Código

Visão geral da organização do repositório `decidim-govbr`.

## Estrutura de diretórios

```
decidim-govbr/
├── app/
│   ├── cells/decidim/        # Cells sobrescritas ou novas
│   ├── commands/decidim/     # Commands (lógica de negócio)
│   ├── controllers/
│   │   ├── api/              # API JSON própria (home_processes)
│   │   ├── decidim/          # Controllers sobrescritos do Decidim
│   │   └── survey_attachments_controller.rb
│   ├── forms/decidim/        # Form objects
│   ├── helpers/
│   ├── jobs/decidim/         # Jobs Sidekiq (identidades, instâncias, troca de fase)
│   ├── models/decidim/       # Models sobrescritos (proposal, question, assembly…)
│   ├── packs/                # Entradas e estilos do Webpacker
│   ├── permissions/decidim/  # Permissões sobrescritas
│   ├── queries/decidim/      # Query objects
│   ├── serializers/decidim/  # Exportações (propostas, comentários…)
│   ├── services/             # ExternalAuthService, serviços de idioma
│   ├── validators/
│   └── views/                # Views sobrescritas, layouts, login externo
├── config/
│   ├── initializers/         # decidim.rb, omniauth_govbr.rb, proposals.rb…
│   ├── locales/              # pt-BR, en, es
│   ├── schedule.rb           # Tarefas periódicas (whenever)
│   ├── secrets.yml           # Mapeia variáveis de ambiente
│   └── routes.rb
├── db/
│   ├── migrate/
│   ├── seeds/                # JSONs de seeds (ex.: assembleias de conferências)
│   └── seeds.rb              # Cria o admin de sistema
├── lib/
│   ├── decidim/              # Extensões de libs do Decidim (comments, forms, meetings…)
│   ├── extends/
│   └── tasks/                # Rake tasks do Brasil Participativo
├── spec/                     # RSpec
├── test/                     # Minitest (rails test)
├── vendor/                   # Gitlinks de decidim-module-homes e decidim-module-mobile (sem .gitmodules; as gems vêm do Gemfile)
├── Dockerfile                # Imagem de desenvolvimento
├── docker-compose.yml
├── Procfile
├── start.sh                  # Entrypoint do container de desenvolvimento
└── .gitlab-ci.yml
```

## Como as customizações são feitas

O core sobrescreve arquivos do Decidim mantendo o **mesmo caminho** da gem original. O Rails carrega primeiro o arquivo da aplicação, então a versão em `app/` substitui a do upstream.

| Exemplo de arquivo sobrescrito | O que muda |
|-------------------------------|-----------|
| `app/models/decidim/proposals/proposal.rb` | Limite de tempo de edição, regras de votação |
| `app/models/decidim/forms/question.rb` | `max_files` para perguntas de arquivo |
| `app/permissions/decidim/comments/permissions.rb` | Edição de comentário em até 5 minutos |
| `lib/decidim/comments/comment_serializer.rb` | Colunas `deletado_em` e `moderado_em` na exportação |
| `app/forms/decidim/participatory_processes/admin/participatory_process_form.rb` | Opção de votos mutuamente exclusivos |
| `app/forms/decidim/assemblies/admin/assembly_form.rb` | Atributo `unlisted` |

!!! warning "Atualização do Decidim"
    Cada arquivo sobrescrito precisa ser comparado com a nova versão do upstream ao atualizar o Decidim. Antes de alterar um comportamento, procure se o arquivo já existe em `app/` ou `lib/`.

## Código próprio do Brasil Participativo

| Local | Conteúdo |
|-------|----------|
| `app/services/external_auth_service.rb` | Vínculo de conta com a API OP-BP via JWT |
| `app/controllers/api/home_processes_controller.rb` | `GET /api/home_processes` |
| `app/jobs/decidim/remove_duplicated_govbr_identities_job.rb` | Remove identidades gov.br duplicadas |
| `app/jobs/decidim/public_bodies_to_instances_job.rb` | Cria instâncias a partir de órgãos públicos |
| `app/queries/decidim/proposals/govbr/` | Consultas de votação exclusiva |
| `lib/tasks/` | `remove_duplicated_govbr_identities`, `public_bodies_to_instances`, `change_active_step`, `update_user_proposals_statistics_data`, `sitemap`, `botapi`, `add_authorization_to_govbr_users` |

## Padrões do Decidim

### Commands

Lógica de negócio encapsulada em command objects:

```ruby
class Decidim::CreateProposal < Decidim::Command
  def call
    return broadcast(:invalid) if form.invalid?
    create_proposal
    broadcast(:ok, proposal)
  end
end
```

### Forms

Validação de entrada separada dos models:

```ruby
class Decidim::Forms::Admin::QuestionForm < Decidim::Form
  attribute :max_files, Integer, default: 10
  validates :max_files, presence: true,
            numericality: { greater_than: 0, less_than_or_equal_to: 50 },
            if: :has_attachments?
end
```

### Cells

View components reutilizáveis (gem `cells`), usados no lugar de partials.

### Permissions

Permissões declarativas por componente:

```ruby
module Decidim::Comments
  class Permissions < Decidim::DefaultPermissions
    COMMENT_EDIT_TIME_LIMIT = 5.minutes.freeze
    # ...
  end
end
```

## Convenções de código

- **Namespacing**: código do Decidim sob `Decidim::`; código específico do Brasil Participativo em `Decidim::Govbr::` quando possível.
- **Traduções**: strings de interface via I18n. Locale principal em `config/locales/pt-BR.yml` e `config/locales/pt-BR/`.
- **Testes**: RSpec com FactoryBot, espelhando `app/`, e Minitest em `test/`.
- **Linting**: RuboCop (`.rubocop.yml`).
- **Versão no rodapé**: a versão publicada é atualizada manualmente em `app/views/layouts/decidim/_main_footer.html.erb` (commits `chore: atualiza versão no footer`).
