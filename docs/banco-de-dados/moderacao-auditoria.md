---
icon: material/shield-search
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-07T13:00:08+00:00. Não edite à mão. -->

# Moderação, auditoria e métricas

Denúncias, moderações, bloqueios de usuários, log de ações administrativas, versões (PaperTrail) e métricas agregadas.

**8 tabelas.** Schema versão `20260405195511`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para outros domínios aparecem na coluna **Referência** das tabelas abaixo.

```mermaid
flowchart LR
    decidim_moderations["moderations"]
    decidim_reports["reports"]
    decidim_user_moderations["user_<br/>moderations"]
    decidim_user_reports["user_reports"]
    decidim_moderations --> decidim_reports
    decidim_user_moderations --> decidim_user_reports
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_action_logs`](#decidim-action-logs) | Log de ações administrativas e de participantes. | 16 | Decidim |
| [`decidim_metrics`](#decidim-metrics) | Métricas agregadas por dia. | 11 | Decidim |
| [`decidim_moderations`](#decidim-moderations) | Moderação de um recurso denunciado (contagem de denúncias, data de ocultação). | 10 | Decidim |
| [`decidim_reports`](#decidim-reports) | Denúncias individuais ligadas a uma moderação. | 8 | Decidim |
| [`decidim_user_blocks`](#decidim-user-blocks) | — | 6 | Decidim |
| [`decidim_user_moderations`](#decidim-user-moderations) | — | 5 | Decidim |
| [`decidim_user_reports`](#decidim-user-reports) | — | 7 | Decidim |
| [`versions`](#versions) | Histórico de versões (PaperTrail). | 8 | Decidim |

### `decidim_action_logs` { #decidim-action-logs }

Log de ações administrativas e de participantes.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `decidim_user_id` | `bigint` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_component_id` | `bigint` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `resource_type` | `string` | não |  |  |  |
| `resource_id` | `bigint` | não |  | polimórfico (tipo em `resource_type`) |  |
| `participatory_space_type` | `string` | sim |  |  |  |
| `participatory_space_id` | `bigint` | sim |  | polimórfico (tipo em `participatory_space_type`) |  |
| `action` | `string` | não |  |  |  |
| `extra` | `jsonb` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `version_id` | `integer` | sim |  |  |  |
| `visibility` | `string` | sim | `"admin-only"` |  |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `decidim_area_id` | `integer` | sim |  | → [`decidim_areas`](componentes-conteudo.md#decidim-areas) |  |

??? note "Índices (10)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_action_logs_on_created_at` | `created_at` |  | btree |
    | `index_decidim_action_logs_on_decidim_area_id` | `decidim_area_id` |  | btree |
    | `index_action_logs_on_component_id` | `decidim_component_id` |  | btree |
    | `index_action_logs_on_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_action_logs_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `index_action_logs_on_user_id` | `decidim_user_id` |  | btree |
    | `index_action_logs_on_space_type_and_id` | `participatory_space_type`, `participatory_space_id` |  | btree |
    | `index_action_logs_on_resource_type_and_id` | `resource_type`, `resource_id` |  | btree |
    | `index_decidim_action_logs_on_version_id` | `version_id` |  | btree |
    | `index_decidim_action_logs_on_visibility` | `visibility` |  | btree |

### `decidim_metrics` { #decidim-metrics }

Métricas agregadas por dia.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `day` | `date` | não |  |  |  |
| `metric_type` | `string` | não |  |  |  |
| `cumulative` | `integer` | não |  |  |  |
| `quantity` | `integer` | não |  |  |  |
| `decidim_organization_id` | `bigint` | não |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `participatory_space_type` | `string` | sim |  |  |  |
| `participatory_space_id` | `bigint` | sim |  | polimórfico (tipo em `participatory_space_type`) |  |
| `related_object_type` | `string` | sim |  |  |  |
| `related_object_id` | `bigint` | sim |  | polimórfico (tipo em `related_object_type`) |  |
| `decidim_category_id` | `bigint` | sim |  | → [`decidim_categories`](componentes-conteudo.md#decidim-categories) |  |

??? note "Índices (7)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `idx_metric_by_day_type_org_space_object_category` | `day`, `metric_type`, `decidim_organization_id`, `participatory_space_type`, `participatory_space_id`, `related_object_type`, `related_object_id`, `decidim_category_id` | sim | btree |
    | `index_decidim_metrics_on_day` | `day` |  | btree |
    | `index_decidim_metrics_on_decidim_category_id` | `decidim_category_id` |  | btree |
    | `index_decidim_metrics_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_metrics_on_metric_type` | `metric_type` |  | btree |
    | `index_metric_on_participatory_space_id_and_type` | `participatory_space_type`, `participatory_space_id` |  | btree |
    | `index_metric_on_related_object_id_and_type` | `related_object_type`, `related_object_id` |  | btree |

### `decidim_moderations` { #decidim-moderations }

Moderação de um recurso denunciado (contagem de denúncias, data de ocultação).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_participatory_space_id` | `integer` | não |  | polimórfico (tipo em `decidim_participatory_space_type`) | — |
| `decidim_reportable_type` | `string` | não |  |  |  |
| `decidim_reportable_id` | `integer` | não |  | polimórfico (tipo em `decidim_reportable_type`) |  |
| `report_count` | `integer` | não | `0` | contador em cache |  |
| `hidden_at` | `datetime` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `decidim_participatory_space_type` | `string` | não |  |  |  |
| `reported_content` | `text` | sim |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_moderations_participatory_space` | `decidim_participatory_space_id`, `decidim_participatory_space_type` |  | btree |
    | `decidim_moderations_reportable` | `decidim_reportable_type`, `decidim_reportable_id` | sim | btree |
    | `decidim_moderations_hidden_at` | `hidden_at` |  | btree |
    | `decidim_moderations_report_count` | `report_count` |  | btree |

### `decidim_reports` { #decidim-reports }

Denúncias individuais ligadas a uma moderação.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_moderation_id` | `integer` | não |  | → [`decidim_moderations`](moderacao-auditoria.md#decidim-moderations) |  |
| `decidim_user_id` | `integer` | não |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `reason` | `string` | não |  |  |  |
| `details` | `text` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `locale` | `string` | sim |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_reports_moderation_user_unique` | `decidim_moderation_id`, `decidim_user_id` | sim | btree |
    | `decidim_reports_moderation` | `decidim_moderation_id` |  | btree |
    | `decidim_reports_user` | `decidim_user_id` |  | btree |

### `decidim_user_blocks` { #decidim-user-blocks }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_user_id` | `bigint` | sim |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `blocking_user_id` | `integer` | sim |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `justification` | `text` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_user_blocks_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_user_moderations` { #decidim-user-moderations }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_user_id` | `bigint` | sim |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `report_count` | `integer` | não | `0` | contador em cache |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_user_moderations_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_user_reports` { #decidim-user-reports }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `user_moderation_id` | `integer` | sim |  | FK → [`decidim_user_moderations`](moderacao-auditoria.md#decidim-user-moderations) |  |
| `user_id` | `integer` | não |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `reason` | `string` | sim |  |  |  |
| `details` | `text` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

### `versions` { #versions }

Histórico de versões (PaperTrail).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `item_type` | `string` | não |  |  |  |
| `item_id` | `integer` | não |  | polimórfico (tipo em `item_type`) |  |
| `event` | `string` | não |  |  |  |
| `whodunnit` | `string` | sim |  |  |  |
| `object` | `jsonb` | sim |  |  |  |
| `created_at` | `datetime` | sim |  |  |  |
| `object_changes` | `text` | sim |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_versions_on_item_id_and_item_type` | `item_id`, `item_type` |  | btree |
    | `index_versions_on_item_type_and_item_id` | `item_type`, `item_id` |  | btree |

