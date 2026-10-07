# Brasil Participativo — Documentação Técnica

Documentação técnica, manual de uso e pacote de transferência do Brasil Participativo, a plataforma de participação digital do governo federal, construída sobre o Decidim 0.27.2. Este glossário fixa a linguagem usada no site, no e-book, na [SPEC.md](./SPEC.md) e no código dos geradores.

- Core: https://gitlab.com/lappis-unb/decidimbr/decidim-govbr
- Componentes: https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo
- Produção: https://brasilparticipativo.presidencia.gov.br/
- Documentação: https://rochacarla.github.io/doc-bp/

## Language

### Instituições

**Brasil Participativo**:
Plataforma de participação digital do governo federal. Cidadãos com conta **gov.br** enviam e votam propostas e participam de consultas, conferências, planos, formulários e enquetes de ministérios e órgãos federais.
_Avoid_: BP (só em nomes técnicos, como OP-BP)

**Secretaria Nacional de Participação Social (SNPS)**:
Unidade da Secretaria-Geral da Presidência da República que administra a plataforma e é parte do **TED**.
_Avoid_: "a Secretaria" sem o nome completo na primeira menção

**LabLivre/UnB**:
Laboratório de Competência em Software Livre da Universidade de Brasília, que desenvolve a plataforma e esta documentação. Os repositórios continuam no grupo GitLab `lappis-unb`, que é um identificador de URL e não deve ser alterado.
_Avoid_: LAPPIS (nome antigo)

**TED**:
Termo de Execução Descentralizada entre a UnB e a **SNPS**, que viabiliza o desenvolvimento, a manutenção e a documentação da plataforma.
_Avoid_: convênio, contrato

**Dataprev**:
Empresa pública que hospeda a plataforma em produção.

**Equipe receptora**:
A equipe que vai assumir a manutenção e a operação da plataforma ao fim da **transferência de tecnologia** (SNPS, Dataprev ou outra designada).
_Avoid_: "governo" (genérico), "cliente"

### Plataforma e código

**Decidim**:
Framework de democracia participativa em Ruby on Rails, criado pela Prefeitura de Barcelona. O core usa a versão 0.27.2.
_Avoid_: upstream (só em contexto técnico de comparação), plataforma base

**Core (`decidim-govbr`)**:
Repositório principal: uma aplicação Rails que instala as gems do Decidim e altera o comportamento delas por **sobrescrita**.
_Avoid_: fork do Decidim (o core não é um fork das gems), instância Decidim

**Sobrescrita**:
Arquivo do core com o mesmo caminho de um arquivo de uma gem do Decidim; o Rails carrega a versão do core. São 492 em relação ao Decidim 0.27.2 e o principal custo de atualização.
_Avoid_: patch, customização (genérico), override

**Módulo Decidim**:
Funcionalidade nativa do Decidim distribuída como gem: propostas, reuniões, formulários, blog, orçamentos, debates, páginas, accountability, sorteios.
_Avoid_: plugin, componente customizado

**Componente**:
Funcionalidade adicionada a um **espaço participativo** pelo painel: propostas, reuniões, formulário, **Página Inicial**, EJ etc. Registrado em `decidim_components`.
_Avoid_: módulo, gem (quando se fala do item no painel)

**Componente customizado**:
Gem desenvolvida pelo LabLivre que estende o Decidim. Pode estar **instalada no core** (no `Gemfile`: homes, enhanced_process_groups_and_scopes, ej, extra_user_fields, mobile) ou **não instalada** (existe no grupo, mas não roda em produção).
_Avoid_: plugin, módulo

**Produção**:
O que está publicado em brasilparticipativo.presidencia.gov.br; em outubro de 2026, a **versão estável** v1.9.2, identificada pelo rodapé do site.
_Avoid_: "a main" como sinônimo de produção

**Versão estável / versão candidata**:
Tags do core: `vX.Y.Z` vai para produção; `vX.Y.Z-rc.N` vai para homologação.
_Avoid_: release (sem qualificar), build

### Participação

**Espaço participativo**:
Contêiner onde a participação acontece: um **processo participativo** ou uma **instância**.
_Avoid_: espaço (sozinho), página

