# Setup Local

Guia para configurar o ambiente de desenvolvimento do Brasil Participativo localmente.

## Pré-requisitos

| Ferramenta | Versão mínima | Observação |
|-----------|---------------|------------|
| Ruby | 3.1+ | Recomenda-se usar `rbenv` ou `asdf` |
| Node.js | 18+ | Para compilar assets (Webpacker/Shakapacker) |
| PostgreSQL | 14+ | Banco de dados principal |
| Redis | 6+ | Cache e filas (Sidekiq) |
| Git | 2.30+ | Controle de versão |
| ImageMagick | 7+ | Processamento de imagens |

## Clone do Repositório

```bash
git clone https://gitlab.com/lappis-unb/decidimbr/decidim-govbr.git
cd decidim-govbr
```

## Instalação de Dependências

### Ruby (gems)

```bash
bundle install
```

### Node.js (pacotes)

```bash
npm install
```

## Banco de Dados

### Criação e migração

```bash
bin/rails db:create
bin/rails db:migrate
bin/rails db:seed
```

!!! tip "Seeds"
    O `db:seed` cria dados iniciais para desenvolvimento, incluindo um usuário administrador e espaços participativos de exemplo. Verifique o arquivo `db/seeds.rb` para detalhes.

## Servidor de Desenvolvimento

```bash
bin/rails s
```

A aplicação estará disponível em [http://localhost:3000](http://localhost:3000).

### Sidekiq (processamento em background)

Em um terminal separado:

```bash
bundle exec sidekiq
```

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (ou copie o `.env.example` se existir):

```bash
DATABASE_URL=postgres://localhost/decidim_govbr_development
REDIS_URL=redis://localhost:6379/0
SECRET_KEY_BASE=<gere com `bin/rails secret`>
```

!!! note "Configuração de integração com EJ"
    Para testar a integração com o Empurrando Juntas localmente, configure a URL da API do EJ nas variáveis de ambiente. Consulte a documentação do componente [decidim-ej](../componentes/ej.md).

## Testes

```bash
bundle exec rspec
```

Para rodar testes de um componente específico:

```bash
bundle exec rspec spec/path/to/spec_file.rb
```

## Problemas Comuns

??? question "Erro de permissão no PostgreSQL"
    Verifique se seu usuário tem permissão para criar bancos de dados:
    ```bash
    sudo -u postgres createuser -s $(whoami)
    ```

??? question "Assets não compilam"
    Limpe o cache e recompile:
    ```bash
    bin/rails assets:clobber
    bin/rails assets:precompile
    ```

??? question "Gems nativas não instalam"
    Instale as dependências de sistema necessárias:
    ```bash
    # macOS
    brew install libpq imagemagick

    # Ubuntu/Debian
    sudo apt-get install libpq-dev libmagickwand-dev
    ```
