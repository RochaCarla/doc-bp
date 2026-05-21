# Criar Componente

Guia para criar um novo componente customizado para o Brasil Participativo.

## Conceito

No Decidim, um **componente customizado** é um Rails Engine empacotado como gem Ruby. Ele se registra no Decidim via manifest e pode adicionar models, controllers, views, APIs e permissões próprias.

Os componentes customizados vivem no repositório [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo).

## Pré-requisitos

- [Setup local](setup.md) funcionando
- Familiaridade com a [estrutura do código](estrutura.md) do Decidim
- Ruby on Rails e o conceito de Rails Engines

## Scaffolding com o Generator

O Decidim fornece um generator CLI para criar a estrutura inicial de um componente:

```bash
decidim --component decidim-module-meu_componente
```

Isso cria a seguinte estrutura:

```
decidim-module-meu_componente/
├── app/
│   ├── cells/
│   ├── commands/
│   ├── controllers/
│   ├── forms/
│   ├── helpers/
│   ├── models/
│   ├── permissions/
│   └── views/
├── config/
│   └── locales/
├── db/
│   └── migrate/
├── lib/
│   ├── decidim/
│   │   └── meu_componente/
│   │       ├── engine.rb          # Engine Rails
│   │       ├── admin_engine.rb    # Engine do painel admin
│   │       └── component.rb       # Manifest do componente
│   └── decidim-module-meu_componente.rb
├── spec/                          # Testes
├── Gemfile
├── Rakefile
├── decidim-module-meu_componente.gemspec
└── README.md
```

## Registro do Componente

Todo componente precisa registrar-se no Decidim via manifest:

```ruby
# lib/decidim/meu_componente/component.rb
Decidim.register_component(:meu_componente) do |component|
  component.engine = Decidim::MeuComponente::Engine
  component.admin_engine = Decidim::MeuComponente::AdminEngine
  component.icon = "media/images/decidim_meu_componente.svg"

  component.settings(:global) do |settings|
    settings.attribute :announcement, type: :text, translated: true
  end

  component.settings(:step) do |settings|
    settings.attribute :votes_enabled, type: :boolean, default: true
  end
end
```

## Engine Rails

A engine define rotas, controllers e toda a lógica do componente:

```ruby
# lib/decidim/meu_componente/engine.rb
module Decidim
  module MeuComponente
    class Engine < ::Rails::Engine
      isolate_namespace Decidim::MeuComponente

      routes do
        root to: "application#index"
        resources :items, only: [:index, :show, :new, :create]
      end

      initializer "decidim_meu_componente.assets" do |app|
        app.config.assets.precompile += %w[decidim_meu_componente_manifest.js]
      end
    end
  end
end
```

## Instalação no Core

Após criar o componente, adicione-o ao `Gemfile` do `decidim-govbr`:

```ruby
# Gemfile
gem "decidim-module-meu_componente",
    git: "https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo.git",
    glob: "decidim-module-meu_componente/*.gemspec"
```

Depois:

```bash
bundle install
bin/rails decidim_meu_componente:install:migrations
bin/rails db:migrate
```

## Testes

Escreva testes para o componente:

```bash
cd decidim-module-meu_componente
bundle exec rspec
```

Estrutura de testes recomendada:

```
spec/
├── commands/       # Testes de commands
├── controllers/    # Testes de controllers
├── forms/          # Testes de forms
├── models/         # Testes de models
├── permissions/    # Testes de permissões
├── system/         # Testes de sistema (Capybara)
└── factories.rb    # FactoryBot factories
```

## Checklist

- [ ] Scaffold criado com o generator
- [ ] Manifest registrado (`Decidim.register_component`)
- [ ] Engine com rotas e controllers
- [ ] Traduções em `config/locales/pt-BR.yml`
- [ ] Testes escritos e passando
- [ ] Gemspec com metadata correto
- [ ] Adicionado ao Gemfile do core
- [ ] Migrações rodadas e testadas
