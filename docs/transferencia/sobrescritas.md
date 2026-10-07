---
title: Inventário de sobrescritas
---

<!-- Gerado por scripts/sobrescritas.py em 2026-10-07T14:09:18+00:00. Não edite à mão. -->

# Inventário de sobrescritas

Arquivos do `decidim-govbr` (branch `main`) que **substituem** arquivos do Decidim 0.27.2. O Rails carrega a versão do core no lugar da versão da gem, então cada um deles precisa ser revisado ao atualizar o Decidim. Veja o [Plano de atualização tecnológica](atualizacao.md).

!!! info "Gerado em 07/10/2026"
    Comparação de `app/`, `lib/`, `config/initializers/` com as gems do Decidim na tag `v0.27.2`. Para atualizar, rode `python3 scripts/sobrescritas.py`.

## Resumo

| Item | Quantidade |
|---|---:|
| Arquivos sobrescritos | 492 |
| Linhas diferentes do original (adicionadas + removidas) | 21.012 |
| Sobrescritas idênticas ao original (podem ser removidas) | 26 |
| Arquivos próprios, sem equivalente no Decidim | 532 |

## Por gem do Decidim

Quanto mais linhas diferentes, maior o esforço de atualização.

| Gem | Arquivos sobrescritos | Linhas diferentes |
|---|---:|---:|
| `decidim-core` | 137 | 6.266 |
| `decidim-proposals` | 72 | 3.506 |
| `decidim-meetings` | 68 | 3.439 |
| `decidim-participatory_processes` | 53 | 1.796 |
| `decidim-assemblies` | 28 | 1.618 |
| `decidim-admin` | 44 | 1.323 |
| `decidim-comments` | 25 | 1.242 |
| `decidim-forms` | 24 | 1.039 |
| `decidim-blogs` | 6 | 261 |
| `decidim-conferences` | 4 | 137 |
| `decidim-surveys` | 3 | 131 |
| `decidim-verifications` | 14 | 102 |
| `decidim-dev` | 3 | 71 |
| `decidim-initiatives` | 1 | 34 |
| `decidim-pages` | 5 | 25 |
| `decidim-system` | 4 | 20 |
| `decidim-accountability` | 1 | 2 |

## Por tipo de arquivo

| Tipo | Arquivos | Linhas diferentes |
|---|---:|---:|
| `views` | 182 | 10.252 |
| `cells` | 92 | 2.592 |
| `packs` | 27 | 1.971 |
| `controllers` | 35 | 1.464 |
| `commands` | 47 | 1.259 |
| `helpers` | 19 | 952 |
| `forms` | 32 | 688 |
| `lib/decidim` | 17 | 560 |
| `permissions` | 8 | 481 |
| `config/initializers` | 2 | 357 |
| `models` | 20 | 344 |
| `presenters` | 6 | 42 |
| `validators` | 1 | 20 |
| `queries` | 1 | 14 |
| `services` | 1 | 12 |
| `jobs` | 1 | 2 |
| `serializers` | 1 | 2 |

## As 40 sobrescritas mais alteradas

| Arquivo | Gem | + | − | Linhas no core |
|---|---|---:|---:|---:|
| [`app/views/decidim/devise/sessions/new.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/devise/sessions/new.html.erb) | `decidim-core` | 456 | 51 | 463 |
| [`app/views/decidim/meetings/meetings/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/meetings/meetings/_form.html.erb) | `decidim-meetings` | 387 | 81 | 409 |
| [`app/views/layouts/decidim/_wrapper.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/layouts/decidim/_wrapper.html.erb) | `decidim-core` | 298 | 96 | 318 |
| [`app/views/decidim/meetings/meetings/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/meetings/meetings/show.html.erb) | `decidim-meetings` | 229 | 150 | 256 |
| [`app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb) | `decidim-participatory_processes` | 196 | 175 | 225 |
| [`app/views/decidim/admin/components/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/admin/components/_form.html.erb) | `decidim-admin` | 282 | 37 | 331 |
| [`config/initializers/devise.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/config/initializers/devise.rb) | `decidim-core` | 2 | 315 | 5 |
| [`app/packs/stylesheets/decidim/modules/_comments.scss`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/packs/stylesheets/decidim/modules/_comments.scss) | `decidim-core` | 159 | 109 | 333 |
| [`app/packs/stylesheets/decidim/modules/_process-nav.scss`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/packs/stylesheets/decidim/modules/_process-nav.scss) | `decidim-core` | 94 | 164 | 112 |
| [`app/controllers/decidim/proposals/proposals_controller.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/controllers/decidim/proposals/proposals_controller.rb) | `decidim-proposals` | 170 | 83 | 395 |
| [`app/views/decidim/assemblies/assemblies/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/assemblies/assemblies/show.html.erb) | `decidim-assemblies` | 43 | 207 | 62 |
| [`app/helpers/decidim/proposals/application_helper.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/helpers/decidim/proposals/application_helper.rb) | `decidim-proposals` | 222 | 23 | 388 |
| [`app/views/decidim/proposals/proposals/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/proposals/proposals/show.html.erb) | `decidim-proposals` | 137 | 107 | 171 |
| [`app/views/layouts/decidim/_main_footer.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/layouts/decidim/_main_footer.html.erb) | `decidim-core` | 214 | 30 | 215 |
| [`app/views/decidim/participatory_processes/participatory_processes/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/participatory_processes/participatory_processes/show.html.erb) | `decidim-participatory_processes` | 101 | 140 | 114 |
| [`app/packs/src/decidim/data_consent/consent_manager.js`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/packs/src/decidim/data_consent/consent_manager.js) | `decidim-core` | 119 | 114 | 141 |
| [`app/views/decidim/admin/organization/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/admin/organization/_form.html.erb) | `decidim-admin` | 137 | 86 | 159 |
| [`app/views/decidim/proposals/proposals/index.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/proposals/proposals/index.html.erb) | `decidim-proposals` | 175 | 47 | 184 |
| [`app/packs/src/decidim/comments/comments.component.js`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/packs/src/decidim/comments/comments.component.js) | `decidim-comments` | 204 | 15 | 518 |
| [`app/views/decidim/forms/admin/questionnaires/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/forms/admin/questionnaires/_form.html.erb) | `decidim-forms` | 137 | 81 | 182 |
| [`app/views/decidim/meetings/admin/meetings/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/meetings/admin/meetings/_form.html.erb) | `decidim-meetings` | 182 | 27 | 262 |
| [`app/views/decidim/forms/questionnaires/answers/_files.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/forms/questionnaires/answers/_files.html.erb) | `decidim-forms` | 200 | 1 | 200 |
| [`app/helpers/decidim/application_helper.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/helpers/decidim/application_helper.rb) | `decidim-core` | 197 | 2 | 322 |
| [`app/views/decidim/assemblies/admin/assemblies/_form.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/assemblies/admin/assemblies/_form.html.erb) | `decidim-assemblies` | 56 | 122 | 176 |
| [`app/packs/src/decidim/participatory_processes/filters.js`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/packs/src/decidim/participatory_processes/filters.js) | `decidim-participatory_processes` | 161 | 9 | 180 |
| [`app/views/decidim/proposals/proposals/new.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/proposals/proposals/new.html.erb) | `decidim-proposals` | 129 | 30 | 139 |
| [`app/cells/decidim/comments/comment/show.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/cells/decidim/comments/comment/show.erb) | `decidim-comments` | 116 | 42 | 125 |
| [`app/views/decidim/forms/questionnaires/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/forms/questionnaires/show.html.erb) | `decidim-forms` | 13 | 145 | 24 |
| [`app/views/decidim/pages/index.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/pages/index.html.erb) | `decidim-core` | 88 | 69 | 109 |
| [`app/views/decidim/proposals/admin/proposals/show.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/proposals/admin/proposals/show.html.erb) | `decidim-proposals` | 74 | 80 | 180 |
| [`app/cells/decidim/flag_modal/show.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/cells/decidim/flag_modal/show.erb) | `decidim-core` | 141 | 12 | 156 |
| [`app/permissions/decidim/assemblies/permissions.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/permissions/decidim/assemblies/permissions.rb) | `decidim-assemblies` | 89 | 63 | 344 |
| [`app/views/decidim/devise/invitations/edit.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/devise/invitations/edit.html.erb) | `decidim-core` | 89 | 62 | 108 |
| [`app/views/decidim/proposals/proposals/preview.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/proposals/proposals/preview.html.erb) | `decidim-proposals` | 119 | 32 | 128 |
| [`app/permissions/decidim/participatory_processes/permissions.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/permissions/decidim/participatory_processes/permissions.rb) | `decidim-participatory_processes` | 103 | 43 | 345 |
| [`app/controllers/decidim/proposals/admin/participatory_texts_controller.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/controllers/decidim/proposals/admin/participatory_texts_controller.rb) | `decidim-proposals` | 119 | 24 | 195 |
| [`app/views/decidim/devise/registrations/new.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/devise/registrations/new.html.erb) | `decidim-core` | 52 | 87 | 62 |
| [`app/views/decidim/blogs/posts/_posts.html.erb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/views/decidim/blogs/posts/_posts.html.erb) | `decidim-blogs` | 110 | 22 | 112 |
| [`app/controllers/decidim/comments/comments_controller.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/app/controllers/decidim/comments/comments_controller.rb) | `decidim-comments` | 118 | 13 | 290 |
| [`lib/decidim/comments/comment_serializer.rb`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr/-/blob/main/lib/decidim/comments/comment_serializer.rb) | `decidim-comments` | 121 | 9 | 155 |

