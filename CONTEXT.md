# Brasil Participativo — Documentação Técnica

Documentação técnica da plataforma Brasil Participativo, plataforma nacional de participação social digital do governo federal brasileiro, baseada no Decidim. O foco é o core (`decidim-govbr`); componentes customizados são documentados como periféricos.

Repositório core: https://gitlab.com/lappis-unb/decidimbr/decidim-govbr
Repositório de componentes: https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo

## Language

### Plataforma

**Brasil Participativo**:
Plataforma nacional de participação social digital do governo federal, construída sobre o framework Decidim.
_Avoid_: BP (ambíguo)

**Decidim**:
Framework open source de democracia participativa escrito em Ruby on Rails. O Brasil Participativo é um fork direto do Decidim com modificações no código upstream.
_Avoid_: plataforma base (genérico)

**decidim-govbr**:
Repositório core do Brasil Participativo. Fork do Decidim com customizações diretas no código-fonte — não é uma instância que apenas consome gems oficiais.
_Avoid_: instância Decidim, app Decidim

**Módulo Decidim**:
Componente nativo que já vem com o Decidim upstream (ex: propostas, reuniões, formulários, blog, enquetes, orçamento participativo). O Brasil Participativo usa um subconjunto desses módulos.
_Avoid_: plugin, componente (ambíguo — confunde com customizado)

**Componente customizado**:
Gem Ruby desenvolvida pelo LAPPIS/UnB que estende o Decidim além dos módulos oficiais. Cada componente é um Rails Engine instalado no core via Gemfile.
_Avoid_: plugin, módulo (reservado para os nativos do Decidim)

### Componentes Customizados

**decidim-module-homes**:
Página inicial customizada da plataforma.

**decidim-module-enhanced_templates**:
Templates melhorados para processos participativos.

**decidim-module-enhanced_process_groups_and_scopes**:
Agrupamento e escopos de processos participativos (ex: por região, tema).

**decidim-module-common_questions**:
Perguntas frequentes compartilhadas entre processos.

**decidim-module-questionnaires**:
Customização do módulo de questionários do Decidim.

**decidim-participatory_text**:
Fork/customização do componente oficial de textos participativos do Decidim.

**decidim-api-categorization**:
Extensão de API para categorização de conteúdos.

**decidim-ej**:
Integração com Empurrando Juntas (EJ) — consome a API do EJ e exibe resultados no Decidim com UI própria. EJ é uma dependência externa.

**Empurrando Juntas (EJ)**:
Plataforma externa de opinião e votação desenvolvida pelo LAPPIS/UnB. O Brasil Participativo se integra via API, não embute nem reimplementa o EJ.
_Avoid_: EJ interno, módulo EJ

### Conceitos de Participação

**Espaço participativo**:
Container organizacional no Decidim (processo participativo, assembleia, conferência) que agrupa componentes.
_Avoid_: espaço (genérico)

**Processo participativo**:
Tipo de espaço com fases temporais (criação, debate, votação, resultado). Principal mecanismo do Brasil Participativo.

**Proposta**:
Contribuição de um participante dentro de um componente de propostas. Pode ser votada, comentada e moderada.

### Arquitetura

**Engine Rails**:
Padrão usado pelo Decidim para modularizar componentes — cada componente é um Rails Engine empacotado como gem.

**Decidim module generator**:
Ferramenta CLI do Decidim para scaffolding de novos componentes (`decidim-generators`).

### Infraestrutura

**Ambiente de produção**:
Kubernetes. Demais dependências externas (banco, cache, e-mail, autenticação, etc.) a detalhar.

## Example Dialogue

> **Dev externo**: "Quero contribuir com o Brasil Participativo. Por onde começo?"
>
> **Domain Expert**: "O core é o `decidim-govbr` — um fork direto do Decidim. Clone o repo, siga o setup local e veja a seção de como contribuir. Se quiser criar um componente customizado novo, ele vai no repositório `components-brasil-participativo` como uma gem Ruby separada."
>
> **Operador**: "Preciso subir uma instância do Brasil Participativo no meu órgão."
>
> **Domain Expert**: "A plataforma roda em Kubernetes. O Guia do Operador cobre deploy e configuração. Atenção às dependências externas — o EJ é consumido via API e precisa estar disponível separadamente."
