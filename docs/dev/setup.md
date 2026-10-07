# Setup Local

Como subir o ambiente de desenvolvimento do `decidim-govbr`. O caminho recomendado é o Docker Compose, que é o mesmo descrito no README do repositório.

## Versões de referência

| Ferramenta | Versão | Fonte |
|-----------|--------|-------|
| Ruby | 3.0.4 | `.ruby-version` |
| Decidim | 0.27.2 | `Gemfile` |
| PostgreSQL | 13.2 | `docker-compose.yml` |
| Redis | 6.0.12 (duas instâncias: fila e cache) | `docker-compose.yml` |
| Node.js + Yarn | compatível com Webpacker 6 | `package.json` |
| Pandoc | qualquer versão recente | `Dockerfile` (importação de documentos) |

## Opção 1: Docker Compose (recomendado)

### 1. Clone o repositório

```bash
git clone https://gitlab.com/lappis-unb/decidimbr/decidim-govbr.git
cd decidim-govbr
```

### 2. Suba os serviços

```bash
docker compose up
```

O `docker-compose.yml` sobe quatro containers:

| Container | Porta | Função |
|-----------|-------|--------|
| `decidim-db` | 5432 | PostgreSQL |
| `redis-queue` | 6379 | Fila do Sidekiq |
| `redis-cache` | 6380 | Cache do Rails |
| `decidim-service` | 3000 e 1080 | Aplicação e Mailcatcher |

O container da aplicação usa a imagem base `lappis/decidim-govbr:v1-release`, carrega as variáveis de `.env.dev` e executa `start.sh`, que:

1. instala dependências (`yarn`, `bundle install`);
2. compila os assets (`rails webpacker:compile`);
3. cria e migra o banco; na primeira execução também roda `db:seed`;
4. inicia Mailcatcher, Sidekiq, webpack-dev-server e o Rails na porta 3000.

!!! warning "Só para desenvolvimento"
    Esses containers não devem ser usados em produção.

### 3. Crie a primeira organização

O seed cria um **administrador de sistema** com as credenciais de `.env.dev` (`ADMIN_EMAIL` e `ADMIN_PASSWORD`; sem elas, o e-mail padrão é `bpadmin@example.com`).

1. Acesse [http://localhost:3000/system](http://localhost:3000/system) e faça login.
2. Crie a organização:
    - **Host**: `localhost`
    - **Idiomas**: habilite Português e defina como padrão
    - **Modo de registro**: permitir que participantes se registrem e façam login
    - **Autorizações disponíveis**: selecione todas
3. Abra o Mailcatcher em [http://localhost:1080](http://localhost:1080) e aceite o convite do administrador da organização.
4. Defina apelido e senha, aceite os termos e acesse `/admin`.

!!! tip "Feature flags da organização"
    O formulário de edição da organização em `/system` também traz as flags do Brasil Participativo, como a remoção de identidades gov.br duplicadas. Veja [Administração](../operador/administracao.md#painel-system).

## Opção 2: sem Docker

Use quando quiser rodar Ruby localmente e manter só os serviços em containers.

```bash
# serviços (PostgreSQL e Redis)
docker compose up -d postgres redis-queue redis-cache

# dependências
bundle install
yarn install

# banco
bin/rails db:create db:migrate db:seed
```

Suba os processos do `Procfile` com Foreman:

```bash
mailcatcher
foreman start
```

| Processo | Comando |
|----------|---------|
| `web` | `bundle exec puma -p 3000 -C config/puma.rb` |
| `webpack` | `bin/webpack-dev-server` |
| `worker` | `bundle exec sidekiq -t 25 -C config/sidekiq.yml` |

Em desenvolvimento, os e-mails também ficam disponíveis em `/letter_opener`.

## Variáveis de ambiente

Há dois arquivos de exemplo no repositório:

- **`.env.dev`**: usado pelo Docker Compose. Define banco (`DATABASE_*`), `DEFAULT_HOST`, `DEFAULT_PROTOCOL`, `ALLOW_HOSTS`, credenciais do admin de sistema, `REDIS_URL` e `REDIS_CACHE_URL`.
- **`.env.example`**: variáveis do bot do Telegram e da [integração OP-BP](../operador/integracao-op-bp.md).

`ALLOW_HOSTS` é obrigatória: o ambiente de desenvolvimento a adiciona a `config.hosts`. A referência completa está em [Configuração](../operador/configuracao.md).

## Testes

O CI roda as duas suítes:

```bash
bundle exec rails test
bundle exec rspec
```

Testes de sistema precisam do Chrome. No CI ele é instalado por `bin/setup_chrome`.

Para rodar um arquivo:

```bash
bundle exec rspec spec/services/external_auth_service_spec.rb
```

## Lint

```bash
bundle exec rubocop
```

## Problemas comuns

??? question "`KeyError: key not found: \"ALLOW_HOSTS\"`"
    Defina `ALLOW_HOSTS` no `.env` (por exemplo, `ALLOW_HOSTS=localhost`).

??? question "A organização não abre em localhost:3000"
    O campo **Host** da organização em `/system` precisa ser exatamente o host usado no navegador, incluindo subdomínio.

??? question "Erro de permissão no PostgreSQL (sem Docker)"
    ```bash
    sudo -u postgres createuser -s $(whoami)
    ```

??? question "Assets não compilam"
    ```bash
    yarn install
    bin/rails webpacker:clobber
    bin/rails webpacker:compile
    ```

??? question "Gems nativas não instalam"
    ```bash
    # macOS
    brew install libpq imagemagick pandoc

    # Ubuntu/Debian
    sudo apt-get install libpq-dev libmagickwand-dev pandoc
    ```