## Sobrescritas idênticas ao original

Estes arquivos são iguais aos do Decidim 0.27.2. Podem ser removidos do core sem mudar o comportamento, o que reduz o trabalho de atualização.

- `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/filters.erb` (`decidim-participatory_processes`)
- `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/participatory_space_filters.erb` (`decidim-participatory_processes`)
- `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/show.erb` (`decidim-participatory_processes`)
- `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/title_filter_order.erb` (`decidim-participatory_processes`)
- `app/cells/decidim/upload_modal/show.erb` (`decidim-core`)
- `app/models/decidim/forms/questionnaire.rb` (`decidim-forms`)
- `app/packs/src/decidim/direct_uploads/upload_utility.js` (`decidim-core`)
- `app/packs/src/decidim/direct_uploads/uploader.js` (`decidim-core`)
- `app/views/decidim/authorization_modals/show.html.erb` (`decidim-core`)
- `app/views/decidim/meetings/meetings/_count.html.erb` (`decidim-meetings`)
- `app/views/decidim/meetings/meetings/_datetime.html.erb` (`decidim-meetings`)
- `app/views/decidim/meetings/meetings/_meeting_minutes.html.erb` (`decidim-meetings`)
- `app/views/decidim/meetings/meetings/index.js.erb` (`decidim-meetings`)
- `app/views/decidim/proposals/proposals/complete.html.erb` (`decidim-proposals`)
- `app/views/decidim/proposals/proposals/index.js.erb` (`decidim-proposals`)
- `app/views/decidim/proposals/proposals/participatory_texts/_proposal_votes_count.html.erb` (`decidim-proposals`)
- `app/views/decidim/verifications/authorizations/index.html.erb` (`decidim-verifications`)
- `app/views/decidim/verifications/id_documents/admin/config/edit.html.erb` (`decidim-verifications`)
- `app/views/decidim/verifications/id_documents/admin/offline_confirmations/new.html.erb` (`decidim-verifications`)
- `app/views/decidim/verifications/id_documents/authorizations/choose.html.erb` (`decidim-verifications`)
- `app/views/decidim/verifications/id_documents/authorizations/new.html.erb` (`decidim-verifications`)
- `app/views/layouts/decidim/_topbar_search.html.erb` (`decidim-core`)
- `lib/decidim/api/participatory_process_step_type.rb` (`decidim-participatory_processes`)
- `lib/decidim/dev/assets/participatory_text.md` (`decidim-dev`)
- `lib/decidim/dev/test/rspec_support/geocoder.rb` (`decidim-dev`)
- `lib/decidim/meetings/test/notifications_handling.rb` (`decidim-meetings`)

## Lista completa por gem

??? note "`decidim-accountability` — 1 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/jobs/application_job.rb` | 0 | 2 |

??? note "`decidim-admin` — 44 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/admin/content_block/show.erb` | 9 | 4 |
    | `app/cells/decidim/admin/content_block_cell.rb` | 5 | 8 |
    | `app/commands/decidim/admin/create_component.rb` | 4 | 1 |
    | `app/commands/decidim/admin/create_newsletter.rb` | 1 | 1 |
    | `app/commands/decidim/admin/create_participatory_space_private_user.rb` | 6 | 0 |
    | `app/commands/decidim/admin/create_static_page.rb` | 3 | 2 |
    | `app/commands/decidim/admin/create_static_page_topic.rb` | 3 | 2 |
    | `app/commands/decidim/admin/unhide_resource.rb` | 1 | 1 |
    | `app/commands/decidim/admin/update_component.rb` | 6 | 2 |
    | `app/commands/decidim/admin/update_newsletter.rb` | 1 | 1 |
    | `app/commands/decidim/admin/update_organization.rb` | 20 | 8 |
    | `app/controllers/decidim/admin/component_permissions_controller.rb` | 2 | 2 |
    | `app/controllers/decidim/admin/components_controller.rb` | 40 | 5 |
    | `app/controllers/decidim/admin/exports_controller.rb` | 48 | 2 |
    | `app/controllers/decidim/admin/officializations_controller.rb` | 28 | 0 |
    | `app/controllers/decidim/admin/organization_controller.rb` | 26 | 0 |
    | `app/controllers/decidim/admin/organization_homepage_content_blocks_controller.rb` | 28 | 37 |
    | `app/controllers/decidim/admin/organization_homepage_controller.rb` | 28 | 28 |
    | `app/controllers/decidim/admin/static_page_topics_controller.rb` | 18 | 0 |
    | `app/controllers/decidim/admin/static_pages_controller.rb` | 18 | 0 |
    | `app/forms/decidim/admin/component_form.rb` | 8 | 2 |
    | `app/forms/decidim/admin/organization_form.rb` | 39 | 0 |
    | `app/forms/decidim/admin/static_page_form.rb` | 1 | 0 |
    | `app/forms/decidim/admin/static_page_topic_form.rb` | 1 | 0 |
    | `app/helpers/decidim/admin/application_helper.rb` | 1 | 1 |
    | `app/permissions/decidim/admin/permissions.rb` | 41 | 1 |
    | `app/views/decidim/admin/components/_form.html.erb` | 282 | 37 |
    | `app/views/decidim/admin/components/_settings_fields.html.erb` | 11 | 7 |
    | `app/views/decidim/admin/components/index.html.erb` | 5 | 1 |
    | `app/views/decidim/admin/components/new.html.erb` | 1 | 2 |
    | `app/views/decidim/admin/exports/_dropdown.html.erb` | 49 | 13 |
    | `app/views/decidim/admin/officializations/index.html.erb` | 5 | 0 |
    | `app/views/decidim/admin/organization/_form.html.erb` | 137 | 86 |
    | `app/views/decidim/admin/organization_homepage/edit.html.erb` | 0 | 43 |
    | `app/views/decidim/admin/organization_homepage_content_blocks/edit.html.erb` | 0 | 13 |
    | `app/views/decidim/admin/shared/landing_page/edit.html.erb` | 1 | 47 |
    | `app/views/decidim/admin/static_page_topics/_form.html.erb` | 2 | 0 |
    | `app/views/decidim/admin/static_page_topics/edit.html.erb` | 10 | 2 |
    | `app/views/decidim/admin/static_page_topics/new.html.erb` | 2 | 2 |
    | `app/views/decidim/admin/static_pages/_form.html.erb` | 2 | 0 |
    | `app/views/decidim/admin/static_pages/_topic.html.erb` | 29 | 1 |
    | `app/views/decidim/admin/static_pages/edit.html.erb` | 10 | 2 |
    | `app/views/decidim/admin/static_pages/new.html.erb` | 2 | 2 |
    | `app/views/decidim/admin/users/_form.html.erb` | 22 | 1 |

