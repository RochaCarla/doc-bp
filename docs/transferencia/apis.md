# APIs

Interfaces de programação expostas pelo Brasil Participativo e os contratos com sistemas externos.

| Interface | Tipo | Autenticação | Uso |
|-----------|------|--------------|-----|
| `/api` | GraphQL (Decidim) | Pública para leitura; JWT ou impersonação para ações | Dados abertos, home, integrações |
| `/api/sign_in` e `/api/sign_out` | REST (`decidim-apiauth`) | E-mail e senha → JWT | Clientes que agem como um usuário |
| `/api/home_processes` | JSON | Nenhuma | Página inicial |
| `/external_auth/link` | Página web | Sessão gov.br + JWT do canal | Vínculo de conta WhatsApp/Telegram |
| Callback OP-BP | Webhook de saída | `Authorization: Bearer` | Notificar o vínculo à API OP-BP |
| `/users/auth/govbr/callback` | OpenID Connect | gov.br | Login |

## GraphQL (`/api`)

API padrão do Decidim 0.27, com o explorador **GraphiQL** em `/api/graphiql`. Limites (`config/secrets.yml`):

| Limite | Padrão |
|--------|--------|
| Itens por página (`API_SCHEMA_MAX_PER_PAGE`) | 50 |
| Complexidade máxima (`API_SCHEMA_MAX_COMPLEXITY`) | 5.000 |
| Profundidade máxima (`API_SCHEMA_MAX_DEPTH`) | 15 |

Exemplo:

```bash
curl -s https://brasilparticipativo.presidencia.gov.br/api \
  -H 'Content-Type: application/json' \
  -d '{"query":"{ participatoryProcesses { id slug title { translation(locale: \"pt-BR\") } } }"}'
```

### Extensões do Brasil Participativo

Tipos e filtros acrescentados ou alterados em `lib/decidim/api/`:

| Arquivo | O que faz |
|---------|-----------|
| `participatory_process_type.rb` | Campos extras do processo participativo |
| `participatory_process_step_type.rb` | Etapas do processo |
| `meetings_type.rb`, `meeting_input_filter.rb` | Consulta e filtro de reuniões |
| `surveys_type.rb`, `survey_input_filter.rb` | Consulta e filtro de formulários |
| `comment_type.rb` | Campos de comentário |
| `input_filters/has_publishable_input_filter.rb` | Filtro por publicação |

Antes de evoluir a API, consulte esses arquivos e o explorador GraphiQL para o esquema exato.

### Autenticação por JWT (`decidim-apiauth`)

```bash
# 1. obter o token (vem no cabeçalho Authorization da resposta)
curl -i -X POST https://<host>/api/sign_in \
  -F 'user[email]=pessoa@exemplo.gov.br' -F 'user[password]=***'

# 2. usar o token
curl -s https://<host>/api -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' -d '{"query":"{ session { user { id name } } }"}'
```

`config.force_api_authentication = false` mantém a leitura pública. Os tokens são assinados com `SECRET_KEY_JWT`.

### Impersonação (OP-BP)

A API OP-BP age em nome do participante já vinculado enviando:

| Cabeçalho | Valor |
|-----------|-------|
| `X-API-KEY` | `OP_BP_API_KEY` |
| `X-USER-ID` | ID do usuário no Brasil Participativo |

!!! info "Segurança"
    Restrições pendentes sobre o uso desta chave estão registradas em canal restrito. Veja [Segurança e LGPD](seguranca.md#riscos-conhecidos). Guarde a chave em cofre e troque-a periodicamente.

A tarefa `bundle exec rake botapi:test` simula o fluxo completo (vínculo e chamada à API) em ambiente local.

## `GET /api/home_processes`

JSON usado pela página inicial. Cache de 10 minutos por organização; `Cache-Control: public, max-age=300, stale-while-revalidate=600`.

```json
{
  "participatoryProcessTypes": [
    {
      "id": 1,
      "title": { "translation": "Consultas Públicas" },
      "processes": [
        {
          "id": 123,
          "slug": "meu-processo",
          "title": { "translation": "…" },
          "heroImage": "/rails/active_storage/blobs/…",
          "publishedAt": "2026-01-01T12:00:00Z",
          "startDate": "2026-01-10",
          "endDate": "2026-02-10"
        }
      ]
    }
  ],
  "assemblies": [ { "id": 7, "slug": "…", "title": { "translation": "…" } } ]
}
```

Só entram espaços públicos. Tipos de processo sem processos públicos são omitidos. Os campos exatos de `assemblies` estão em `serialize_assembly` (`app/controllers/api/home_processes_controller.rb`).

## Login externo e callback

Contrato completo (JWT, callback e variáveis) em [Integração OP-BP](../operador/integracao-op-bp.md).

## Dados abertos

A tarefa diária `decidim:open_data:export` gera o pacote de dados abertos do Decidim, disponível em `/open-data/download`.
