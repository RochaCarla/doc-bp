# Configuração

Referência de variáveis de ambiente e configurações da plataforma.

## Variáveis de Ambiente

### Banco de Dados

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `DATABASE_URL` | URL de conexão PostgreSQL | `postgres://user:pass@host:5432/decidim_prod` |
| `DATABASE_POOL` | Tamanho do pool de conexões | `10` |

### Redis

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `REDIS_URL` | URL de conexão Redis | `redis://host:6379/0` |

### Aplicação

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SECRET_KEY_BASE` | Chave secreta Rails | Gerada com `bin/rails secret` |
| `RAILS_ENV` | Ambiente de execução | `production` |
| `RAILS_SERVE_STATIC_FILES` | Servir assets diretamente | `true` |
| `RAILS_LOG_LEVEL` | Nível de log | `info` |
| `DECIDIM_HOST` | Domínio da plataforma | `brasilparticipativo.presidencia.gov.br` |
| `DECIDIM_FORCE_SSL` | Forçar HTTPS | `true` |

### E-mail (SMTP)

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `SMTP_ADDRESS` | Servidor SMTP | `smtp.gov.br` |
| `SMTP_PORT` | Porta SMTP | `587` |
| `SMTP_USERNAME` | Usuário SMTP | `noreply@gov.br` |
| `SMTP_PASSWORD` | Senha SMTP | `***` |
| `SMTP_DOMAIN` | Domínio do remetente | `gov.br` |
| `SMTP_FROM` | Endereço de remetente | `noreply@brasilparticipativo.gov.br` |

### Integração EJ (Empurrando Juntas)

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `EJ_API_URL` | URL base da API do EJ | `https://ej.brasilparticipativo.gov.br/api` |

### Storage (Uploads)

| Variável | Descrição | Exemplo |
|----------|-----------|---------|
| `STORAGE_PROVIDER` | Provider de storage | `local`, `s3`, `gcs` |
| `S3_BUCKET` | Nome do bucket S3 | `bp-uploads` |
| `S3_REGION` | Região AWS | `sa-east-1` |
| `S3_ACCESS_KEY_ID` | Chave de acesso | `***` |
| `S3_SECRET_ACCESS_KEY` | Chave secreta | `***` |

## Configuração do Decidim

O Decidim é configurado via initializer em `config/initializers/decidim.rb`:

```ruby
Decidim.configure do |config|
  config.application_name = "Brasil Participativo"
  config.mailer_sender = ENV.fetch("SMTP_FROM", "noreply@brasilparticipativo.gov.br")
  config.available_locales = [:pt, :en, :es]
  config.default_locale = :pt
  config.force_ssl = ENV.fetch("DECIDIM_FORCE_SSL", "true") == "true"
  config.enable_html_header_snippets = false
  config.currency_unit = "R$"
  config.track_newsletter_links = true
end
```

## Kubernetes — ConfigMap e Secrets

### ConfigMap (valores não-sensíveis)

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: brasil-participativo-config
data:
  RAILS_ENV: "production"
  RAILS_SERVE_STATIC_FILES: "true"
  RAILS_LOG_LEVEL: "info"
  DECIDIM_HOST: "brasilparticipativo.presidencia.gov.br"
  DECIDIM_FORCE_SSL: "true"
```

### Secret (valores sensíveis)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: brasil-participativo-secrets
type: Opaque
stringData:
  DATABASE_URL: "postgres://user:pass@host:5432/decidim_prod"
  REDIS_URL: "redis://host:6379/0"
  SECRET_KEY_BASE: "<valor gerado>"
  SMTP_PASSWORD: "<senha>"
```

!!! warning "Segurança"
    Nunca versione secrets no Git. Use ferramentas como Sealed Secrets, External Secrets Operator ou Vault para gerenciar credenciais no cluster.
