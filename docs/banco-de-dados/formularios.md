---
icon: material/form-select
---

<!-- Gerado por scripts/banco_de_dados.py em 2026-10-07T12:08:06+00:00. Não edite à mão. -->

# Formulários

Questionários, perguntas, condições de exibição e respostas dos componentes de formulário.

**8 tabelas.** Schema versão `20260405195511`. Legenda da coluna **Referência**: *FK* = chave estrangeira declarada no banco; *→* = referência por convenção de nome (sem restrição no banco).

## Relacionamentos

Relações entre as tabelas deste domínio. Referências para outros domínios aparecem nas tabelas abaixo.

```mermaid
erDiagram
    decidim_forms_answer_options ||--o{ decidim_forms_answer_choices : ""
    decidim_forms_answer_options ||--o{ decidim_forms_display_conditions : ""
    decidim_forms_answers ||--o{ decidim_forms_answer_choices : ""
    decidim_forms_question_matrix_rows ||--o{ decidim_forms_answer_choices : ""
    decidim_forms_questionnaires ||--o{ decidim_forms_answers : ""
    decidim_forms_questionnaires ||--o{ decidim_forms_questions : ""
    decidim_forms_questions ||--o{ decidim_forms_answer_options : ""
    decidim_forms_questions ||--o{ decidim_forms_answers : ""
    decidim_forms_questions ||--o{ decidim_forms_display_conditions : ""
    decidim_forms_questions ||--o{ decidim_forms_question_matrix_rows : ""
```

## Tabelas