??? note "`decidim-assemblies` — 28 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/assemblies/assembly_m/footer.erb` | 11 | 12 |
    | `app/cells/decidim/assemblies/assembly_m_cell.rb` | 69 | 12 |
    | `app/cells/decidim/assemblies/assembly_member/show.erb` | 41 | 48 |
    | `app/cells/decidim/assemblies/assembly_member_cell.rb` | 17 | 0 |
    | `app/commands/decidim/assemblies/admin/create_assembly.rb` | 39 | 60 |
    | `app/commands/decidim/assemblies/admin/create_assembly_admin.rb` | 26 | 14 |
    | `app/commands/decidim/assemblies/admin/destroy_assembly_admin.rb` | 21 | 12 |
    | `app/commands/decidim/assemblies/admin/update_assembly.rb` | 58 | 12 |
    | `app/commands/decidim/assemblies/admin/update_assembly_admin.rb` | 23 | 11 |
    | `app/controllers/concerns/decidim/assemblies/admin/filterable.rb` | 23 | 0 |
    | `app/controllers/decidim/assemblies/admin/assemblies_controller.rb` | 9 | 0 |
    | `app/controllers/decidim/assemblies/assemblies_controller.rb` | 75 | 6 |
    | `app/controllers/decidim/assemblies/assembly_members_controller.rb` | 10 | 18 |
    | `app/forms/decidim/assemblies/admin/assembly_form.rb` | 38 | 14 |
    | `app/helpers/decidim/assemblies/admin/assemblies_helper.rb` | 1 | 3 |
    | `app/models/decidim/assembly.rb` | 77 | 27 |
    | `app/permissions/decidim/assemblies/permissions.rb` | 89 | 63 |
    | `app/presenters/decidim/assemblies/assembly_stats_presenter.rb` | 7 | 2 |
    | `app/views/decidim/assemblies/admin/assemblies/_form.html.erb` | 56 | 122 |
    | `app/views/decidim/assemblies/admin/assemblies/index.html.erb` | 3 | 3 |
    | `app/views/decidim/assemblies/assemblies/_parent_assemblies.html.erb` | 16 | 6 |
    | `app/views/decidim/assemblies/assemblies/index.html.erb` | 73 | 3 |
    | `app/views/decidim/assemblies/assemblies/show.html.erb` | 43 | 207 |
    | `app/views/decidim/assemblies/assembly_members/index.html.erb` | 14 | 6 |
    | `app/views/decidim/assembly_members/_assembly_member.html.erb` | 2 | 1 |
    | `app/views/layouts/decidim/_assembly_header.html.erb` | 28 | 23 |
    | `app/views/layouts/decidim/_assembly_navigation.html.erb` | 24 | 12 |
    | `app/views/layouts/decidim/assembly.html.erb` | 13 | 15 |

??? note "`decidim-blogs` — 6 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/commands/decidim/blogs/admin/update_post.rb` | 1 | 0 |
    | `app/forms/decidim/blogs/admin/post_form.rb` | 2 | 0 |
    | `app/views/decidim/blogs/admin/posts/_form.html.erb` | 4 | 1 |
    | `app/views/decidim/blogs/posts/_posts.html.erb` | 110 | 22 |
    | `app/views/decidim/blogs/posts/index.html.erb` | 2 | 5 |
    | `app/views/decidim/blogs/posts/show.html.erb` | 72 | 42 |

??? note "`decidim-comments` — 25 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/comments/comment/actions.erb` | 9 | 5 |
    | `app/cells/decidim/comments/comment/show.erb` | 116 | 42 |
    | `app/cells/decidim/comments/comment/utilities.erb` | 32 | 37 |
    | `app/cells/decidim/comments/comment_cell.rb` | 29 | 3 |
    | `app/cells/decidim/comments/comment_form/show.erb` | 21 | 2 |
    | `app/cells/decidim/comments/comment_form_cell.rb` | 6 | 0 |
    | `app/cells/decidim/comments/comment_thread/show.erb` | 2 | 1 |
    | `app/cells/decidim/comments/comments/add_comment.erb` | 5 | 20 |
    | `app/cells/decidim/comments/comments/order_control.erb` | 39 | 35 |
    | `app/cells/decidim/comments/comments/show.erb` | 83 | 24 |
    | `app/cells/decidim/comments/comments_cell.rb` | 21 | 3 |
    | `app/commands/decidim/comments/create_comment.rb` | 24 | 1 |
    | `app/commands/decidim/comments/update_comment.rb` | 2 | 1 |
    | `app/controllers/decidim/comments/comments_controller.rb` | 118 | 13 |
    | `app/forms/decidim/comments/comment_form.rb` | 16 | 0 |
    | `app/models/decidim/comments/comment.rb` | 15 | 6 |
    | `app/packs/src/decidim/comments/comments.component.js` | 204 | 15 |
    | `app/permissions/decidim/comments/permissions.rb` | 23 | 1 |
    | `app/queries/decidim/comments/sorted_comments.rb` | 2 | 12 |
    | `app/views/decidim/comments/comments/create.js.erb` | 21 | 3 |
    | `app/views/decidim/comments/comments/error.js.erb` | 19 | 1 |
    | `app/views/decidim/comments/comments/reload.js.erb` | 37 | 4 |
    | `lib/decidim/api/comment_type.rb` | 8 | 0 |
    | `lib/decidim/comments/comment_serializer.rb` | 121 | 9 |
    | `lib/decidim/comments/comments_helper.rb` | 23 | 8 |

??? note "`decidim-conferences` — 4 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/conferences/media_link/show.erb` | 54 | 9 |
    | `app/cells/decidim/conferences/photo/show.erb` | 16 | 23 |
    | `app/cells/decidim/conferences/photos_list/show.erb` | 13 | 5 |
    | `app/views/layouts/decidim/conference.html.erb` | 8 | 9 |

