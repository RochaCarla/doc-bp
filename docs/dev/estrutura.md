# Estrutura do Código

Visão geral da organização do repositório `decidim-govbr`.

## Estrutura de Diretórios

O `decidim-govbr` segue a estrutura padrão de uma aplicação Rails/Decidim:

```
decidim-govbr/
├── app/
│   ├── assets/              # Stylesheets, JavaScripts, imagens
│   ├── cells/               # View components (Decidim cells)
│   ├── commands/             # Command objects (business logic)
│   ├── controllers/          # Controllers HTTP
│   ├── forms/                # Form objects (validação de entrada)
│   ├── helpers/              # View helpers
│   ├── mailers/              # E-mail templates
│   ├── models/               # ActiveRecord models
│   ├── packs/                # Webpacker/Shakapacker entry points
│   ├── permissions/          # Authorization e permissões
│   ├── presenters/           # Presenters (formatação para views)
│   ├── queries/              # Query objects (consultas complexas)
│   ├── serializers/          # Serializers (export de dados)
│   └── views/                # Templates ERB/HTML
├── config/
│   ├── environments/         # Config por ambiente (dev/test/prod)
│   ├── initializers/         # Inicializadores Rails e Decidim
│   ├── locales/              # Traduções (pt-BR, en, es)
│   ├── database.yml          # Configuração do banco
│   └── routes.rb             # Rotas da aplicação
├── db/
│   ├── migrate/              # Migrações do banco de dados
│   └── seeds.rb              # Dados iniciais para desenvolvimento
├── lib/                      # Código auxiliar e tasks Rake
├── spec/                     # Testes RSpec
├── Gemfile                   # Dependências Ruby (módulos + componentes)
├── Gemfile.lock              # Lock de versões
├── package.json              # Dependências Node.js
└── Procfile                  # Processos (web, worker, etc.)
```

## Padrões do Decidim

O Decidim utiliza padrões específicos que diferem de uma aplicação Rails convencional:

### Commands

Lógica de negócio encapsulada em command objects (padrão Rectify/Wisper). Cada ação do usuário é um command:

```ruby
# app/commands/decidim/create_proposal.rb
class Decidim::CreateProposal < Decidim::Command
  def call
    return broadcast(:invalid) if form.invalid?
    create_proposal
    broadcast(:ok, proposal)
  end
end
```

### Forms

Validação de dados de entrada separada dos models:

```ruby
# app/forms/decidim/proposal_form.rb
class Decidim::ProposalForm < Decidim::Form
  attribute :title, String
  attribute :body, String
  validates :title, presence: true, length: { maximum: 150 }
end
```

### Cells

View components reutilizáveis (gem `cells`), usados no lugar de partials Rails:

```ruby
# app/cells/decidim/proposal_cell.rb
class Decidim::ProposalCell < Decidim::ViewModel
  def show
    render
  end
end
```

### Permissions

Sistema de permissões declarativo por componente:

```ruby
# app/permissions/decidim/proposals/permissions.rb
class Decidim::Proposals::Permissions < Decidim::DefaultPermissions
  def permissions
    return permission_action if permission_action.scope != :public
    allow! if permission_action.subject == :proposal
    permission_action
  end
end
```

## Convenções de Código

- **Namespacing**: todo código do Decidim vive sob o namespace `Decidim::`
- **Traduções**: todas as strings de interface usam I18n (`t(".title")`)
- **Locale principal**: `pt-BR` — arquivo em `config/locales/pt-BR.yml`
- **Testes**: RSpec com FactoryBot, organizados espelhando `app/`
- **Linting**: RuboCop com configuração do Decidim