| Tabela | Descrição | Colunas | Origem |
|---|---|---:|---|
| [`decidim_forms_answer_choices`](#decidim-forms-answer-choices) | Opções escolhidas em uma resposta. | 7 | Decidim |
| [`decidim_forms_answer_options`](#decidim-forms-answer-options) | Opções de resposta. | 4 | Decidim |
| [`decidim_forms_answers`](#decidim-forms-answers) | Respostas a perguntas. | 12 | Decidim |
| [`decidim_forms_display_conditions`](#decidim-forms-display-conditions) | Condições de exibição entre perguntas. | 9 | Decidim |
| [`decidim_forms_question_matrix_rows`](#decidim-forms-question-matrix-rows) | — | 4 | Decidim |
| [`decidim_forms_questionnaires`](#decidim-forms-questionnaires) | Questionários. Polimórfico em `questionnaire_for` (formulário, reunião…). | 12 | Decidim |
| [`decidim_forms_questions`](#decidim-forms-questions) | Perguntas de um questionário. | 13 | Decidim |
| [`decidim_surveys_surveys`](#decidim-surveys-surveys) | Componente de formulário (enquete). | 4 | Decidim |

### `decidim_forms_answer_choices` { #decidim-forms-answer-choices }

Opções escolhidas em uma resposta.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_answer_id` | `bigint` | sim |  | → [`decidim_forms_answers`](formularios.md#decidim-forms-answers) |  |
| `decidim_answer_option_id` | `bigint` | sim |  | → [`decidim_forms_answer_options`](formularios.md#decidim-forms-answer-options) |  |
| `position` | `integer` | sim |  |  |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `custom_body` | `text` | sim |  |  |  |
| `decidim_question_matrix_row_id` | `integer` | sim |  | → [`decidim_forms_question_matrix_rows`](formularios.md#decidim-forms-question-matrix-rows) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_answer_choices_answer_id` | `decidim_answer_id` |  | btree |
    | `index_decidim_forms_answer_choices_answer_option_id` | `decidim_answer_option_id` |  | btree |

### `decidim_forms_answer_options` { #decidim-forms-answer-options }

Opções de resposta.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_question_id` | `bigint` | sim |  | → [`decidim_forms_questions`](formularios.md#decidim-forms-questions) |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `free_text` | `boolean` | sim |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_answer_options_question_id` | `decidim_question_id` |  | btree |

### `decidim_forms_answers` { #decidim-forms-answers }

Respostas a perguntas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `body` | `text` | sim |  |  |  |
| `decidim_user_id` | `integer` | sim |  | → [`decidim_users`](organizacao-usuarios.md#decidim-users) |  |
| `decidim_questionnaire_id` | `integer` | sim |  | → [`decidim_forms_questionnaires`](formularios.md#decidim-forms-questionnaires) |  |
| `decidim_question_id` | `integer` | sim |  | → [`decidim_forms_questions`](formularios.md#decidim-forms-questions) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `session_token` | `string` | não | `""` |  |  |
| `ip_hash` | `string` | sim |  |  |  |
| `anonymous_answer` | `boolean` | sim | `true` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20231128195549_add_anonymous_answer_to_answer.rb "20231128195549_add_anonymous_answer_to_answer.rb") |
| `decidim_meetings_meeting_id` | `integer` | sim |  | FK → [`decidim_meetings_meetings`](reunioes.md#decidim-meetings-meetings) | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240807171104_add_questions_answers_to_meeting.rb "20240807171104_add_questions_answers_to_meeting.rb") |
| `extra_fields` | `jsonb` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240812200008_add_extra_fields_to_answers.rb "20240812200008_add_extra_fields_to_answers.rb") |

??? note "Índices (5)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_answers_question_id` | `decidim_question_id` |  | btree |
    | `index_decidim_forms_answers_on_decidim_questionnaire_id` | `decidim_questionnaire_id` |  | btree |
    | `index_decidim_forms_answers_on_decidim_user_id` | `decidim_user_id` |  | btree |
    | `index_decidim_forms_answers_on_ip_hash` | `ip_hash` |  | btree |
    | `index_decidim_forms_answers_on_session_token` | `session_token` |  | btree |

### `decidim_forms_display_conditions` { #decidim-forms-display-conditions }

Condições de exibição entre perguntas.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_question_id` | `bigint` | não |  | → [`decidim_forms_questions`](formularios.md#decidim-forms-questions) |  |
| `decidim_condition_question_id` | `bigint` | não |  |  |  |
| `decidim_answer_option_id` | `bigint` | sim |  | → [`decidim_forms_answer_options`](formularios.md#decidim-forms-answer-options) |  |
| `condition_type` | `integer` | não | `0` |  |  |
| `condition_value` | `jsonb` | sim |  |  |  |
| `mandatory` | `boolean` | sim | `false` |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (3)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `decidim_forms_display_condition_answer_option` | `decidim_answer_option_id` |  | btree |
    | `decidim_forms_display_condition_condition_question` | `decidim_condition_question_id` |  | btree |
    | `decidim_forms_display_condition_question` | `decidim_question_id` |  | btree |

### `decidim_forms_question_matrix_rows` { #decidim-forms-question-matrix-rows }

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `bigint` | não |  | chave primária |  |
| `decidim_question_id` | `bigint` | sim |  | → [`decidim_forms_questions`](formularios.md#decidim-forms-questions) |  |
| `position` | `integer` | sim |  |  |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_question_matrix_questionnaire_id` | `decidim_question_id` |  | btree |
    | `index_decidim_forms_question_matrix_rows_on_position` | `position` |  | btree |

### `decidim_forms_questionnaires` { #decidim-forms-questionnaires }

Questionários. Polimórfico em `questionnaire_for` (formulário, reunião…).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `title` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `tos` | `jsonb` | sim |  |  |  |
| `questionnaire_for_type` | `string` | sim |  |  |  |
| `questionnaire_for_id` | `integer` | sim |  | polimórfico (tipo em `questionnaire_for_type`) |  |
| `published_at` | `datetime` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `salt` | `string` | sim |  |  |  |
| `topp` | `jsonb` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20231128211231_add_topp_fields_to_questionnaires.rb "20231128211231_add_topp_fields_to_questionnaires.rb") |
| `collect_user_data` | `boolean` | sim | `false` |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20231128211231_add_topp_fields_to_questionnaires.rb "20231128211231_add_topp_fields_to_questionnaires.rb") |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_questionnaires_questionnaire_for` | `questionnaire_for_type`, `questionnaire_for_id` |  | btree |

### `decidim_forms_questions` { #decidim-forms-questions }

Perguntas de um questionário.

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_questionnaire_id` | `integer` | sim |  | → [`decidim_forms_questionnaires`](formularios.md#decidim-forms-questionnaires) |  |
| `position` | `integer` | sim |  |  |  |
| `question_type` | `string` | sim |  |  |  |
| `mandatory` | `boolean` | sim |  |  |  |
| `body` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `description` | `jsonb` | sim |  | traduzível (`{"pt-BR": …}`) |  |
| `max_choices` | `integer` | sim |  |  |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |
| `max_characters` | `integer` | sim | `0` |  |  |
| `decidim_meetings_meeting_id` | `integer` | sim |  | FK → [`decidim_meetings_meetings`](reunioes.md#decidim-meetings-meetings) | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20240807171104_add_questions_answers_to_meeting.rb "20240807171104_add_questions_answers_to_meeting.rb") |
| `max_files` | `integer` | sim |  |  | [:flag_br: BP](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/db/migrate/20250909160405_add_max_files_to_decidim_forms_questions.rb "20250909160405_add_max_files_to_decidim_forms_questions.rb") |

??? note "Índices (2)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_forms_questions_on_decidim_questionnaire_id` | `decidim_questionnaire_id` |  | btree |
    | `index_decidim_forms_questions_on_position` | `position` |  | btree |

### `decidim_surveys_surveys` { #decidim-surveys-surveys }

Componente de formulário (enquete).

Origem: Decidim.

| Coluna | Tipo | Nulo | Padrão | Referência / observação | Origem |
|---|---|:---:|---|---|---|
| `id` | `serial` | não |  | chave primária |  |
| `decidim_component_id` | `integer` | sim |  | → [`decidim_components`](componentes-conteudo.md#decidim-components) |  |
| `created_at` | `datetime` | não |  |  |  |
| `updated_at` | `datetime` | não |  |  |  |

??? note "Índices (1)"

    | Nome | Colunas | Único | Tipo |
    |---|---|:---:|---|
    | `index_decidim_surveys_surveys_on_decidim_component_id` | `decidim_component_id` |  | btree |

