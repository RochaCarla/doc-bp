# Reuniões

**Gem**: `decidim-meetings` (com sobrescritas no core)

O módulo de reuniões organiza eventos presenciais, virtuais ou híbridos, como audiências públicas e etapas de conferências.

## Funcionalidades

- **Agendamento**: data, horário, local e tipo.
- **Inscrição** com controle de vagas.
- **Atas** e resultados.
- **Videoconferência**: link para sala virtual ou serviço incorporado (`MEETINGS_EMBEDDABLE_SERVICES`).
- **Geolocalização**: mapa com o local.
- **Convites**.

## Página de eventos

A listagem geral de eventos (diretório de reuniões) foi redesenhada em 2026:

- filtros padrão do Decidim;
- cards no estilo da tela de eventos, com data e botão de participação no novo design;
- rótulo com o espaço participativo de cada evento;
- mapa exibe apenas reuniões com coordenadas.

## Rotas próprias

| Rota | Uso |
|------|-----|
| `GET /get_all_meetings_of_a_participatory_process/:slug` | Todas as reuniões de um processo |
| `GET /processes/:slug/f/:process_id/meetings/:meeting_id/export` | Exportação das inscrições |

## Configuração

| Opção | Descrição |
|-------|-----------|
| **Inscrições habilitadas** | Permitir inscrições |
| **Limite de vagas** | Máximo de inscritos |
| **Criação por participantes** | Permitir que participantes criem reuniões |
| **Comentários habilitados** | Permitir discussão |

Uma tarefa diária (`decidim_meetings:clean_registration_forms`) limpa formulários de inscrição antigos.

## Referência

- [Documentação oficial do Decidim: Meetings](https://docs.decidim.org/en/develop/admin/components/meetings/)
