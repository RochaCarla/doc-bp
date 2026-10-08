# Brasil Participativo — Documentação Técnica

Linguagem do Brasil Participativo, a plataforma de participação digital do governo federal construída sobre o Decidim, e da documentação que a descreve. Os detalhes de implementação estão na [SPEC.md](./SPEC.md) e no site.

## Language

### Instituições

**Brasil Participativo**:
Plataforma de participação digital do governo federal, na qual **participantes** atuam em **processos participativos** e **instâncias** de ministérios e órgãos federais.
_Avoid_: BP (só em nomes técnicos, como OP-BP)

**Secretaria Nacional de Participação Social (SNPS)**:
Unidade da Secretaria-Geral da Presidência da República que administra o **Brasil Participativo** e é parte do **TED**.
_Avoid_: "a Secretaria" sem o nome completo na primeira menção

**LabLivre/UnB**:
Laboratório de Competência em Software Livre da Universidade de Brasília, que desenvolve a plataforma e esta documentação.
_Avoid_: LAPPIS (nome antigo)

**TED**:
Termo de Execução Descentralizada entre a UnB e a **SNPS**, que viabiliza o desenvolvimento, a manutenção e a documentação da plataforma.
_Avoid_: convênio, contrato

**Dataprev**:
Empresa pública que hospeda o **Brasil Participativo** em **produção**.

**Equipe receptora**:
Equipe que assume a manutenção e a operação da plataforma ao fim da **transferência de tecnologia**.
_Avoid_: "governo" (genérico), cliente

### Plataforma e código

**Decidim**:
Software livre de democracia participativa, base do **Brasil Participativo**.
_Avoid_: upstream (só ao comparar código), plataforma base

**Core**:
Repositório principal do **Brasil Participativo** (`decidim-govbr`): uma aplicação que instala o **Decidim** e altera seu comportamento por **sobrescritas**.
_Avoid_: fork do Decidim, instância Decidim

**Sobrescrita**:
Arquivo do **core** que substitui o arquivo de mesmo caminho numa gem do **Decidim**; é o principal custo de atualização.
_Avoid_: patch, override, customização (genérico)

**Módulo Decidim**:
Funcionalidade nativa do **Decidim**, como propostas, reuniões e formulários.
_Avoid_: plugin, componente customizado

**Componente**:
Funcionalidade adicionada pelo painel a um **espaço participativo**, como um conjunto de propostas ou uma **Página Inicial**.
_Avoid_: módulo, gem

**Componente customizado**:
Extensão do **Decidim** desenvolvida pelo **LabLivre/UnB**; pode estar instalada no **core** ou apenas existir no grupo de componentes.
_Avoid_: plugin, módulo

**Organização**:
Instalação lógica do **Brasil Participativo**, identificada por um endereço, que reúne participantes, **espaços participativos** e configurações.
_Avoid_: tenant, site, instância (é outro conceito)

**Produção**:
A versão do **Brasil Participativo** publicada no site oficial, identificada pelo rodapé.
_Avoid_: "a main" como sinônimo de produção

**Versão estável**:
Versão liberada para **produção**.
_Avoid_: release (sem qualificar)

**Versão candidata**:
Versão em homologação antes de se tornar **versão estável**.
_Avoid_: beta, build

### Participação

**Participante**:
Pessoa com conta **gov.br** na plataforma que participa de um **espaço participativo**: propõe, vota, comenta ou responde formulários.
_Avoid_: usuário (só ao contar contas, em rótulos da interface e ao falar do código ou do banco), cidadão (só em nomes oficiais e para o público em geral, com ou sem conta)

**Espaço participativo**:
Lugar onde a participação acontece: um **processo participativo** ou uma **instância**. Um espaço tem muitos **componentes**.
_Avoid_: espaço (sozinho), página

