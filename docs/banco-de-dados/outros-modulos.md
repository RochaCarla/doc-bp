---
title: Orçamentos, debates, blog e outros módulos
icon: material/view-grid-plus
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-07T13:48:25+00:00. Não edite à mão. -->

# Orçamentos, debates, blog e outros módulos

Demais módulos nativos do Decidim: orçamentos, prestação de contas, debates, blog, páginas e sorteios.

**11 tabelas.** Schema versão `20260405195511`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Cada seta vai da tabela referenciada para a tabela que guarda a referência. Referências para outros domínios aparecem na coluna **Referência** das tabelas abaixo.

**A partir de `decidim_budgets_budgets`**

```mermaid
flowchart TB
    decidim_budgets_budgets["budgets_<br/>budgets"]
    decidim_budgets_line_items["budgets_line_<br/>items"]
    decidim_budgets_orders["budgets_<br/>orders"]
    decidim_budgets_projects["budgets_<br/>projects"]
    decidim_budgets_budgets --> decidim_budgets_orders
    decidim_budgets_budgets --> decidim_budgets_projects
    decidim_budgets_orders --> decidim_budgets_line_items
    decidim_budgets_projects --> decidim_budgets_line_items
```

**A partir de `decidim_accountability_statuses`**

```mermaid
flowchart TB
    decidim_accountability_results["accountability_<br/>results"]
    decidim_accountability_statuses["accountability_<br/>statuses"]
    decidim_accountability_timeline_entries["accountability_<br/>timeline_<br/>entries"]
    decidim_accountability_results --> decidim_accountability_timeline_entries
    decidim_accountability_statuses --> decidim_accountability_results
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_accountability_results`](#decidim-accountability-results) | Resultados acompanhados na prestação de contas. | 17 | Decidim |
| [`decidim_accountability_statuses`](#decidim-accountability-statuses) | — | 8 | Decidim |
| [`decidim_accountability_timeline_entries`](#decidim-accountability-timeline-entries) | — | 7 | Decidim |
| [`decidim_blogs_posts`](#decidim-blogs-posts) | Posts do blog (notícias). | 13 | Decidim |
| [`decidim_budgets_budgets`](#decidim-budgets-budgets) | Orçamentos de um componente. | 9 | Decidim |
| [`decidim_budgets_line_items`](#decidim-budgets-line-items) | — | 3 | Decidim |
| [`decidim_budgets_orders`](#decidim-budgets-orders) | Votos (carrinhos) de participantes num orçamento. | 6 | Decidim |
| [`decidim_budgets_projects`](#decidim-budgets-projects) | Projetos votáveis de um orçamento. | 15 | Decidim |
| [`decidim_debates_debates`](#decidim-debates-debates) | Debates. | 25 | Decidim |
| [`decidim_pages_pages`](#decidim-pages-pages) | Conteúdo do componente Páginas. | 6 | Decidim |
| [`decidim_sortitions_sortitions`](#decidim-sortitions-sortitions) | Sorteios de propostas. | 20 | Decidim |

### `decidim_accountability_results` { #decidim-accountability-results }

Resultados acompanhados na prestação de contas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `reference` | `string` | sim |  |  |  |
| `start_date` | `date` | sim |  |  |  |
| `end_date` | `date` | sim |  |  |  |
| `progress` | `decimal` | sim |  |  |  |
| `parent_id` | `integer` | sim |  | → [`decidim_accountability_results`](outros-modulos.md#decidim-accountability-results) |  |
| `decidim_accountability_status_id` | `integer` | sim |  | → [`decidim_accountability_statuses`](outros-modulos.md#decidim-accountability-statuses) |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `children_count` | `integer` | sim | `0` | contador em cache |  |
| `weight` | `float` | sim | `1.0` |  |  |
| `external_id` | `string` | sim |  |  |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_accountability_results_on_status_id` | `decidim_accountability_status_id` |  | btree |
    | `index_decidim_accountability_results_on_decidim_component_id` | `decidim_component_id` |  | btree |
    | `index_decidim_accountability_results_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `index_decidim_accountability_results_on_external_id` | `external_id` |  | btree |
    | `decidim_accountability_results_on_parent_id` | `parent_id` |  | btree |

### `decidim_accountability_statuses` { #decidim-accountability-statuses }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `key` | `string` | sim |  |  |  |
| `name` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `progress` | `integer` | sim |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_accountability_statuses_on_decidim_component_id` | `decidim_component_id` |  | btree |

### `decidim_accountability_timeline_entries` { #decidim-accountability-timeline-entries }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `entry_date` | `date` | sim |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_accountability_result_id` | `integer` | sim |  | → [`decidim_accountability_results`](outros-modulos.md#decidim-accountability-results) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_accountability_timeline_entries_on_results_id` | `decidim_accountability_result_id` |  | btree |
    | `index_decidim_accountability_timeline_entries_on_entry_date` | `entry_date` |  | btree |

### `decidim_blogs_posts` { #decidim-blogs-posts }

Posts do blog (notícias).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `decidim_author_id` | `integer` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `decidim_user_group_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `endorsements_count` | `integer` | não | `0` | contador em cache |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `subtitle` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20231004032051_add_subtitle_to_blog_post.rb "20231004032051_add_subtitle_to_blog_post.rb") |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_blogs_posts_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `index_decidim_blogs_posts_on_decidim_component_id` | `decidim_component_id` |  | btree |
    | `index_decidim_blogs_posts_on_decidim_user_group_id` | `decidim_user_group_id` |  | btree |

### `decidim_budgets_budgets` { #decidim-budgets-budgets }

Orçamentos de um componente.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `weight` | `integer` | não | `0` |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `total_budget` | `integer` | sim | `0` |  |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `decidim_scope_id` | `bigint` | sim |  | FK → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_budgets_budgets_on_decidim_component_id` | `decidim_component_id` |  | btree |
    | `index_decidim_budgets_budgets_on_decidim_scope_id` | `decidim_scope_id` |  | btree |

### `decidim_budgets_line_items` { #decidim-budgets-line-items }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_order_id` | `integer` | sim |  | → [`decidim_budgets_orders`](outros-modulos.md#decidim-budgets-orders) |  |
| `decidim_project_id` | `integer` | sim |  | → [`decidim_budgets_projects`](outros-modulos.md#decidim-budgets-projects) |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_budgets_line_items_order_project_unique` | `decidim_order_id`, `decidim_project_id` | sim | btree |
    | `index_decidim_budgets_line_items_on_decidim_order_id` | `decidim_order_id` |  | btree |
    | `index_decidim_budgets_line_items_on_decidim_project_id` | `decidim_project_id` |  | btree |

### `decidim_budgets_orders` { #decidim-budgets-orders }

Votos (carrinhos) de participantes num orçamento.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_user_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `checked_out_at` | `datetime` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `decidim_budgets_budget_id` | `bigint` | sim |  | FK → [`decidim_budgets_budgets`](outros-modulos.md#decidim-budgets-budgets) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_budgets_orders_on_decidim_budgets_budget_id` | `decidim_budgets_budget_id` |  | btree |
    | `index_decidim_budgets_orders_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_budgets_projects` { #decidim-budgets-projects }

Projetos votáveis de um orçamento.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `budget_amount` | `bigint` | não |  |  |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `reference` | `string` | sim |  |  |  |
| `decidim_budgets_budget_id` | `bigint` | sim |  | FK → [`decidim_budgets_budgets`](outros-modulos.md#decidim-budgets-budgets) |  |
| `selected_at` | `date` | sim |  |  |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `address` | `text` | sim |  |  |  |
| `latitude` | `float` | sim |  |  |  |
| `longitude` | `float` | sim |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_budgets_projects_on_decidim_budgets_budget_id` | `decidim_budgets_budget_id` |  | btree |
    | `index_decidim_budgets_projects_on_decidim_scope_id` | `decidim_scope_id` |  | btree |

### `decidim_debates_debates` { #decidim-debates-debates }

Debates.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `instructions` | `jsonb` | sim |  |  |  |
| `start_time` | `datetime` | sim |  |  |  |
| `end_time` | `datetime` | sim |  |  |  |
| `image` | `string` | sim |  |  |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `information_updates` | `jsonb` | sim |  |  |  |
| `decidim_author_id` | `integer` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `reference` | `string` | sim |  |  |  |
| `decidim_user_group_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `closed_at` | `datetime` | sim |  |  |  |
| `conclusions` | `jsonb` | sim |  |  |  |
| `endorsements_count` | `integer` | não | `0` | contador em cache |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |
| `last_comment_at` | `datetime` | sim |  |  |  |
| `last_comment_by_id` | `integer` | sim |  | polimórfico (tipo em `last_comment_by_type`) |  |
| `last_comment_by_type` | `string` | sim |  |  |  |
| `decidim_scope_id` | `bigint` | sim |  | FK → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `comments_enabled` | `boolean` | sim | `true` |  |  |

??? note "Índices (6)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_debates_debates_on_closed_at` | `closed_at` |  | btree |
    | `index_decidim_debates_debates_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `index_decidim_debates_debates_on_decidim_component_id` | `decidim_component_id` |  | btree |
    | `index_decidim_debates_debates_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `index_decidim_debates_debates_on_decidim_user_group_id` | `decidim_user_group_id` |  | btree |
    | `idx_decidim_debates_debates_on_endorsemnts_count` | `endorsements_count` |  | btree |

### `decidim_pages_pages` { #decidim-pages-pages }

Conteúdo do componente Páginas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `description` | `string` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240606181840_add_description_to_pages.rb "20240606181840_add_description_to_pages.rb") |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_pages_pages_on_decidim_component_id` | `decidim_component_id` |  | btree |

### `decidim_sortitions_sortitions` { #decidim-sortitions-sortitions }

Sorteios de propostas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_component_id` | `bigint` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `decidim_proposals_component_id` | `integer` | sim |  |  |  |
| `dice` | `integer` | não |  |  |  |
| `target_items` | `integer` | não |  |  |  |
| `request_timestamp` | `datetime` | não |  |  |  |
| `selected_proposals` | `jsonb` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `witnesses` | `jsonb` | sim |  |  |  |
| `additional_info` | `jsonb` | sim |  |  |  |
| `decidim_author_id` | `bigint` | não |  | polimórfico (tipo em `decidim_author_type`) |  |
| `reference` | `string` | sim |  |  |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `cancel_reason` | `jsonb` | sim |  |  |  |
| `cancelled_on` | `datetime` | sim |  |  |  |
| `cancelled_by_user_id` | `integer` | sim |  |  |  |
| `candidate_proposals` | `jsonb` | sim |  |  |  |
| `decidim_author_type` | `string` | não |  |  |  |
| `comments_count` | `integer` | não | `0` | contador em cache |  |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_sortitions_sortitions_on_cancelled_by_user_id` | `cancelled_by_user_id` |  | btree |
    | `index_decidim_sortitions_sortitions_on_decidim_author` | `decidim_author_id`, `decidim_author_type` |  | btree |
    | `index_decidim_sortitions_sortitions_on_decidim_author_id` | `decidim_author_id` |  | btree |
    | `index_sortitions__on_feature` | `decidim_component_id` |  | btree |
    | `index_sortitions__on_proposals_feature` | `decidim_proposals_component_id` |  | btree |