??? note "`decidim-core` — 137 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/amendable/amend_button_card/show.erb` | 3 | 9 |
    | `app/cells/decidim/announcement/show.erb` | 6 | 5 |
    | `app/cells/decidim/author/date.erb` | 2 | 1 |
    | `app/cells/decidim/author/profile_inline.erb` | 1 | 1 |
    | `app/cells/decidim/author/profile_minicard.erb` | 11 | 15 |
    | `app/cells/decidim/author/show.erb` | 0 | 9 |
    | `app/cells/decidim/author/withdraw.erb` | 12 | 4 |
    | `app/cells/decidim/card_m/badge.erb` | 10 | 1 |
    | `app/cells/decidim/card_m/header.erb` | 3 | 4 |
    | `app/cells/decidim/card_m/show.erb` | 14 | 20 |
    | `app/cells/decidim/card_m/top.erb` | 5 | 2 |
    | `app/cells/decidim/card_m_cell.rb` | 10 | 1 |
    | `app/cells/decidim/collapsible_authors/show.erb` | 26 | 6 |
    | `app/cells/decidim/collapsible_list/show.erb` | 1 | 1 |
    | `app/cells/decidim/content_blocks/hero/show.erb` | 1 | 3 |
    | `app/cells/decidim/content_blocks/html/show.erb` | 1 | 0 |
    | `app/cells/decidim/data_consent/category.erb` | 7 | 7 |
    | `app/cells/decidim/data_consent/dialog.erb` | 14 | 13 |
    | `app/cells/decidim/data_consent/modal.erb` | 23 | 25 |
    | `app/cells/decidim/date_range/show.erb` | 44 | 22 |
    | `app/cells/decidim/date_range_cell.rb` | 0 | 2 |
    | `app/cells/decidim/flag_modal/show.erb` | 141 | 12 |
    | `app/cells/decidim/navbar_admin_link/show.erb` | 10 | 5 |
    | `app/cells/decidim/navbar_admin_link_cell.rb` | 9 | 3 |
    | `app/cells/decidim/profile_sidebar/show.erb` | 10 | 11 |
    | `app/cells/decidim/progress_bar/show.erb` | 2 | 2 |
    | `app/cells/decidim/search_results_section/show.erb` | 18 | 19 |
    | `app/cells/decidim/search_results_section_cell.rb` | 0 | 4 |
    | `app/cells/decidim/statistic/show.erb` | 5 | 5 |
    | `app/cells/decidim/statistics/show.erb` | 13 | 17 |
    | `app/cells/decidim/tags_cell.rb` | 3 | 3 |
    | `app/cells/decidim/upload_modal/files.erb` | 75 | 24 |
    | `app/cells/decidim/upload_modal/modal.erb` | 8 | 1 |
    | `app/cells/decidim/upload_modal/show.erb` | 0 | 0 |
    | `app/cells/decidim/user_profile/user_data.erb` | 9 | 13 |
    | `app/commands/decidim/create_omniauth_registration.rb` | 38 | 5 |
    | `app/commands/decidim/create_registration.rb` | 17 | 3 |
    | `app/commands/decidim/invite_user.rb` | 34 | 0 |
    | `app/controllers/concerns/decidim/paginable.rb` | 1 | 1 |
    | `app/controllers/decidim/devise/invitations_controller.rb` | 2 | 1 |
    | `app/controllers/decidim/devise/registrations_controller.rb` | 7 | 3 |
    | `app/controllers/decidim/devise/sessions_controller.rb` | 16 | 0 |
    | `app/controllers/decidim/pages_controller.rb` | 19 | 4 |
    | `app/forms/decidim/invite_user_form.rb` | 12 | 0 |
    | `app/helpers/decidim/action_authorization_helper.rb` | 5 | 5 |
    | `app/helpers/decidim/application_helper.rb` | 197 | 2 |
    | `app/helpers/decidim/check_boxes_tree_helper.rb` | 29 | 15 |
    | `app/helpers/decidim/layout_helper.rb` | 22 | 7 |
    | `app/helpers/decidim/map_helper.rb` | 24 | 2 |
    | `app/helpers/decidim/sanitize_helper.rb` | 19 | 6 |
    | `app/models/decidim/attachment.rb` | 2 | 0 |
    | `app/models/decidim/organization.rb` | 2 | 0 |
    | `app/models/decidim/report.rb` | 6 | 1 |
    | `app/models/decidim/static_page.rb` | 5 | 2 |
    | `app/models/decidim/static_page_topic.rb` | 6 | 1 |
    | `app/models/decidim/user.rb` | 4 | 0 |
    | `app/packs/src/decidim/data_consent/consent_manager.js` | 119 | 114 |
    | `app/packs/src/decidim/data_consent/index.js` | 0 | 4 |
    | `app/packs/src/decidim/data_picker.js` | 3 | 6 |
    | `app/packs/src/decidim/decidim_application.js` | 21 | 0 |
    | `app/packs/src/decidim/direct_uploads/upload_field.js` | 27 | 4 |
    | `app/packs/src/decidim/direct_uploads/upload_modal.js` | 2 | 1 |
    | `app/packs/src/decidim/direct_uploads/upload_utility.js` | 0 | 0 |
    | `app/packs/src/decidim/direct_uploads/uploader.js` | 0 | 0 |
    | `app/packs/src/decidim/external_link.js` | 26 | 56 |
    | `app/packs/src/decidim/index.js` | 28 | 26 |
    | `app/packs/src/decidim/user_registrations.js` | 0 | 10 |
    | `app/packs/stylesheets/decidim/_decidim-settings.scss` | 4 | 0 |
    | `app/packs/stylesheets/decidim/decidim_application.scss` | 35 | 1 |
    | `app/packs/stylesheets/decidim/modules/_author-avatar.scss` | 59 | 4 |
    | `app/packs/stylesheets/decidim/modules/_comments.scss` | 159 | 109 |
    | `app/packs/stylesheets/decidim/modules/_data-picker.scss` | 72 | 5 |
    | `app/packs/stylesheets/decidim/modules/_docs-manager.scss` | 75 | 4 |
    | `app/packs/stylesheets/decidim/modules/_filters.scss` | 19 | 9 |
    | `app/packs/stylesheets/decidim/modules/_inline-filters.scss` | 2 | 1 |
    | `app/packs/stylesheets/decidim/modules/_process-header.scss` | 19 | 49 |
    | `app/packs/stylesheets/decidim/modules/_process-nav.scss` | 94 | 164 |
    | `app/packs/stylesheets/decidim/modules/_statistics.scss` | 73 | 46 |
    | `app/packs/stylesheets/decidim/modules/_upload_modal.scss` | 5 | 4 |
    | `app/packs/stylesheets/decidim/plugins/leaflet.scss` | 102 | 1 |
    | `app/presenters/decidim/stats_presenter.rb` | 17 | 0 |
    | `app/validators/etiquette_validator.rb` | 7 | 13 |
    | `app/views/decidim/application/_attachments.erb` | 4 | 8 |
    | `app/views/decidim/application/_collection.html.erb` | 28 | 6 |
    | `app/views/decidim/application/_document.erb` | 8 | 17 |
    | `app/views/decidim/application/_documents.erb` | 37 | 12 |
    | `app/views/decidim/application/_photos.erb` | 11 | 4 |
    | `app/views/decidim/authorization_modals/_content.html.erb` | 38 | 36 |
    | `app/views/decidim/authorization_modals/show.html.erb` | 0 | 0 |
    | `app/views/decidim/devise/confirmations/new.html.erb` | 36 | 27 |
    | `app/views/decidim/devise/invitations/edit.html.erb` | 89 | 62 |
    | `app/views/decidim/devise/passwords/edit.html.erb` | 33 | 31 |
    | `app/views/decidim/devise/passwords/new.html.erb` | 26 | 19 |
    | `app/views/decidim/devise/registrations/new.html.erb` | 52 | 87 |
    | `app/views/decidim/devise/sessions/new.html.erb` | 456 | 51 |
    | `app/views/decidim/devise/shared/_links.html.erb` | 18 | 29 |
    | `app/views/decidim/devise/shared/_omniauth_buttons.html.erb` | 5 | 21 |
    | `app/views/decidim/devise/unlocks/new.html.erb` | 30 | 22 |
    | `app/views/decidim/pages/_tabbed.html.erb` | 58 | 36 |
    | `app/views/decidim/pages/index.html.erb` | 88 | 69 |
    | `app/views/decidim/pages/show.html.erb` | 3 | 1 |
    | `app/views/decidim/searches/_count.html.erb` | 32 | 26 |
    | `app/views/decidim/searches/_filters.html.erb` | 41 | 16 |
    | `app/views/decidim/searches/_resources_filter_block.html.erb` | 10 | 17 |
    | `app/views/decidim/searches/index.html.erb` | 6 | 9 |
    | `app/views/decidim/shared/_address_details.html.erb` | 1 | 7 |
    | `app/views/decidim/shared/_check_boxes_tree.html.erb` | 55 | 52 |
    | `app/views/decidim/shared/_confirm_modal.html.erb` | 8 | 15 |
    | `app/views/decidim/shared/_embed_modal.html.erb` | 2 | 2 |
    | `app/views/decidim/shared/_extended_navigation_bar.html.erb` | 25 | 48 |
    | `app/views/decidim/shared/_filter_form_help.erb` | 2 | 2 |
    | `app/views/decidim/shared/_floating_help.html.erb` | 0 | 30 |
    | `app/views/decidim/shared/_orders.html.erb` | 11 | 7 |
    | `app/views/decidim/shared/_results_per_page.html.erb` | 9 | 3 |
    | `app/views/decidim/shared/_share_modal.html.erb` | 5 | 48 |
    | `app/views/decidim/shared/_static_map.html.erb` | 16 | 11 |
    | `app/views/decidim/widgets/_data_picker.html.erb` | 18 | 3 |
    | `app/views/devise/mailer/confirmation_instructions.html.erb` | 34 | 6 |
    | `app/views/devise/mailer/reset_password_instructions.html.erb` | 7 | 5 |
    | `app/views/kaminari/decidim/_first_page.html.erb` | 4 | 5 |
    | `app/views/kaminari/decidim/_last_page.html.erb` | 5 | 6 |
    | `app/views/kaminari/decidim/_next_page.html.erb` | 4 | 6 |
    | `app/views/kaminari/decidim/_paginator.html.erb` | 1 | 1 |
    | `app/views/kaminari/decidim/_prev_page.html.erb` | 4 | 6 |
    | `app/views/layouts/decidim/_admin_links.html.erb` | 27 | 2 |
    | `app/views/layouts/decidim/_head.html.erb` | 46 | 10 |
    | `app/views/layouts/decidim/_main_footer.html.erb` | 214 | 30 |
    | `app/views/layouts/decidim/_topbar_search.html.erb` | 0 | 0 |
    | `app/views/layouts/decidim/_user_menu.html.erb` | 6 | 6 |
    | `app/views/layouts/decidim/_wrapper.html.erb` | 298 | 96 |
    | `app/views/layouts/decidim/mailer.html.erb` | 17 | 0 |
    | `config/initializers/carrierwave.rb` | 28 | 12 |
    | `config/initializers/devise.rb` | 2 | 315 |
    | `lib/decidim/api/input_filters/has_publishable_input_filter.rb` | 40 | 1 |
    | `lib/decidim/filter_form_builder.rb` | 18 | 8 |
    | `lib/decidim/has_attachments.rb` | 4 | 0 |
    | `lib/decidim/nicknamizable.rb` | 5 | 1 |