**Processo participativo**:
Mecanismo institucional de interlocução entre a administração pública e os cidadãos para elaborar, executar, monitorar ou avaliar leis, projetos e políticas públicas. Tem **etapas** e um **tipo de processo**.
_Avoid_: campanha, consulta (quando não for Consulta Pública)

**Tipo de processo**:
Classificação de um **processo participativo** em Consulta Pública, Conferência, Plano Participativo ou Audiência Pública.
_Avoid_: categoria (é outro conceito do Decidim)

**Modalidade de participação**:
Cada forma de participação oferecida no menu da plataforma: os quatro **tipos de processo**, Conselhos e Colegiados e Fóruns de Participação.
_Avoid_: tipo de espaço

**Instância**:
**Espaço participativo** permanente de um órgão, como um conselho, colegiado ou fórum. Pode ter sub-instâncias, uma por setor do órgão.
_Avoid_: assembleia (em texto voltado ao usuário)

**Etapa**:
Fase de um **processo participativo**, com período definido.
_Avoid_: step (só no código)

**Proposta**:
Contribuição de um participante, que pode ser votada, comentada e moderada.

**Texto participativo**:
Documento dividido em parágrafos, cada um aberto a comentários, publicado num **componente** de propostas.
_Avoid_: minuta (só quando o documento de fato for uma minuta)

**Página Inicial**:
**Componente** que monta, com blocos, a vitrine de um **espaço participativo**.
_Avoid_: home (reservado para a página inicial do site)

**Moderação**:
Análise e ocultação de conteúdo que viola os termos de uso da plataforma.
_Avoid_: censura, remoção (o conteúdo é ocultado, não apagado)

**Devolutiva**:
Retorno do poder público aos participantes sobre o que foi feito com a participação.
_Avoid_: feedback

**Votos mutuamente exclusivos**:
Regra de um **processo participativo** que limita o participante a votar em um único **componente** de propostas do processo.

**Orçamento do Povo**:
Orçamento participativo federal, com participação pela web, por mensageria e presencial.
_Avoid_: "OP" em texto corrido

### Integrações

**gov.br**:
Login Único do governo federal, a identidade exigida para participar.

**Login externo**:
Vínculo entre a conta **gov.br** e o participante que chegou por WhatsApp ou Telegram.
_Avoid_: login social, SSO

**API OP-BP**:
Sistema externo que conduz a participação por mensageria e pede o **login externo**.
_Avoid_: bot (é só uma parte), N8N (implementação anterior)

**Impersonação**:
Acesso pelo qual a **API OP-BP** age em nome de um participante já vinculado.
_Avoid_: login por API

**Empurrando Juntas (EJ)**:
Plataforma externa de conversas e opiniões, integrada ao **Brasil Participativo** por um **componente customizado**.
_Avoid_: módulo EJ, EJ interno

### Documentação

**Página gerada**:
Página da documentação produzida automaticamente a partir do código e de fontes públicas, e que não se edita à mão.
_Avoid_: página automática, relatório

**Série analisada**:
Período coberto pelas estatísticas do projeto, a partir de abril de 2023.
_Avoid_: histórico completo

**Fator de ausência**:
Menor número de pessoas que somam metade das contribuições de código.
_Avoid_: bus factor (em texto corrido)

**A confirmar**:
Marca de informação sem fonte verificável, que precisa ser levantada com a equipe atual.
_Avoid_: TBD, a definir

**Medido / inferido**:
Qualificação de uma afirmação de desempenho: *medido* quando há número publicado; *inferido* quando é conclusão da leitura do código.

**Transferência de tecnologia**:
Passagem da plataforma do **LabLivre/UnB** para a **equipe receptora**, em fases, com critérios de aceite.
_Avoid_: handover, repasse (repasse é só a fase de capacitação)

**Estudo**:
Análise sobre a participação na plataforma, publicada com uma ficha padronizada.
_Avoid_: relatório (é o documento de origem), pesquisa