**Processo participativo**:
"Mecanismo institucional de interlocução entre a administração pública e os cidadãos para elaboração, execução, monitoramento ou avaliação de leis, projetos e políticas públicas." No Decidim, espaço com **etapas**. Classificado por **tipo de processo**.
_Avoid_: consulta (quando não for o tipo Consulta Pública), campanha

**Tipo de processo**:
Classificação que define em qual menu o processo aparece: Consulta Pública (1), Conferência (2), Plano Participativo (3) e Audiência Pública (4).
_Avoid_: categoria (é outra coisa no Decidim)

**Modalidade de participação**:
Cada item do menu de produção: Consultas Públicas, Conferências, Planos Participativos, Audiências Públicas, Conselhos e Colegiados, Fóruns de Participação.
_Avoid_: tipo de espaço

**Instância**:
Nome, na interface, da assembleia do Decidim (`Decidim::Assembly`). Abriga Conselhos e Colegiados e Fóruns de Participação. Órgãos públicos viram instâncias e seus setores, sub-instâncias, de hora em hora.
_Avoid_: assembleia (em texto voltado ao usuário)

**Etapa**:
Fase de um processo participativo, com período definido. A etapa ativa muda sozinha conforme as datas.
_Avoid_: fase (aceitável em texto explicativo), step (só no código)

**Proposta**:
Contribuição de um participante num componente de propostas; pode ser votada, comentada e moderada.

**Texto participativo**:
Documento dividido em parágrafos, cada um aberto a comentários. É um recurso do componente de propostas (cada parágrafo é uma proposta), com **renderização leve** para textos publicados a partir da data de corte v2.
_Avoid_: confundir com a gem `decidim-participatory_text`, que não está instalada

**Página Inicial (componente)**:
Componente `homes` que monta a vitrine de um processo ou instância com blocos.
_Avoid_: home (reservado para a página inicial do site)

**Devolutiva**:
Retorno do poder público aos participantes. Na interface, também nomeia a exportação de relatórios de participação.
_Avoid_: feedback

**Votos mutuamente exclusivos**:
Opção do processo que impede votar em mais de um componente de propostas do mesmo processo.

**Orçamento do Povo**:
O orçamento participativo federal, com participação pela web, por WhatsApp e Telegram e presencial. É objeto do primeiro **estudo**.
_Avoid_: "OP" em texto corrido

### Integrações

**gov.br**:
Login Único do governo federal, usado via OpenID Connect. Para o gov.br, o CPF fica em `decidim_identities.uid`.

**Login externo**:
Fluxo `/external_auth/link` que vincula a conta gov.br ao participante que chegou por WhatsApp ou Telegram, a partir de um JWT assinado.
_Avoid_: login social, SSO

**API OP-BP**:
Sistema externo que conduz a participação por mensageria, gera o link do login externo e recebe o callback do vínculo.
_Avoid_: bot (é só uma das partes), N8N (implementação anterior)

**Impersonação**:
Autenticação por cabeçalhos `X-API-KEY` e `X-USER-ID`, com a qual a API OP-BP age em nome de um participante vinculado.
_Avoid_: login por API

**Empurrando Juntas (EJ)**:
Plataforma externa de conversas e opiniões, integrada pelo componente `decidim-ej`.
_Avoid_: módulo EJ, EJ interno

### Documentação

**Página gerada**:
Página produzida por um script em `scripts/` e marcada com "Não edite à mão": Estatísticas, Banco de Dados (exceto Consultas úteis) e Inventário de sobrescritas.
_Avoid_: página automática, relatório

**Série analisada**:
Recorte temporal das Estatísticas: a partir de 01/04/2023.
_Avoid_: histórico completo

**Fator de ausência**:
Menor número de pessoas que somam metade dos commits (*Contributor Absence Factor*, CHAOSS).
_Avoid_: bus factor (em texto corrido)

**A confirmar**:
Marca de informação que não está no código nem em fonte pública e precisa ser levantada com a equipe atual. Nunca é preenchida por suposição.
_Avoid_: TBD, a definir

**Medido / inferido**:
Rótulos de afirmações de desempenho: *medido* é número publicado num merge request; *inferido* é conclusão da leitura do código.