??? note "`decidim-dev` — 3 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `lib/decidim/dev/assets/logo.png` | 37 | 34 |
    | `lib/decidim/dev/assets/participatory_text.md` | 0 | 0 |
    | `lib/decidim/dev/test/rspec_support/geocoder.rb` | 0 | 0 |

??? note "`decidim-forms` — 24 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/commands/decidim/forms/admin/update_questionnaire.rb` | 8 | 2 |
    | `app/commands/decidim/forms/answer_questionnaire.rb` | 23 | 17 |
    | `app/controllers/decidim/forms/admin/concerns/has_questionnaire.rb` | 33 | 1 |
    | `app/controllers/decidim/forms/concerns/has_questionnaire.rb` | 22 | 3 |
    | `app/forms/decidim/forms/admin/display_condition_form.rb` | 1 | 1 |
    | `app/forms/decidim/forms/admin/question_form.rb` | 6 | 0 |
    | `app/forms/decidim/forms/admin/questionnaire_form.rb` | 5 | 1 |
    | `app/forms/decidim/forms/answer_form.rb` | 29 | 4 |
    | `app/forms/decidim/forms/questionnaire_form.rb` | 8 | 1 |
    | `app/helpers/decidim/forms/application_helper.rb` | 15 | 1 |
    | `app/models/decidim/forms/answer.rb` | 4 | 0 |
    | `app/models/decidim/forms/question.rb` | 26 | 0 |
    | `app/models/decidim/forms/questionnaire.rb` | 0 | 0 |
    | `app/presenters/decidim/forms/admin/questionnaire_answer_presenter.rb` | 4 | 0 |
    | `app/views/decidim/forms/admin/questionnaires/_display_condition.html.erb` | 2 | 2 |
    | `app/views/decidim/forms/admin/questionnaires/_form.html.erb` | 137 | 81 |
    | `app/views/decidim/forms/admin/questionnaires/_question.html.erb` | 56 | 27 |
    | `app/views/decidim/forms/admin/questionnaires/_separator.html.erb` | 15 | 10 |
    | `app/views/decidim/forms/admin/questionnaires/_title_and_description.html.erb` | 19 | 15 |
    | `app/views/decidim/forms/questionnaires/_answer.html.erb` | 44 | 16 |
    | `app/views/decidim/forms/questionnaires/answers/_files.html.erb` | 200 | 1 |
    | `app/views/decidim/forms/questionnaires/answers/_short_answer.html.erb` | 9 | 1 |
    | `app/views/decidim/forms/questionnaires/show.html.erb` | 13 | 145 |
    | `lib/decidim/forms/user_answers_serializer.rb` | 27 | 4 |

??? note "`decidim-initiatives` — 1 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/views/decidim/initiatives/initiative_signatures/_wizard_steps.html.erb` | 15 | 19 |