**Trilha de aprendizado**:
Sequência de leitura recomendada para um perfil de leitor.
_Avoid_: tutorial

**E-book**:
Versão em PDF, autônoma, de todo o conteúdo da documentação.
_Avoid_: exportação, impressão

**Rodapé institucional**:
Faixa no fim de toda página que identifica quem realiza a documentação e quem é parceiro.
_Avoid_: rodapé (sozinho)

## Flagged ambiguities

**"main" × produção**: as versões em **produção** deixaram de ser marcadas na branch `main`, e as branches divergiram. Termo canônico: **produção** é o que está publicado no site oficial; `main` é só o nome de uma branch.

**"Conferência"**: no menu da plataforma, é um **tipo de processo**. O **Decidim** também tem um espaço chamado conferência, que não é o usado nesse menu. Termo canônico: **Conferência** = tipo de processo.

**"Instância" × "assembleia"**: são o mesmo conceito. **Instância** em todo texto para leitores; assembleia só ao falar do código ou do banco.

**"Componente"**: no painel, é o item adicionado a um espaço; no repositório, a palavra também designa gems. Sempre qualifique: **componente** ou **componente customizado**.

**"Texto participativo"**: o recurso em uso é o do **componente** de propostas. Existe também um **componente customizado** de mesmo nome, que não está instalado.

**"Devolutiva"**: na política pública, é o retorno aos participantes; na interface da plataforma, também nomeia a exportação de relatórios. Explicite qual dos dois.

**"OP"**: aparece em nomes técnicos e nos documentos do projeto para o **Orçamento do Povo**. Termo canônico: **Orçamento do Povo** em texto corrido.

**"Orçamento participativo"**: com minúscula, é a prática de participação em geral. O **módulo Decidim** de votação de projetos com teto de gastos se chama **Orçamentos**, e o **Orçamento do Povo** não o usa: nele, os participantes votam em **propostas**. Termo canônico: **Orçamento do Povo** para o programa federal; **Orçamentos** para o módulo.

**"Prestação de contas" × "devolutiva"**: **Prestação de contas** é o **módulo Decidim** que acompanha a execução dos resultados da participação; "accountability" fica só no nome da gem. A **devolutiva** é o retorno aos participantes e pode usar esse módulo, mas não se resume a ele. Em texto corrido, "prestação de contas" também é o dever geral de transparência do poder público. Termo canônico: **módulo Prestação de contas** para o módulo; **devolutiva** para o retorno.

**"Fork"**: a documentação antiga chamava o **core** de "fork do Decidim". Termo canônico: **core com sobrescritas**, porque ele instala o Decidim em vez de copiar seu repositório.

## Example dialogue

> **Equipe receptora**: Queremos corrigir um defeito e publicar. Partimos da `main`, que é a produção, certo?
>
> **Especialista**: Não. **Produção** é o que está publicado no site oficial, e essa versão não está marcada na `main`. Antes, reconciliem as branches e combinem como uma **versão candidata** vira **versão estável**.
>
> **Equipe receptora**: O defeito está numa tela de propostas. Corrigimos no **Decidim**?
>
> **Especialista**: Nunca no Decidim. Vejam se o arquivo já é uma **sobrescrita** no **core**. Se for, a correção vai nela, com teste. Se não for, avaliem se dá para resolver sem criar mais uma sobrescrita.
>
> **Equipe receptora**: Um gestor pediu um espaço para o conselho do ministério. É um **processo participativo**?
>
> **Especialista**: Conselhos são **instâncias**, e a instância do órgão é criada automaticamente. Processos servem a consultas, conferências, planos e audiências, cada um com seu **tipo de processo**.
>
> **Equipe receptora**: E a participação pelo WhatsApp?
>
> **Especialista**: A **API OP-BP** conduz a conversa e pede o **login externo**. Depois do vínculo, ela usa a **impersonação** para agir em nome do participante. É o ponto de segurança mais sensível que vocês vão herdar.