**Transferência de tecnologia**:
Processo, em cinco fases, de passagem da plataforma do LabLivre para a **equipe receptora**, com pacote de documentos e critérios de aceite.
_Avoid_: handover, repasse (repasse é só a fase de capacitação)

**Estudo**:
Análise sobre a participação na plataforma, publicada com ficha (questão, tipo, período, fontes, método, resultados, limitações, situação).
_Avoid_: relatório (é o documento original), pesquisa

**Trilha de aprendizado**:
Sequência de leitura recomendada para um perfil.
_Avoid_: tutorial

**E-book**:
Versão em PDF de todo o site, exceto a home, com capa, folha de rosto, apresentação, sumário, miolo numerado e contracapa.
_Avoid_: exportação, impressão

**Rodapé institucional**:
Faixa com Realização (LabLivre e UnB) e Parceria (Secretaria) no fim de toda página, configurada em `extra.institucional`.
_Avoid_: rodapé (sozinho, ambíguo com o rodapé de página e o do e-book)

## Flagged ambiguities

**"main" × produção**: até a v1.9.1 as tags ficavam em `main`; a partir da v1.9.2 ficam na linha de `develop` e de branches `deploy-v*`, e as duas branches divergiram. Termo canônico: **produção** é a versão no rodapé do site oficial; `main` é só o nome de uma branch.

**"Conferência"**: no menu de produção, é um **tipo de processo** (processo participativo tipo 2). O Decidim também tem o espaço `decidim-conferences`, instalado mas não usado nesse menu. Termo canônico: **Conferência** = tipo de processo; o espaço do Decidim é citado pelo nome da gem.

**"Instância" × "assembleia"**: são a mesma coisa. **Instância** na interface e no texto para usuários; `Assembly`/assembleia só em código e no Banco de Dados.

**"Componente"**: no painel, é o item adicionado a um espaço; no repositório, "componente customizado" é uma gem. Sempre qualifique: **componente** (painel) ou **componente customizado** (gem).

**"Texto participativo"**: o recurso em produção é o do componente de propostas, com sobrescritas no core; a gem `decidim-participatory_text` existe no grupo, mas não está instalada.

**"Devolutiva"**: na política pública, é o retorno aos participantes; na interface, é também o nome da exportação de relatórios. Explicite qual dos dois.

**"OP"**: aparece no código (`op_custom_index`), na **API OP-BP** e nos documentos do projeto para o orçamento participativo federal. Termo canônico: **Orçamento do Povo** em texto corrido; "OP" só em nomes técnicos.

**"Fork"**: a documentação antiga chamava o core de "fork direto do Decidim". Termo canônico: **core com sobrescritas**; ele instala as gems do Decidim em vez de copiar o repositório.

## Example dialogue

> **Equipe receptora**: Queremos corrigir um defeito e publicar. Partimos da `main`, que é a produção, certo?
>
> **Especialista**: Não necessariamente. **Produção** é o que aparece no rodapé do site, hoje a v1.9.2, e essa tag está na linha de `develop`, não em `main`. Antes de qualquer coisa, reconciliem as branches e combinem o fluxo de **versões estáveis** e **candidatas**.
>
> **Equipe receptora**: E o defeito está numa tela de propostas. Mexemos na gem do Decidim?
>
> **Especialista**: Nunca na gem. Veja se o arquivo já é uma **sobrescrita** no core; o inventário lista as 492. Se for, a correção vai lá, com teste. Se não for, avalie se dá para resolver sem criar mais uma sobrescrita.
>
> **Equipe receptora**: O gestor pediu um espaço para o conselho do ministério. É um processo?
>
> **Especialista**: Conselhos são **instâncias**. Se o órgão já está cadastrado como escopo de órgão público, a instância aparece sozinha na próxima hora. Processos são para consultas, conferências, planos e audiências, cada um com seu **tipo de processo**.
>
> **Equipe receptora**: E essa história de WhatsApp?
>
> **Especialista**: A **API OP-BP** conduz a conversa e manda o link do **login externo**. Depois do vínculo, ela usa a **impersonação** para votar em nome do participante, e esse é o ponto de segurança mais sensível que vocês vão herdar.