??? note "`decidim-meetings` — 68 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/meetings/highlighted_meetings_for_component/show.erb` | 5 | 6 |
    | `app/cells/decidim/meetings/join_meeting_button/registration_confirm.erb` | 11 | 24 |
    | `app/cells/decidim/meetings/join_meeting_button/show.erb` | 37 | 33 |
    | `app/cells/decidim/meetings/join_meeting_button_cell.rb` | 1 | 3 |
    | `app/cells/decidim/meetings/meeting_m/address.erb` | 5 | 4 |
    | `app/cells/decidim/meetings/meeting_m/data.erb` | 1 | 1 |
    | `app/cells/decidim/meetings/meeting_m/date.erb` | 36 | 7 |
    | `app/cells/decidim/meetings/meeting_m/footer.erb` | 11 | 7 |
    | `app/cells/decidim/meetings/meeting_m/multiple_dates.erb` | 1 | 1 |
    | `app/cells/decidim/meetings/meeting_m_cell.rb` | 72 | 11 |
    | `app/cells/decidim/meetings/meetings_map/show.erb` | 16 | 7 |
    | `app/cells/decidim/meetings/online_meeting_link/show.erb` | 41 | 31 |
    | `app/cells/decidim/meetings/public_participants_list/show.erb` | 5 | 15 |
    | `app/commands/decidim/meetings/admin/close_meeting.rb` | 62 | 4 |
    | `app/commands/decidim/meetings/admin/copy_meeting.rb` | 2 | 0 |
    | `app/commands/decidim/meetings/admin/create_meeting.rb` | 10 | 4 |
    | `app/commands/decidim/meetings/admin/publish_meeting.rb` | 1 | 1 |
    | `app/commands/decidim/meetings/admin/update_meeting.rb` | 20 | 7 |
    | `app/commands/decidim/meetings/close_meeting.rb` | 78 | 3 |
    | `app/commands/decidim/meetings/create_meeting.rb` | 28 | 4 |
    | `app/commands/decidim/meetings/update_meeting.rb` | 33 | 30 |
    | `app/controllers/decidim/meetings/meeting_closes_controller.rb` | 3 | 1 |
    | `app/controllers/decidim/meetings/meetings_controller.rb` | 43 | 61 |
    | `app/controllers/decidim/meetings/registrations_controller.rb` | 15 | 0 |
    | `app/forms/decidim/meetings/admin/close_meeting_form.rb` | 32 | 3 |
    | `app/forms/decidim/meetings/admin/meeting_form.rb` | 7 | 18 |
    | `app/forms/decidim/meetings/base_meeting_form.rb` | 53 | 3 |
    | `app/forms/decidim/meetings/close_meeting_form.rb` | 82 | 2 |
    | `app/forms/decidim/meetings/meeting_form.rb` | 66 | 52 |
    | `app/helpers/decidim/meetings/application_helper.rb` | 47 | 18 |
    | `app/helpers/decidim/meetings/map_helper.rb` | 23 | 11 |
    | `app/helpers/decidim/meetings/meetings_helper.rb` | 35 | 9 |
    | `app/models/decidim/meetings/meeting.rb` | 56 | 15 |
    | `app/packs/src/decidim/meetings/admin/registrations_invite_form.js` | 13 | 7 |
    | `app/permissions/decidim/meetings/admin/permissions.rb` | 8 | 6 |
    | `app/permissions/decidim/meetings/permissions.rb` | 68 | 7 |
    | `app/presenters/decidim/meetings/meeting_presenter.rb` | 2 | 0 |
    | `app/serializers/decidim/meetings/registration_serializer.rb` | 2 | 0 |
    | `app/services/decidim/meetings/meeting_iframe_embedder.rb` | 7 | 5 |
    | `app/views/decidim/meetings/_calendar_modal.html.erb` | 8 | 11 |
    | `app/views/decidim/meetings/admin/agenda/edit.html.erb` | 11 | 5 |
    | `app/views/decidim/meetings/admin/agenda/new.html.erb` | 10 | 5 |
    | `app/views/decidim/meetings/admin/meeting_closes/_form.html.erb` | 69 | 11 |
    | `app/views/decidim/meetings/admin/meetings/_form.html.erb` | 182 | 27 |
    | `app/views/decidim/meetings/admin/meetings/index.html.erb` | 7 | 2 |
    | `app/views/decidim/meetings/directory/meetings/_meetings.html.erb` | 20 | 19 |
    | `app/views/decidim/meetings/directory/meetings/index.html.erb` | 65 | 12 |
    | `app/views/decidim/meetings/directory/meetings/index.js.erb` | 2 | 2 |
    | `app/views/decidim/meetings/meeting_closes/_form.html.erb` | 111 | 6 |
    | `app/views/decidim/meetings/meeting_closes/edit.html.erb` | 18 | 18 |
    | `app/views/decidim/meetings/meetings/_calendar_modal.html.erb` | 4 | 6 |
    | `app/views/decidim/meetings/meetings/_count.html.erb` | 0 | 0 |
    | `app/views/decidim/meetings/meetings/_datetime.html.erb` | 0 | 0 |
    | `app/views/decidim/meetings/meetings/_filters.html.erb` | 4 | 14 |
    | `app/views/decidim/meetings/meetings/_filters_small_view.html.erb` | 7 | 6 |
    | `app/views/decidim/meetings/meetings/_form.html.erb` | 387 | 81 |
    | `app/views/decidim/meetings/meetings/_linked_meetings.html.erb` | 11 | 9 |
    | `app/views/decidim/meetings/meetings/_meeting_agenda.html.erb` | 42 | 24 |
    | `app/views/decidim/meetings/meetings/_meeting_minutes.html.erb` | 0 | 0 |
    | `app/views/decidim/meetings/meetings/_meetings.html.erb` | 17 | 16 |
    | `app/views/decidim/meetings/meetings/edit.html.erb` | 14 | 21 |
    | `app/views/decidim/meetings/meetings/index.html.erb` | 87 | 30 |
    | `app/views/decidim/meetings/meetings/index.js.erb` | 0 | 0 |
    | `app/views/decidim/meetings/meetings/new.html.erb` | 21 | 22 |
    | `app/views/decidim/meetings/meetings/show.html.erb` | 229 | 150 |
    | `lib/decidim/api/meetings_type.rb` | 44 | 4 |
    | `lib/decidim/meetings/meeting_serializer.rb` | 73 | 36 |
    | `lib/decidim/meetings/test/notifications_handling.rb` | 0 | 0 |

??? note "`decidim-pages` — 5 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/commands/decidim/pages/admin/update_page.rb` | 1 | 0 |
    | `app/forms/decidim/pages/admin/page_form.rb` | 1 | 0 |
    | `app/models/decidim/pages/page.rb` | 1 | 1 |
    | `app/views/decidim/pages/admin/pages/_form.html.erb` | 1 | 0 |
    | `app/views/decidim/pages/application/show.html.erb` | 9 | 11 |

