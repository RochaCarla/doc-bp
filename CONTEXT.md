# Brasil Participativo — Documentação Técnica

Documentação técnica do Brasil Participativo, plataforma de participação digital do governo federal brasileiro, baseada no Decidim 0.27.2. O foco é o core (`decidim-govbr`); componentes customizados são documentados como periféricos.

Repositório core: https://gitlab.com/lappis-unb/decidimbr/decidim-govbr
Repositório de componentes: https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo
Produção: https://brasilparticipativo.presidencia.gov.br/
Fontes institucionais: páginas "Sobre o Brasil Participativo" (`/processes/brasilparticipativo/f/1400/`) e "Sobre os Processos Participativos" (`/processes/brasilparticipativo/f/1401/`)

## Language

### Plataforma

**Brasil Participativo**:
Plataforma de participação digital do governo federal. Cidadãos com conta gov.br enviam e votam propostas e participam de consultas, conferências, planos, formulários e enquetes de ministérios e órgãos federais.
_Avoid_: BP (ambíguo)

**Secretaria Nacional de Participação Social (SNPS)**:
Unidade da Secretaria-Geral da Presidência da República que administra a plataforma.

**LabLivre/UnB**:
Laboratório de Competência em Software Livre da UnB, responsável pelo desenvolvimento. Os repositórios ficam no grupo GitLab `lappis-unb` (identificador de URL, não altere).

**Dataprev**:
Empresa pública que hospeda a plataforma em produção.

**ColaboraGov**:
Iniciativa do Ministério da Gestão e da Inovação em Serviços Públicos que apoia a plataforma.

**Decidim**:
Framework open source de democracia participativa escrito em Ruby on Rails. O core usa o Decidim 0.27.2.
_Avoid_: plataforma base (genérico)

**decidim-govbr**:
Repositório core do Brasil Participativo. Aplicação Decidim que sobrescreve diretamente models, controllers, views, comandos e permissões do upstream.
_Avoid_: instância Decidim, app Decidim

**Módulo Decidim**:
Componente nativo do Decidim upstream (propostas, reuniões, formulários, blog, orçamento, debates, páginas, accountability, sorteios).
_Avoid_: plugin, componente (ambíguo, confunde com customizado)

**Componente customizado**:
Gem Ruby desenvolvida pelo LabLivre/UnB que estende o Decidim. Cada componente é um Rails Engine instalado no core via Gemfile.
_Avoid_: plugin, módulo (reservado para os nativos do Decidim)

### Modalidades de participação (vocabulário de produção)

**Processo participativo**:
"Mecanismo institucional de interlocução entre a administração pública e os cidadãos para elaboração, execução, monitoramento ou avaliação de leis, projetos e políticas públicas." No Decidim, espaço com fases temporais. Em produção é classificado por tipo de processo.

**Consulta Pública**:
Processo participativo (tipo 1) de natureza consultiva, com prazo determinado e aberto a qualquer pessoa.

**Conferência**:
Processo participativo (tipo 2) de debate entre poder público e sociedade civil, com etapas municipal, estadual e nacional e eleição de delegados.
_Avoid_: confundir com o espaço `decidim-conferences` do Decidim

**Plano Participativo**:
Processo participativo (tipo 3) de planejamento de médio ou longo prazo construído com a sociedade civil.

**Audiência Pública**:
Processo participativo (tipo 4).

**Instância**:
Nome de produção para a assembleia do Decidim (`Decidim::Assembly`). Agrupa **Conselhos e Colegiados** (`/assemblies`) e **Fóruns de Participação** (`/assemblies/fps`). Órgãos públicos e setores viram instâncias e sub-instâncias automaticamente.
_Avoid_: assembleia (em texto voltado ao usuário)

**Conselho / Colegiado**:
Instância formal e permanente, com representação paritária entre governo e sociedade civil, de caráter consultivo, deliberativo, fiscalizador ou normativo.

**Fórum de Participação**:
Instância flexível de articulação da sociedade civil, temporária ou permanente, sem poder normativo necessário.

**Proposta**:
Contribuição de um participante dentro de um componente de propostas. Pode ser votada, comentada e moderada.

**OP (Orçamento Participativo)**:
Uso do componente de propostas com listagem e votação customizadas. A integração **OP-BP** vincula a conta do participante a um canal de mensagens (WhatsApp/Telegram).

### Componentes customizados instalados no core

**decidim-homes**: página inicial customizada (também usada como componente `homes` dentro das instâncias).
**decidim-enhanced_process_groups_and_scopes**: agrupamento e escopos de processos.
**decidim-ej**: integração com o Empurrando Juntas.
**decidim-extra_user_fields**: campos extras no cadastro de usuário.
**decidim-mobile**: suporte ao app móvel (repositório `bp-mobile`).

Repositórios existentes no grupo de componentes mas **não** instalados no Gemfile do core: `decidim-module-enhanced_templates`, `decidim-module-common_questions`, `decidim-module-questionnaires`, `decidim-participatory_text`. O `decidim-api-categorization` foi removido do core em junho de 2026.

**Empurrando Juntas (EJ)**:
Plataforma externa de opinião e votação desenvolvida pelo LabLivre/UnB. O Brasil Participativo se integra via API, não embute nem reimplementa o EJ.
_Avoid_: EJ interno, módulo EJ

### Arquitetura

**Engine Rails**:
Padrão usado pelo Decidim para modularizar componentes. Cada componente é um Rails Engine empacotado como gem.

**Decidim module generator**:
Ferramenta CLI do Decidim para scaffolding de novos componentes (`decidim-generators`).

**Login externo**:
Fluxo `/external_auth/link` que vincula a conta gov.br a um usuário da API OP-BP usando JWT HS256.

### Infraestrutura

**Ambiente de produção**:
Hospedado pela Dataprev. A aplicação roda Puma (web), Sidekiq (jobs) e tarefas agendadas via `whenever`, com PostgreSQL e dois Redis (fila e cache). Autenticação via gov.br (OpenID Connect).

## Example Dialogue

> **Dev externo**: "Quero contribuir com o Brasil Participativo. Por onde começo?"
>
> **Domain Expert**: "O core é o `decidim-govbr`. Suba o ambiente com `docker compose up`, crie a organização em `/system` e veja a seção de como contribuir. MRs vão para `develop`. Um componente novo vai num repositório próprio dentro do grupo `components-brasil-participativo`."
>
> **Operador**: "Preciso criar um espaço para o conselho do meu ministério."
>
> **Domain Expert**: "Conselhos são instâncias, ou seja, assembleias no Decidim. Se o órgão já está cadastrado como escopo de órgão público, a instância é criada automaticamente pelo job horário. Consultas, conferências, planos e audiências são processos participativos com o tipo correspondente."
