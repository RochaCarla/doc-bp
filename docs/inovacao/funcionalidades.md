---
icon: material/star-plus
---

# Funcionalidades

O que o Brasil Participativo acrescentou ao Decidim 0.27.2, por área. Cada item aponta onde está no código.

## Autenticação e canais

| Funcionalidade | Onde |
|----------------|------|
| Login gov.br via OpenID Connect, com PKCE e escopo `govbr_confiabilidades` | `config/initializers/omniauth_govbr.rb` |
| Vínculo de conta com WhatsApp e Telegram ([OP-BP](../operador/integracao-op-bp.md)) | `app/services/external_auth_service.rb` |
| Tela de login simplificada para o login externo | `app/views/decidim/devise/sessions/new.html.erb` |
| Remoção de identidades gov.br duplicadas, ligada por organização | `app/jobs/decidim/remove_duplicated_govbr_identities_job.rb` |
| Bot de moderação no Telegram por processo (`group_chat_id`) | [Manual › Moderação](../manual/moderacao.md) |

## Propostas e votação

| Funcionalidade | Onde |
|----------------|------|
| Votos mutuamente exclusivos entre componentes de um processo | `app/queries/decidim/proposals/govbr/exclusive_proposal_components_user_already_voted_for.rb` |
| Listagem e votação próprias do Orçamento do Povo | `app/views/decidim/proposals/proposals/op_custom_index.html.erb` |
| Exibir contagem de votos (`show_votes`) | `config/initializers/proposals.rb` |
| Perfil completo obrigatório para participar | `should_have_user_full_profile` em processos |
| Estados extras: parcialmente aceita, desqualificada | `app/models/decidim/proposals/proposal.rb` |
| Selos em propostas | `PATCH /proposal_badges/...` |
| Exportação com nome e ID do autor | `app/serializers/decidim/proposals/proposal_serializer.rb` |
| Texto participativo reformulado | [Texto participativo](texto-participativo.md) |

## Comentários como devolutiva

| Funcionalidade | Onde |
|----------------|------|
| Status do comentário: incorporado, incorporado com mudanças, rejeitado | coluna `status`; `comments_controller#update_status` |
| Marcação de conteúdo sensível | coluna `sensitive_content`; `update_sensitive` |
| Anexos em comentários | opção `enable_comments_attachment` |
| Edição limitada a 5 minutos | `app/permissions/decidim/comments/permissions.rb` |
| Exportação com datas de exclusão e moderação | `lib/decidim/comments/comment_serializer.rb` |

## Formulários

| Funcionalidade | Onde |
|----------------|------|
| Limite de arquivos por pergunta (`max_files`) | `app/models/decidim/forms/question.rb` |
| E-mail de confirmação ao responder | `app/commands/decidim/forms/answer_questionnaire.rb` |
| Download de anexos em ZIP | `app/services/decidim/surveys/process_attachment_files.rb` |
| Respostas anônimas | coluna `anonymous_answer` |

## Espaços participativos

| Funcionalidade | Onde |
|----------------|------|
| Assembleias renomeadas para "instâncias" | `config/locales/pt-BR/assemblies.yml` |
| Criação automática de instâncias a partir de órgãos públicos | `app/jobs/decidim/public_bodies_to_instances_job.rb` |
| Instâncias não listadas (`unlisted`) | `app/models/decidim/assembly.rb` |
| Processos-modelo e cópia de processo | `is_template`; `copy_participatory_process.rb` |
| Aba de mobilização, parceiros e links de mídia | tabelas `decidim_govbr_*` |
| Dados do processo (órgão, setor, DOU) | `extra_fields` em processos |
| Troca automática de etapa por fuso horário | `ChangeActiveStepJob` |
| Página inicial por blocos | [`decidim-homes`](../componentes/homes.md) |

## Administração e relatórios

| Funcionalidade | Onde |
|----------------|------|
| Feature flags da organização em `/system` | `decidim_organizations.prune_duplicated_govbr_identities` |
| Super admins por organização | `decidim_organizations.super_admins` |
| Estatísticas de propostas por participante | `decidim_govbr_user_proposals_statistics` |
| Relatórios via Airflow | `Decidim::Govbr::Airflow::TriggerAirflowReport` |
| Acesso ao painel de relatórios para administradores de espaço | `app/views/decidim/proposals/proposals/_admin_actions.html.erb` (`7b7b26d2`) |
| Sitemap diário | `config/sitemap.rb` |

## Interface e acessibilidade

| Funcionalidade | Onde |
|----------------|------|
| Design System gov.br | [Design System](../design-system/index.md) |
| VLibras | `app/views/layouts/decidim/_wrapper.html.erb` |
| Widget de alto contraste e tamanho de fonte | `app/packs/src/acessibility_widget.js` |

## Só na branch `develop`

- Perguntas condicionais em formulários.
- API multicanal.
- Cascata de vínculos entre instâncias e processos.
- Contagem separada de parágrafos de texto participativo e de propostas nas estatísticas.

O banco de dados mostra todas as tabelas e colunas acrescentadas: [Banco de Dados › O que o Brasil Participativo acrescentou](../banco-de-dados/index.md#o-que-o-brasil-participativo-acrescentou).
