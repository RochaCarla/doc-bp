# Componentes usados

Levantamento das classes do Design System gov.br nas views e cells do core (`app/views`, `app/cells`), na branch `main`. Das 357 views ERB do core, 64 usam componentes do padrão.

## Componentes por número de usos

Contagem de ocorrências da classe base em atributos `class` (cada elemento conta uma vez).

| Componente | Usos | Onde aparece |
|------------|-----:|--------------|
| `br-button` | 71 | Botões em toda a plataforma (votar, enviar, filtros, idioma) |
| `br-container` | 52 | Contêineres de largura máxima (`br-container-lg`) |
| `br-divider` | 28 | Separadores de seção |
| `br-item` | 18 | Itens de listas e menus |
| `br-input` | 18 | Campos de formulário |
| `br-message` | 11 | Mensagens de feedback (sucesso, erro, aviso) |
| `br-sign-in` | 8 | Botão de entrar no cabeçalho e nas telas de texto participativo |
| `br-list` | 8 | Listas e menus suspensos (`br-list-dropdown`) |
| `br-modal` | 7 | Diálogos |
| `br-radio` | 4 | Opções de escolha única |
| `br-magic-button` | 4 | Botão de destaque |
| `br-footer` | 4 | Rodapé |
| `br-card` | 3 | Cartões de posts do blog |
| `br-scrim` | 2 | Sobreposição de fundo |
| `br-upload` | 1 | Envio de arquivos |
| `br-tab` | 1 | Abas |
| `br-switch` | 1 | Interruptor |
| `br-menu` | 1 | Menu principal |
| `br-header` | 1 | Cabeçalho |
| `br-datetimepicker` | 1 | Seletor de data |
| `br-avatar` | 1 | Avatar |

No componente `decidim-homes` (página inicial), os mais usados são `br-container` (34), `br-button` (29), `br-carousel` (6) e `br-modal` (4).

## Comportamentos em JavaScript

O `core.js` traz o comportamento destes componentes do padrão:

`accordion`, `avatar`, `breadcrumb`, `card`, `carousel`, `checkbox`, `cookiebar`, `datetimepicker`, `footer`, `header`, `input`, `item`, `list`, `menu`, `message`, `modal`, `notification`, `pagination`, `scrim`, `select`, `step`, `tab`, `table`, `tag`, `textarea`, `tooltip`, `upload`, `wizard`.

Ele também inclui os comportamentos genéricos `accordion`, `checkgroup`, `collapse`, `dropdown`, `scrim`, `swipe` e `tooltip`.

Os componentes são ativados pela classe no HTML. Um `br-modal` ganha comportamento ao carregar a página, sem chamada explícita na view.

## Telas e componentes

| Tela | Componentes gov.br | Arquivos |
|------|-------------------|----------|
| Cabeçalho e menu | `br-header`, `br-menu`, `br-avatar`, `br-sign-in`, `br-button`, `br-list` | `layouts/decidim/_wrapper.html.erb` |
| Rodapé | `br-footer`, `br-list`, `br-container-lg` | `layouts/decidim/_main_footer.html.erb` |
| Login, cadastro e senha | `br-input`, `br-button` | `decidim/devise/*/new.html.erb` |
| Propostas e Orçamento do Povo | `br-button`, `br-message`, `br-magic-button` | `decidim/proposals/proposals/` |
| Texto participativo | `br-sign-in`, `br-button` | `decidim/proposals/proposals/participatory_texts/`, `decidim/proposals/participatory_text_proposal/` |
| Formulários | `br-input`, `br-upload` | `decidim/forms/questionnaires/` |
| Filtros de componentes | `br-radio` | `decidim/components/_filter.html.erb` |
| Abas de navegação do espaço | `br-tab` | `decidim/shared/_extended_navigation_bar.html.erb` |
| Exportação | `br-datetimepicker`, `br-input` | `decidim/shared/_export_modal.html.erb` |
| Consentimento de cookies | `br-switch` | `cells/decidim/data_consent/` |
| Blog | `br-card`, `br-message` | `decidim/blogs/posts/_posts.html.erb` |

A tela de vínculo de conta do [login externo](../operador/integracao-op-bp.md) (`external_auth/link_success`) tem layout próprio e não usa classes do padrão.

## Classes próprias com prefixo `br-`

Estas classes **não** são do Design System, apesar do prefixo: `br-processes`, `br-assemblies`, `br-announcement`, `br-decidim-logo`, `br-cookie-modal`, `br-cookie-group`, `br-cookie-buttons`, `br-author`, `br-actions`, `br-comment`, `br-filter-container`, `br-date`, `br-subtitle`. Elas são definidas no próprio Brasil Participativo. Ao procurar um componente na documentação oficial, desconsidere essas classes.
