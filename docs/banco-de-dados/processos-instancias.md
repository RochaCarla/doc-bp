---
icon: material/sitemap
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-07T12:08:06+00:00. Não edite à mão. -->

# Processos participativos e instâncias

Espaços participativos usados em produção: processos (consultas, conferências, planos, audiências) e assembleias, chamadas de instâncias (conselhos, colegiados, fóruns).

**13 tabelas.** Schema versão `20260405195511`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Relações entre as tabelas deste domínio. Referências para outros domínios aparecem nas tabelas abaixo.

```mermaid
erDiagram
    decidim_assemblies ||--o{ decidim_assembly_members : ""
    decidim_assemblies ||--o{ decidim_assembly_user_roles : ""
    decidim_assemblies_types ||--o{ decidim_assemblies : ""
    decidim_participatory_process_groups ||--o{ decidim_participatory_processes : ""
    decidim_participatory_process_types ||--o{ decidim_participatory_processes : ""
    decidim_participatory_processes ||--o{ decidim_participatory_process_steps : ""
    decidim_participatory_processes ||--o{ decidim_participatory_process_user_roles : ""
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_assemblies`](#decidim-assemblies) | Assembleias, chamadas de instâncias na interface. `parent_id` forma a hierarquia de sub-instâncias. | 55 | Decidim |
| [`decidim_assemblies_settings`](#decidim-assemblies-settings) | — | 3 | Decidim |
| [`decidim_assemblies_types`](#decidim-assemblies-types) | Tipos de assembleia. | 5 | Decidim |
| [`decidim_assembly_members`](#decidim-assembly-members) | Membros de uma assembleia. | 14 | Decidim |
| [`decidim_assembly_user_roles`](#decidim-assembly-user-roles) | Papéis de usuários em assembleias. | 6 | Decidim |
| [`decidim_epng_scope_memberships`](#decidim-epng-scope-memberships) | — | 6 | `decidim-enhanced_process_groups_and_scopes` (LabLivre) |
| [`decidim_participatory_process_groups`](#decidim-participatory-process-groups) | Grupos de processos. | 19 | Decidim |
| [`decidim_participatory_process_steps`](#decidim-participatory-process-steps) | Etapas (fases) de cada processo. | 12 | Decidim |
| [`decidim_participatory_process_types`](#decidim-participatory-process-types) | Tipos de processo. Definem em que menu o processo aparece. | 6 | Decidim |
| [`decidim_participatory_process_user_roles`](#decidim-participatory-process-user-roles) | Papéis de usuários em processos (admin, moderador, avaliador, colaborador). | 7 | Decidim |
| [`decidim_participatory_processes`](#decidim-participatory-processes) | Processos participativos (consultas, conferências, planos, audiências). | 46 | Decidim |
| [`decidim_participatory_space_links`](#decidim-participatory-space-links) | — | 7 | Decidim |
| [`decidim_participatory_space_private_users`](#decidim-participatory-space-private-users) | — | 6 | Decidim |

### `decidim_assemblies` { #decidim-assemblies }

Assembleias, chamadas de instâncias na interface. `parent_id` forma a hierarquia de sub-instâncias.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `slug` | `string` | não |  |  |  |
| `hashtag` | `string` | sim |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `subtitle` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `short_description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `hero_image` | `string` | sim |  |  |  |
| `banner_image` | `string` | sim |  |  |  |
| `promoted` | `boolean` | sim | `false` |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `developer_group` | `jsonb` | sim |  |  |  |
| `meta_scope` | `jsonb` | sim |  |  |  |
| `local_area` | `jsonb` | sim |  |  |  |
| `target` | `jsonb` | sim |  |  |  |
| `participatory_scope` | `jsonb` | sim |  |  |  |
| `participatory_structure` | `jsonb` | sim |  |  |  |
| `show_statistics` | `boolean` | sim | `false` |  |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `scopes_enabled` | `boolean` | não | `true` |  |  |
| `private_space` | `boolean` | sim | `false` |  |  |
| `reference` | `string` | sim |  |  |  |
| `decidim_area_id` | `bigint` | sim |  | → [`decidim_areas`](componentes-conteudo.md#decidim-areas) |  |
| `parent_id` | `bigint` | sim |  | → [`decidim_assemblies`](processos-instancias.md#decidim-assemblies) |  |
| `parents_path` | `ltree` | sim |  |  |  |
| `children_count` | `integer` | sim | `0` | contador em cache |  |
| `purpose_of_action` | `jsonb` | sim |  |  |  |
| `composition` | `jsonb` | sim |  |  |  |
| `creation_date` | `date` | sim |  |  |  |
| `created_by` | `string` | sim |  |  |  |
| `created_by_other` | `jsonb` | sim |  |  |  |
| `duration` | `date` | sim |  |  |  |
| `included_at` | `date` | sim |  |  |  |
| `closing_date` | `date` | sim |  |  |  |
| `closing_date_reason` | `jsonb` | sim |  |  |  |
| `internal_organisation` | `jsonb` | sim |  |  |  |
| `is_transparent` | `boolean` | sim | `true` |  |  |
| `special_features` | `jsonb` | sim |  |  |  |
| `twitter_handler` | `string` | sim |  |  |  |
| `instagram_handler` | `string` | sim |  |  |  |
| `facebook_handler` | `string` | sim |  |  |  |
| `youtube_handler` | `string` | sim |  |  |  |
| `github_handler` | `string` | sim |  |  |  |
| `decidim_assemblies_type_id` | `bigint` | sim |  | FK → [`decidim_assemblies_types`](processos-instancias.md#decidim-assemblies-types) |  |
| `weight` | `integer` | não | `1` |  |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `announcement` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `initial_page_type` | `string` | não | `"default"` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240213153148_add_custom_initial_page_to_assemblies.rb "20240213153148_add_custom_initial_page_to_assemblies.rb") |
| `initial_page_component_id` | `bigint` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240213153148_add_custom_initial_page_to_assemblies.rb "20240213153148_add_custom_initial_page_to_assemblies.rb") |
| `show_documents` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20250618180428_add_show_documents_and_show_members_to_decidim_assemblies.rb "20250618180428_add_show_documents_and_show_members_to_decidim_assemblies.rb") |
| `show_members` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20250618180428_add_show_documents_and_show_members_to_decidim_assemblies.rb "20250618180428_add_show_documents_and_show_members_to_decidim_assemblies.rb") |
| `unlisted` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20260112173425_add_unlisted_attribute_to_assemblies.rb "20260112173425_add_unlisted_attribute_to_assemblies.rb") |

??? note "Índices (6)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_assemblies_on_decidim_area_id` | `decidim_area_id` |  | btree |
    | `index_decidim_assemblies_on_decidim_assemblies_type_id` | `decidim_assemblies_type_id` |  | btree |
    | `index_unique_assembly_slug_and_organization` | `decidim_organization_id`, `slug` | sim | btree |
    | `index_decidim_assemblies_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `index_decidim_assemblies_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `decidim_assemblies_assemblies_on_parent_id` | `parent_id` |  | btree |

### `decidim_assemblies_settings` { #decidim-assemblies-settings }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `enable_organization_chart` | `boolean` | sim | `true` |  |  |
| `decidim_organization_id` | `bigint` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_assemblies_settings_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_assemblies_types` { #decidim-assemblies-types }

Tipos de assembleia.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_assemblies_types_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_assembly_members` { #decidim-assembly-members }

Membros de uma assembleia.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_assembly_id` | `bigint` | sim |  | → [`decidim_assemblies`](processos-instancias.md#decidim-assemblies) |  |
| `weight` | `integer` | não | `0` |  |  |
| `full_name` | `string` | sim |  |  |  |
| `gender` | `string` | sim |  |  |  |
| `birthday` | `date` | sim |  |  |  |
| `birthplace` | `string` | sim |  |  |  |
| `designation_date` | `date` | sim |  |  |  |
| `position` | `string` | sim |  |  |  |
| `position_other` | `string` | sim |  |  |  |
| `ceased_date` | `date` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `decidim_user_id` | `bigint` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_assembly_members_on_decidim_assembly_id` | `decidim_assembly_id` |  | btree |
    | `index_decidim_assembly_members_on_decidim_user_id` | `decidim_user_id` |  | btree |
    | `index_decidim_assembly_members_on_weight_and_created_at` | `weight`, `created_at` |  | btree |

### `decidim_assembly_user_roles` { #decidim-assembly-user-roles }

Papéis de usuários em assembleias.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_user_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_assembly_id` | `integer` | sim |  | → [`decidim_assemblies`](processos-instancias.md#decidim-assemblies) |  |
| `role` | `string` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_unique_user_and_assembly_role` | `decidim_assembly_id`, `decidim_user_id`, `role` | sim | btree |
    | `index_decidim_assembly_user_roles_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_epng_scope_memberships` { #decidim-epng-scope-memberships }

Origem: `decidim-enhanced_process_groups_and_scopes` (LabLivre).

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_user_id` | `bigint` | não |  | FK → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_scope_id` | `bigint` | não |  | FK → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `role` | `string` | não |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_epng_scope_memberships_on_decidim_scope_id` | `decidim_scope_id` |  | btree |
    | `decidim_epng_user_and_scopes_uniquiness` | `decidim_user_id`, `decidim_scope_id` | sim | btree |
    | `index_decidim_epng_scope_memberships_on_decidim_user_id` | `decidim_user_id` |  | btree |

### `decidim_participatory_process_groups` { #decidim-participatory-process-groups }

Grupos de processos.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `hero_image` | `string` | sim |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `hashtag` | `string` | sim |  |  |  |
| `group_url` | `string` | sim |  |  |  |
| `developer_group` | `jsonb` | sim |  |  |  |
| `local_area` | `jsonb` | sim |  |  |  |
| `meta_scope` | `jsonb` | sim |  |  |  |
| `target` | `jsonb` | sim |  |  |  |
| `participatory_scope` | `jsonb` | sim |  |  |  |
| `participatory_structure` | `jsonb` | sim |  |  |  |
| `promoted` | `boolean` | sim | `false` |  |  |
| `decidim_area_id` | `bigint` | sim |  | FK → [`decidim_areas`](componentes-conteudo.md#decidim-areas) | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240421213322_add_area_to_participatory_process_group.rb "20240421213322_add_area_to_participatory_process_group.rb") |
| `decidim_scope_id` | `bigint` | sim |  | FK → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) | `decidim-enhanced_process_groups_and_scopes` (LabLivre) |
| `epng_enhanced` | `boolean` | sim |  |  | `decidim-enhanced_process_groups_and_scopes` (LabLivre) |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_participatory_process_groups_on_decidim_area_id` | `decidim_area_id` |  | btree |
    | `decidim_participatory_process_group_organization` | `decidim_organization_id` |  | btree |
    | `index_decidim_participatory_process_groups_on_decidim_scope_id` | `decidim_scope_id` |  | btree |

### `decidim_participatory_process_steps` { #decidim-participatory-process-steps }

Etapas (fases) de cada processo.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `start_date` | `date` | sim |  |  |  |
| `end_date` | `date` | sim |  |  |  |
| `decidim_participatory_process_id` | `integer` | sim |  | → [`decidim_participatory_processes`](processos-instancias.md#decidim-participatory-processes) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `active` | `boolean` | sim | `false` |  |  |
| `position` | `integer` | sim |  |  |  |
| `cta_text` | `jsonb` | sim | `{}` |  |  |
| `cta_path` | `string` | sim |  |  |  |

??? note "Índices (4)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `unique_index_to_avoid_duplicate_active_steps` | `decidim_participatory_process_id`, `active` | sim | btree (parcial: `(active = true)`) |
    | `index_unique_position_for_process` | `decidim_participatory_process_id`, `position` | sim | btree |
    | `index_decidim_processes_steps__on_decidim_process_id` | `decidim_participatory_process_id` |  | btree |
    | `index_order_by_position_for_steps` | `position` |  | btree |

### `decidim_participatory_process_types` { #decidim-participatory-process-types }

Tipos de processo. Definem em que menu o processo aparece.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `decidim_organization_id` | `bigint` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) | — |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240730140945_add_process_type_description.rb "20240730140945_add_process_type_description.rb") |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_process_types_on_decidim_organization_id` | `decidim_organization_id` |  | btree |

### `decidim_participatory_process_user_roles` { #decidim-participatory-process-user-roles }

Papéis de usuários em processos (admin, moderador, avaliador, colaborador).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_user_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_participatory_process_id` | `integer` | sim |  | → [`decidim_participatory_processes`](processos-instancias.md#decidim-participatory-processes) |  |
| `role` | `string` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `epng_enhanced` | `boolean` | sim |  |  | `decidim-enhanced_process_groups_and_scopes` (LabLivre) |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_unique_user_and_process_role` | `decidim_participatory_process_id`, `decidim_user_id`, `role` | sim | btree |
    | `idx_proces_user_role_on_user_id` | `decidim_user_id` |  | btree |

### `decidim_participatory_processes` { #decidim-participatory-processes }

Processos participativos (consultas, conferências, planos, audiências).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `slug` | `string` | não |  |  |  |
| `hashtag` | `string` | sim |  |  |  |
| `decidim_organization_id` | `integer` | sim |  | FK → [`decidim_organizations`](organizacao-usuarios.md#decidim-organizations) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `title` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `subtitle` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `short_description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | não |  | traduzível (`{"pt-BR": …}`) |  |
| `hero_image` | `string` | sim |  |  |  |
| `banner_image` | `string` | sim |  |  |  |
| `promoted` | `boolean` | sim | `false` |  |  |
| `published_at` | `datetime` | sim |  |  |  |
| `developer_group` | `jsonb` | sim |  |  |  |
| `end_date` | `date` | sim |  |  |  |
| `meta_scope` | `jsonb` | sim |  |  |  |
| `local_area` | `jsonb` | sim |  |  |  |
| `target` | `jsonb` | sim |  |  |  |
| `participatory_scope` | `jsonb` | sim |  |  |  |
| `participatory_structure` | `jsonb` | sim |  |  |  |
| `decidim_scope_id` | `integer` | sim |  | → [`decidim_scopes`](componentes-conteudo.md#decidim-scopes) |  |
| `decidim_participatory_process_group_id` | `integer` | sim |  | → [`decidim_participatory_process_groups`](processos-instancias.md#decidim-participatory-process-groups) |  |
| `show_statistics` | `boolean` | sim | `true` |  |  |
| `announcement` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `scopes_enabled` | `boolean` | não | `true` |  |  |
| `start_date` | `date` | sim |  |  |  |
| `private_space` | `boolean` | sim | `false` |  |  |
| `reference` | `string` | sim |  |  |  |
| `decidim_area_id` | `bigint` | sim |  | → [`decidim_areas`](componentes-conteudo.md#decidim-areas) |  |
| `decidim_scope_type_id` | `bigint` | sim |  | FK → [`decidim_scope_types`](componentes-conteudo.md#decidim-scope-types) |  |
| `show_metrics` | `boolean` | sim | `true` |  |  |
| `weight` | `integer` | não | `1` |  |  |
| `follows_count` | `integer` | não | `0` | contador em cache |  |
| `decidim_participatory_process_type_id` | `bigint` | sim |  | FK → [`decidim_participatory_process_types`](processos-instancias.md#decidim-participatory-process-types) | — |
| `initial_page_type` | `string` | não | `"default"` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240213153444_add_custom_initial_page_to_processes.rb "20240213153444_add_custom_initial_page_to_processes.rb") |
| `initial_page_component_id` | `bigint` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240213153444_add_custom_initial_page_to_processes.rb "20240213153444_add_custom_initial_page_to_processes.rb") |
| `group_chat_id` | `string` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240220181855_add_telegram_group_id_to_participatory_processes.rb "20240220181855_add_telegram_group_id_to_participatory_processes.rb") |
| `should_have_user_full_profile` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240304183136_add_should_have_user_full_profile_to_decidim_participatory_processes.rb "20240304183136_add_should_have_user_full_profile_to_decidim_participatory_processes.rb") |
| `publish_date` | `date` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240321172506_add_publish_date_to_participatory_processes.rb "20240321172506_add_publish_date_to_participatory_processes.rb") |
| `show_mobilization` | `boolean` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240409134438_add_show_mobilization.rb "20240409134438_add_show_mobilization.rb") |
| `is_template` | `boolean` | não | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240412152629_add_is_template_to_participatory_process.rb "20240412152629_add_is_template_to_participatory_process.rb") |
| `extra_fields` | `jsonb` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240722183817_add_extra_fields_to_decidim_participatory_process.rb "20240722183817_add_extra_fields_to_decidim_participatory_process.rb") |
| `mobilization_title` | `string` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240819194623_add_mobilization_title_to_decidim_participatory_processes.rb "20240819194623_add_mobilization_title_to_decidim_participatory_processes.rb") |
| `mobilization_position` | `integer` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240820121007_add_index_of_mobilization_to_participatory_processes.rb "20240820121007_add_index_of_mobilization_to_participatory_processes.rb") |
| `mutually_exclusive_votes_in_proposals_components` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20260405195511_add_mutually_exclusive_votes_in_proposals_components_flag_to_participatory_processes.rb "20260405195511_add_mutually_exclusive_votes_in_proposals_components_flag_to_participatory_processes.rb") |

??? note "Índices (7)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_participatory_processes_on_decidim_area_id` | `decidim_area_id` |  | btree |
    | `index_unique_process_slug_and_organization` | `decidim_organization_id`, `slug` | sim | btree |
    | `index_decidim_processes_on_decidim_organization_id` | `decidim_organization_id` |  | btree |
    | `idx_process_on_process_group_id` | `decidim_participatory_process_group_id` |  | btree |
    | `index_decidim_processes_on_decidim_process_type_id` | `decidim_participatory_process_type_id` |  | btree |
    | `idx_process_on_scope_id` | `decidim_scope_id` |  | btree |
    | `index_decidim_participatory_processes_on_decidim_scope_type_id` | `decidim_scope_type_id` |  | btree |

### `decidim_participatory_space_links` { #decidim-participatory-space-links }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `from_type` | `string` | não |  |  |  |
| `from_id` | `integer` | não |  | polimórfico (tipo em `from_type`) |  |
| `to_type` | `string` | não |  |  |  |
| `to_id` | `integer` | não |  | polimórfico (tipo em `to_type`) |  |
| `name` | `string` | não |  |  |  |
| `data` | `jsonb` | sim |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_participatory_space_links_on_from` | `from_type`, `from_id` |  | btree |
    | `index_participatory_space_links_name` | `name` |  | btree |
    | `index_participatory_space_links_on_to` | `to_type`, `to_id` |  | btree |

### `decidim_participatory_space_private_users` { #decidim-participatory-space-private-users }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_user_id` | `bigint` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `privatable_to_id` | `integer` | sim |  | polimórfico (tipo em `privatable_to_type`) |  |
| `privatable_to_type` | `string` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_spaces_users_on_private_user_id` | `decidim_user_id` |  | btree |
    | `space_privatable_to_privatable_id` | `privatable_to_type`, `privatable_to_id` |  | btree |

