# Configuração

Referência das variáveis de ambiente lidas pelo `decidim-govbr`. Os valores chegam à aplicação por `config/secrets.yml` (via `Decidim::Env`) ou por `ENV` direto no código.

## Aplicação e hosts

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `SECRET_KEY_BASE` | Chave secreta do Rails (produção) | — |
| `SECRET_KEY_JWT` | Chave JWT do Decidim (produção) | — |
| `RAILS_ENV` | Ambiente | — |
| `ALLOW_HOSTS` | Hosts aceitos pelo Rails, separados por espaço. **Obrigatória** em desenvolvimento e produção | — |
| `DEFAULT_HOST` / `DEFAULT_PROTOCOL` | Host e protocolo das URLs geradas (e-mails, jobs) | — |
| `RAILS_SERVE_STATIC_FILES` | Servir assets pelo Rails | — |
| `RAILS_LOG_LEVEL`, `RAILS_LOG_TO_STDOUT`, `RAILS_LOG_TO_JSON` | Logs | — |
| `RAILS_MAX_THREADS`, `WEB_CONCURRENCY`, `PORT` | Puma | — |
| `ADMIN_USERNAME` / `ADMIN_PASSWORD` | Basic Auth do painel `/sidekiq` em produção. Em desenvolvimento, `ADMIN_EMAIL`/`ADMIN_PASSWORD` definem o admin de sistema do seed | — |

## Decidim

Principais variáveis de `secrets.yml`:

| Variável | Descrição | Padrão |
|----------|-----------|--------|
| `DECIDIM_APPLICATION_NAME` | Nome da aplicação | `My Application Name` |
| `DECIDIM_MAILER_SENDER` | Remetente dos e-mails | `change-me@example.org` |
| `DECIDIM_AVAILABLE_LOCALES` | Idiomas disponíveis | lista ampla, inclui `pt-BR` |
| `DECIDIM_DEFAULT_LOCALE` | Idioma padrão | `en` (defina `pt-BR`) |
| `DECIDIM_FORCE_SSL` | Forçar HTTPS | `auto` |
| `DECIDIM_CURRENCY_UNIT` | Moeda | `€` (defina `R$`) |
| `DECIDIM_ENABLE_HTML_HEADER_SNIPPETS` | Permitir snippets no `<head>` | desligado |
| `DECIDIM_MAXIMUM_ATTACHMENT_SIZE` | Tamanho máximo de anexo (MB) | `10` |
| `DECIDIM_THROTTLING_MAX_REQUESTS` / `DECIDIM_THROTTLING_PERIOD` | Limite de requisições | `100` / `1` min |
| `DECIDIM_EXPIRE_SESSION_AFTER` | Expiração de sessão (min) | `30` |
| `DECIDIM_SYSTEM_ACCESSLIST_IPS` | IPs permitidos em `/system` | vazio |
| `DECIDIM_ADMIN_PASSWORD_MIN_LENGTH` | Tamanho mínimo da senha de admin | `15` |
| `DECIDIM_ADMIN_PASSWORD_EXPIRATION_DAYS` | Expiração da senha de admin | `90` |
| `DECIDIM_SERVICE_WORKER_ENABLED` | Service worker | ligado fora de desenvolvimento |
| `API_SCHEMA_MAX_PER_PAGE`, `API_SCHEMA_MAX_COMPLEXITY`, `API_SCHEMA_MAX_DEPTH` | Limites da API GraphQL | `50`, `5000`, `15` |

Há variáveis equivalentes por módulo (`PROPOSALS_*`, `MEETINGS_*`, `BUDGETS_*`, `INITIATIVES_*`, `CONSULTATIONS_*`). Consulte `config/secrets.yml`.

## Banco de dados e Redis

| Variável | Descrição |
|----------|-----------|
| `DATABASE_URL` | URL de conexão PostgreSQL |
| `DATABASE_HOST`, `DATABASE_PORT`, `DATABASE_USERNAME`, `DATABASE_PASSWORD` | Alternativa a `DATABASE_URL` |
| `REDIS_URL` | Redis da fila do Sidekiq |
| `REDIS_CACHE_URL` | Redis do cache do Rails (aceita lista separada por vírgula) |
| `SIDEKIQ_CONCURRENCY` | Concorrência do Sidekiq |