??? note "`decidim-participatory_processes` — 53 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/participatory_process_groups/content_block_cell.rb` | 5 | 1 |
    | `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/filters.erb` | 0 | 0 |
    | `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/filters_small_view.erb` | 1 | 1 |
    | `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/participatory_space_filters.erb` | 0 | 0 |
    | `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/show.erb` | 0 | 0 |
    | `app/cells/decidim/participatory_process_groups/content_blocks/highlighted_participatory_processes/title_filter_order.erb` | 0 | 0 |
    | `app/cells/decidim/participatory_processes/process_filters/filter_tabs.erb` | 23 | 11 |
    | `app/cells/decidim/participatory_processes/process_filters/show.erb` | 44 | 15 |
    | `app/cells/decidim/participatory_processes/process_filters/type_filter.erb` | 14 | 14 |
    | `app/cells/decidim/participatory_processes/process_filters_cell.rb` | 27 | 2 |
    | `app/cells/decidim/participatory_processes/process_m/data.erb` | 19 | 20 |
    | `app/cells/decidim/participatory_processes/process_m/footer.erb` | 12 | 11 |
    | `app/cells/decidim/participatory_processes/process_m/tags.erb` | 1 | 1 |
    | `app/cells/decidim/participatory_processes/process_m_cell.rb` | 41 | 7 |
    | `app/commands/decidim/participatory_processes/admin/activate_participatory_process_step.rb` | 13 | 7 |
    | `app/commands/decidim/participatory_processes/admin/copy_participatory_process.rb` | 71 | 4 |
    | `app/commands/decidim/participatory_processes/admin/create_participatory_process.rb` | 37 | 3 |
    | `app/commands/decidim/participatory_processes/admin/create_participatory_process_group.rb` | 2 | 1 |
    | `app/commands/decidim/participatory_processes/admin/update_participatory_process.rb` | 26 | 1 |
    | `app/commands/decidim/participatory_processes/admin/update_participatory_process_type.rb` | 2 | 1 |
    | `app/controllers/decidim/participatory_processes/admin/participatory_process_copies_controller.rb` | 2 | 2 |
    | `app/controllers/decidim/participatory_processes/admin/participatory_process_group_landing_page_content_blocks_controller.rb` | 17 | 0 |
    | `app/controllers/decidim/participatory_processes/admin/participatory_process_group_landing_page_controller.rb` | 18 | 1 |
    | `app/controllers/decidim/participatory_processes/admin/participatory_processes_controller.rb` | 6 | 2 |
    | `app/controllers/decidim/participatory_processes/participatory_processes_controller.rb` | 55 | 7 |
    | `app/forms/decidim/participatory_processes/admin/participatory_process_copy_form.rb` | 8 | 0 |
    | `app/forms/decidim/participatory_processes/admin/participatory_process_form.rb` | 49 | 6 |
    | `app/forms/decidim/participatory_processes/admin/participatory_process_group_form.rb` | 6 | 0 |
    | `app/forms/decidim/participatory_processes/admin/participatory_process_type_form.rb` | 1 | 0 |
    | `app/models/decidim/participatory_process.rb` | 11 | 1 |
    | `app/models/decidim/participatory_process_group.rb` | 7 | 0 |
    | `app/models/decidim/participatory_process_step.rb` | 10 | 0 |
    | `app/models/decidim/participatory_process_type.rb` | 1 | 1 |
    | `app/models/decidim/participatory_process_user_role.rb` | 1 | 1 |
    | `app/packs/src/decidim/participatory_processes/filters.js` | 161 | 9 |
    | `app/permissions/decidim/participatory_processes/permissions.rb` | 103 | 43 |
    | `app/presenters/decidim/participatory_processes/admin_log/participatory_process_presenter.rb` | 2 | 1 |
    | `app/presenters/decidim/participatory_processes/participatory_process_stats_presenter.rb` | 6 | 1 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_copies/_form.html.erb` | 5 | 3 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_copies/new.html.erb` | 8 | 2 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_groups/_form.html.erb` | 7 | 0 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_steps/_form.html.erb` | 3 | 3 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_steps/index.html.erb` | 1 | 1 |
    | `app/views/decidim/participatory_processes/admin/participatory_process_types/_form.html.erb` | 6 | 0 |
    | `app/views/decidim/participatory_processes/admin/participatory_processes/_form.html.erb` | 196 | 175 |
    | `app/views/decidim/participatory_processes/admin/participatory_processes/index.html.erb` | 19 | 0 |
    | `app/views/decidim/participatory_processes/participatory_processes/index.html.erb` | 15 | 9 |
    | `app/views/decidim/participatory_processes/participatory_processes/show.html.erb` | 101 | 140 |
    | `app/views/layouts/decidim/_process_header.html.erb` | 35 | 24 |
    | `app/views/layouts/decidim/_process_navigation.html.erb` | 30 | 5 |
    | `app/views/layouts/decidim/participatory_process.html.erb` | 3 | 7 |
    | `lib/decidim/api/participatory_process_step_type.rb` | 0 | 0 |
    | `lib/decidim/api/participatory_process_type.rb` | 21 | 0 |

??? note "`decidim-proposals` — 72 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/cells/decidim/proposals/highlighted_proposals_for_component/show.erb` | 2 | 4 |
    | `app/cells/decidim/proposals/participatory_text_proposal/buttons.erb` | 22 | 31 |
    | `app/cells/decidim/proposals/participatory_text_proposal/show.erb` | 11 | 6 |
    | `app/cells/decidim/proposals/participatory_text_proposal_cell.rb` | 23 | 6 |
    | `app/cells/decidim/proposals/proposal_m/footer.erb` | 34 | 19 |
    | `app/cells/decidim/proposals/proposal_m_cell.rb` | 19 | 1 |
    | `app/cells/decidim/proposals/proposal_tags/show.erb` | 30 | 32 |
    | `app/cells/decidim/proposals/proposals_picker/proposals.erb` | 13 | 3 |
    | `app/cells/decidim/proposals/proposals_picker/show.erb` | 10 | 5 |
    | `app/cells/decidim/proposals/proposals_picker_cell.rb` | 1 | 0 |
    | `app/commands/decidim/proposals/admin/create_proposal.rb` | 3 | 2 |
    | `app/commands/decidim/proposals/admin/update_participatory_text.rb` | 95 | 11 |
    | `app/commands/decidim/proposals/admin/update_proposal.rb` | 79 | 22 |
    | `app/commands/decidim/proposals/create_proposal.rb` | 33 | 9 |
    | `app/commands/decidim/proposals/publish_proposal.rb` | 12 | 0 |
    | `app/commands/decidim/proposals/update_proposal.rb` | 3 | 2 |
    | `app/commands/decidim/proposals/vote_proposal.rb` | 2 | 1 |
    | `app/controllers/concerns/decidim/proposals/orderable.rb` | 5 | 7 |
    | `app/controllers/decidim/proposals/admin/participatory_texts_controller.rb` | 119 | 24 |
    | `app/controllers/decidim/proposals/admin/proposal_answers_controller.rb` | 11 | 0 |
    | `app/controllers/decidim/proposals/admin/proposals_controller.rb` | 30 | 3 |
    | `app/controllers/decidim/proposals/proposals_controller.rb` | 170 | 83 |
    | `app/forms/decidim/proposals/admin/import_participatory_text_form.rb` | 5 | 1 |
    | `app/forms/decidim/proposals/admin/participatory_text_proposal_form.rb` | 19 | 3 |
    | `app/forms/decidim/proposals/admin/preview_participatory_text_form.rb` | 7 | 0 |
    | `app/forms/decidim/proposals/admin/proposal_answer_form.rb` | 7 | 2 |
    | `app/forms/decidim/proposals/admin/proposal_form.rb` | 33 | 2 |
    | `app/forms/decidim/proposals/proposal_form.rb` | 11 | 0 |
    | `app/helpers/decidim/proposals/admin/proposals_helper.rb` | 7 | 1 |
    | `app/helpers/decidim/proposals/application_helper.rb` | 222 | 23 |
    | `app/helpers/decidim/proposals/map_helper.rb` | 2 | 1 |
    | `app/helpers/decidim/proposals/participatory_texts_helper.rb` | 97 | 3 |
    | `app/helpers/decidim/proposals/proposal_votes_helper.rb` | 31 | 2 |
    | `app/helpers/decidim/proposals/proposal_wizard_helper.rb` | 20 | 19 |
    | `app/helpers/decidim/proposals/proposals_helper.rb` | 21 | 5 |
    | `app/models/decidim/proposals/proposal.rb` | 36 | 5 |
    | `app/permissions/decidim/proposals/admin/permissions.rb` | 11 | 4 |
    | `app/permissions/decidim/proposals/permissions.rb` | 10 | 3 |
    | `app/views/decidim/proposals/admin/participatory_texts/_article-preview.html.erb` | 41 | 6 |
    | `app/views/decidim/proposals/admin/participatory_texts/_bulk-actions.html.erb` | 1 | 0 |
    | `app/views/decidim/proposals/admin/participatory_texts/index.html.erb` | 4 | 44 |
    | `app/views/decidim/proposals/admin/participatory_texts/new_import.html.erb` | 1 | 1 |
    | `app/views/decidim/proposals/admin/proposal_answers/_form.html.erb` | 1 | 7 |
    | `app/views/decidim/proposals/admin/proposals/_bulk-actions.html.erb` | 31 | 28 |
    | `app/views/decidim/proposals/admin/proposals/_form.html.erb` | 48 | 2 |
    | `app/views/decidim/proposals/admin/proposals/index.html.erb` | 6 | 1 |
    | `app/views/decidim/proposals/admin/proposals/show.html.erb` | 74 | 80 |
    | `app/views/decidim/proposals/proposal_votes/update_buttons_and_counters.js.erb` | 58 | 13 |
    | `app/views/decidim/proposals/proposals/_count.html.erb` | 8 | 1 |
    | `app/views/decidim/proposals/proposals/_filters.html.erb` | 43 | 44 |
    | `app/views/decidim/proposals/proposals/_filters_small_view.html.erb` | 5 | 4 |
    | `app/views/decidim/proposals/proposals/_linked_proposals.html.erb` | 20 | 19 |
    | `app/views/decidim/proposals/proposals/_proposals.html.erb` | 34 | 30 |
    | `app/views/decidim/proposals/proposals/_vote_button.html.erb` | 33 | 20 |
    | `app/views/decidim/proposals/proposals/_votes_count.html.erb` | 19 | 17 |
    | `app/views/decidim/proposals/proposals/_voting_rules.html.erb` | 50 | 42 |
    | `app/views/decidim/proposals/proposals/_wizard_aside.html.erb` | 5 | 19 |
    | `app/views/decidim/proposals/proposals/_wizard_header.html.erb` | 21 | 31 |
    | `app/views/decidim/proposals/proposals/compare.html.erb` | 1 | 0 |
    | `app/views/decidim/proposals/proposals/complete.html.erb` | 0 | 0 |
    | `app/views/decidim/proposals/proposals/edit.html.erb` | 83 | 23 |
    | `app/views/decidim/proposals/proposals/edit_draft.html.erb` | 0 | 1 |
    | `app/views/decidim/proposals/proposals/index.html.erb` | 175 | 47 |
    | `app/views/decidim/proposals/proposals/index.js.erb` | 0 | 0 |
    | `app/views/decidim/proposals/proposals/new.html.erb` | 129 | 30 |
    | `app/views/decidim/proposals/proposals/participatory_texts/_index.html.erb` | 13 | 16 |
    | `app/views/decidim/proposals/proposals/participatory_texts/_proposal_vote_button.html.erb` | 3 | 3 |
    | `app/views/decidim/proposals/proposals/participatory_texts/_proposal_votes_count.html.erb` | 0 | 0 |
    | `app/views/decidim/proposals/proposals/participatory_texts/_view_index.html.erb` | 19 | 8 |
    | `app/views/decidim/proposals/proposals/participatory_texts/participatory_text.html.erb` | 25 | 12 |
    | `app/views/decidim/proposals/proposals/preview.html.erb` | 119 | 32 |
    | `app/views/decidim/proposals/proposals/show.html.erb` | 137 | 107 |