## E-mail (SMTP, produção)

| Variável | Padrão |
|----------|--------|
| `SMTP_ADDRESS` | — |
| `SMTP_PORT` | `587` |
| `SMTP_USERNAME` / `SMTP_PASSWORD` | — |
| `SMTP_DOMAIN` | — |
| `SMTP_STARTTLS_AUTO` | desligado |
| `SMTP_AUTHENTICATION` | `plain` |

## Autenticação

### gov.br (OpenID Connect)

| Variável | Descrição |
|----------|-----------|
| `OMNIAUTH_GOVBR_CLIENT_ID` | Client ID. Habilita o provedor quando presente |
| `OMNIAUTH_GOVBR_CLIENT_SECRET` / `OMNIAUTH_GOVBR_SECRET_KEY` | Segredo do cliente |
| `OMNIAUTH_GOVBR_HOST` | Host do provedor (issuer e `jwks_uri` derivam dele) |
| `OMNIAUTH_GOVBR_REDIRECT_URI` | URL de retorno |

Outros provedores ficam habilitados quando suas variáveis existem: `OMNIAUTH_FACEBOOK_*`, `OMNIAUTH_TWITTER_*`, `OMNIAUTH_GOOGLE_*`.

### Integração OP-BP

`OP_BP_JWT_SECRET`, `OP_BP_API_KEY`, `OP_BP_CALLBACK_API_KEY`, `OP_BP_CALLBACK_ALLOWED_HOSTS`, `OP_BP_FALLBACK_WHATSAPP_URL` e `API_BASE_URL`. Veja [Integração OP-BP](integracao-op-bp.md).

### Bot do Telegram

| Variável | Descrição |
|----------|-----------|
| `TELEGRAM_TOKEN` | Token do bot (obtido com o @BotFather) |
| `COMPONENT_ID` | ID do componente de propostas usado pelo bot |

## Storage de arquivos

| Variável | Descrição |
|----------|-----------|
| `STORAGE_PROVIDER` | `local` (padrão), `s3`, `azure` ou `gcs` |
| `STORAGE_CDN_HOST` | Host de CDN para os arquivos |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`, `AWS_BUCKET`, `AWS_ENDPOINT`, `AWS_FORCE_PATH_STYLE` | S3 ou compatível |
| `AZURE_STORAGE_ACCOUNT_NAME`, `AZURE_STORAGE_ACCESS_KEY`, `AZURE_CONTAINER` | Azure |
| `GCS_PROJECT`, `GCS_BUCKET`, `GCS_*` (credenciais da service account) | Google Cloud Storage |

## Integrações

| Variável | Descrição |
|----------|-----------|
| `EJ_JWT_SECRET` / `EJ_SECRET_KEY` | Empurrando Juntas (`decidim-ej`) |
| `HOST_AIRFLOW`, `USER_AIRFLOW`, `PASSWORD_AIRFLOW` | Disparo de relatórios no Airflow |
| `MAPS_PROVIDER`, `MAPS_API_KEY`, `MAPS_DYNAMIC_URL`, `MAPS_STATIC_URL`, `MAPS_GEOCODING_HOST`, `MAPS_ATTRIBUTION`, `MAPS_EXTRA_VARS` | Mapas e geocodificação |
| `ETHERPAD_SERVER`, `ETHERPAD_API_KEY` | Etherpad (reuniões) |
| `VAPID_PUBLIC_KEY`, `VAPID_PRIVATE_KEY` | Notificações push |

## Configurações por organização

Algumas configurações não são variáveis de ambiente, mas campos da organização editados em `/system`:

| Campo | Descrição | Padrão |
|-------|-----------|--------|
| `prune_duplicated_govbr_identities` | Ativa a remoção de identidades gov.br duplicadas | `false` |
| `prune_duplicated_govbr_identities_users_quantity` | Usuários processados por execução (a cada 5 min) | `5` |

!!! warning "Segurança"
    Nunca versione segredos no Git. Use o gerenciador de segredos do ambiente de hospedagem.