??? note "`decidim-surveys` — 3 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/controllers/decidim/surveys/surveys_controller.rb` | 84 | 0 |
    | `app/models/decidim/surveys/survey.rb` | 8 | 5 |
    | `lib/decidim/api/surveys_type.rb` | 30 | 4 |

??? note "`decidim-system` — 4 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/commands/decidim/system/update_organization.rb` | 3 | 0 |
    | `app/forms/decidim/system/update_organization_form.rb` | 11 | 0 |
    | `app/views/decidim/system/organizations/_advanced_settings.html.erb` | 1 | 0 |
    | `app/views/decidim/system/organizations/edit.html.erb` | 5 | 0 |

??? note "`decidim-verifications` — 14 arquivos"

    | Arquivo | + | − |
    |---|---:|---:|
    | `app/commands/decidim/verifications/confirm_user_authorization.rb` | 3 | 0 |
    | `app/commands/decidim/verifications/perform_authorization_step.rb` | 7 | 1 |
    | `app/forms/decidim/verifications/id_documents/information_form.rb` | 2 | 1 |
    | `app/forms/decidim/verifications/id_documents/upload_form.rb` | 6 | 0 |
    | `app/views/decidim/verifications/authorizations/first_login.html.erb` | 20 | 21 |
    | `app/views/decidim/verifications/authorizations/index.html.erb` | 0 | 0 |
    | `app/views/decidim/verifications/id_documents/admin/config/edit.html.erb` | 0 | 0 |
    | `app/views/decidim/verifications/id_documents/admin/confirmations/new.html.erb` | 10 | 1 |
    | `app/views/decidim/verifications/id_documents/admin/offline_confirmations/new.html.erb` | 0 | 0 |
    | `app/views/decidim/verifications/id_documents/admin/pending_authorizations/index.html.erb` | 1 | 0 |
    | `app/views/decidim/verifications/id_documents/authorizations/_form.html.erb` | 19 | 1 |
    | `app/views/decidim/verifications/id_documents/authorizations/choose.html.erb` | 0 | 0 |
    | `app/views/decidim/verifications/id_documents/authorizations/edit.html.erb` | 6 | 3 |
    | `app/views/decidim/verifications/id_documents/authorizations/new.html.erb` | 0 | 0 |

## Arquivos próprios

Arquivos sem equivalente no Decidim (código exclusivo do Brasil Participativo), por pasta:

| Pasta | Arquivos |
|---|---:|
| `views` | 268 |
| `packs` | 68 |
| `commands` | 36 |
| `controllers` | 32 |
| `config` | 31 |
| `lib` | 22 |
| `cells` | 17 |
| `forms` | 10 |
| `models` | 10 |
| `helpers` | 8 |
| `assets` | 7 |
| `services` | 6 |
| `mailers` | 5 |
| `jobs` | 3 |
| `presenters` | 3 |
| `serializers` | 3 |
| `channels` | 2 |
| `queries` | 1 |
