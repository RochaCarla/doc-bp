---
title: Glossário
---

<!-- Gerado por scripts/glossario.py a partir do CONTEXT.md. Não edite à mão: edite o CONTEXT.md. -->

# Glossário

Linguagem oficial do Brasil Participativo e desta documentação: 50 termos, com as palavras a evitar e as ambiguidades já resolvidas. Use estes termos em textos, telas e código.

!!! info "Fonte única"
    Esta página é gerada a partir do `CONTEXT.md` do repositório. Para mudar um termo, edite o `CONTEXT.md` e rode `python3 scripts/glossario.py`.

## Instituições

Brasil Participativo
:   Plataforma de participação digital do governo federal, na qual **participantes** atuam em **processos participativos** e **instâncias** de ministérios e órgãos federais.

    *Evite:* BP (só em nomes técnicos, como OP-BP)

Secretaria Nacional de Participação Social (SNPS)
:   Unidade da Secretaria-Geral da Presidência da República que administra o **Brasil Participativo** e é parte do **TED**.

    *Evite:* "a Secretaria" sem o nome completo na primeira menção

LabLivre/UnB
:   Laboratório de Competência em Software Livre da Universidade de Brasília, que desenvolve a plataforma e esta documentação.

    *Evite:* LAPPIS (nome antigo)

TED
:   Termo de Execução Descentralizada entre a UnB e a **SNPS**, que viabiliza o desenvolvimento, a manutenção e a documentação da plataforma.

    *Evite:* convênio, contrato

Dataprev
:   Empresa pública que hospeda o **Brasil Participativo** em **produção**.

## Pessoas e papéis

Participante
:   Pessoa com conta **gov.br** na plataforma que participa de um **espaço participativo**: propõe, vota, comenta ou responde formulários.

    *Evite:* usuário (só ao contar contas, em rótulos da interface e ao falar do código ou do banco), cidadão (só em nomes oficiais e para o público em geral, com ou sem conta)

Gestor de processo
:   Servidor de um órgão que cria, publica e acompanha **espaços participativos** pelo painel da plataforma, com o **papel** de administrador de espaço.

    *Evite:* administrador (é o papel, não a pessoa), admin

Equipe de operação
:   Equipe técnica que implanta, configura, monitora e recupera a plataforma.

    *Evite:* operador (na LGPD, é quem trata dados em nome do controlador), sysadmin

Equipe receptora
:   Equipe que assume a manutenção e a operação da plataforma ao fim da **transferência de tecnologia**.

    *Evite:* "governo" (genérico), cliente

Papel
:   Nível de acesso de uma pessoa aos painéis da plataforma: administrador de sistema, administrador da organização, administrador de espaço, moderador, avaliador ou colaborador.

    *Evite:* perfil (é a página pública do participante)

## Plataforma e código

Decidim
:   Software livre de democracia participativa, base do **Brasil Participativo**.

    *Evite:* upstream (só ao comparar código), plataforma base

Core
:   Repositório principal do **Brasil Participativo** (`decidim-govbr`): uma aplicação que instala o **Decidim** e altera seu comportamento por **sobrescritas**.

    *Evite:* fork do Decidim, instância Decidim

Sobrescrita
:   Arquivo do **core** que substitui o arquivo de mesmo caminho numa gem do **Decidim**; é o principal custo de atualização.

    *Evite:* patch, override, customização (genérico)

Módulo Decidim
:   Funcionalidade nativa do **Decidim**, como propostas, reuniões e formulários.

    *Evite:* plugin, componente customizado

Componente
:   Funcionalidade adicionada pelo painel a um **espaço participativo**, como um conjunto de propostas ou uma **Página Inicial**.

    *Evite:* módulo, gem

Componente customizado
:   Extensão do **Decidim** desenvolvida pelo **LabLivre/UnB**; pode estar instalada no **core** ou apenas existir no grupo de componentes.

    *Evite:* plugin, módulo

Organização
:   Instalação lógica do **Brasil Participativo**, identificada por um endereço, que reúne participantes, **espaços participativos** e configurações.

    *Evite:* tenant, site, instância (é outro conceito)

Produção
:   A versão do **Brasil Participativo** publicada no site oficial, identificada pelo rodapé.

    *Evite:* "a main" como sinônimo de produção

Versão estável
:   Versão liberada para **produção**.

    *Evite:* release (sem qualificar)

Versão candidata
:   Versão em homologação antes de se tornar **versão estável**.

    *Evite:* beta, build

## Participação

Espaço participativo
:   Lugar onde a participação acontece: um **processo participativo** ou uma **instância**. Um espaço tem muitos **componentes**.

    *Evite:* espaço (sozinho), página

Processo participativo
:   Mecanismo institucional de interlocução entre a administração pública e os cidadãos para elaborar, executar, monitorar ou avaliar leis, projetos e políticas públicas. Tem **etapas** e um **tipo de processo**.

    *Evite:* campanha, consulta (quando não for Consulta Pública)

Tipo de processo
:   Classificação de um **processo participativo** em Consulta Pública, Conferência, Plano Participativo ou Audiência Pública.

    *Evite:* categoria (é outro conceito do Decidim)

Modalidade de participação
:   Cada forma de participação oferecida no menu da plataforma: os quatro **tipos de processo**, Conselhos e Colegiados e Fóruns de Participação.

    *Evite:* tipo de espaço

Instância
:   **Espaço participativo** permanente de um **órgão**, como um conselho, colegiado ou fórum. Pode ter sub-instâncias, uma por **setor** do órgão.

    *Evite:* assembleia (só ao falar do código ou do banco)

Órgão
:   Órgão público federal cadastrado na plataforma. Cada órgão ganha uma **instância** própria, criada automaticamente.

    *Evite:* escopo (é o mecanismo do Decidim que guarda o cadastro), public body

Setor
:   Unidade de um **órgão**. Cada setor ganha uma sub-instância dentro da **instância** do órgão.

    *Evite:* subescopo

Etapa
:   Fase de um **processo participativo**, com período definido.

    *Evite:* step (só no código)

Proposta
:   Contribuição de um participante, que pode ser votada, comentada e moderada.

Texto participativo
:   Documento dividido em parágrafos, cada um aberto a comentários, publicado num **componente** de propostas.

    *Evite:* minuta (só quando o documento de fato for uma minuta)

Página Inicial
:   **Componente** que monta, com blocos, a vitrine de um **espaço participativo**.

    *Evite:* home (reservado para a página inicial do site)

Moderação
:   Análise e ocultação de conteúdo que viola os termos de uso da plataforma.

    *Evite:* censura, remoção (o conteúdo é ocultado, não apagado)

Devolutiva
:   Retorno do poder público aos participantes sobre o que foi feito com a participação.

    *Evite:* feedback

Votos mutuamente exclusivos
:   Regra de um **processo participativo** que limita o participante a votar em um único **componente** de propostas do processo.

Orçamento do Povo
:   Orçamento participativo federal, com participação pela web, por mensageria e presencial.

    *Evite:* "OP" em texto corrido

## Integrações

gov.br
:   Login Único do governo federal, a identidade exigida para participar.

Login externo
:   Vínculo entre a conta **gov.br** e o participante que chegou por WhatsApp ou Telegram.

    *Evite:* login social, SSO

API OP-BP
:   Sistema externo que conduz a participação por mensageria e pede o **login externo**.

    *Evite:* bot (é só uma parte), N8N (implementação anterior)

Impersonação
:   Acesso pelo qual a **API OP-BP** age em nome de um participante já vinculado.

    *Evite:* login por API

Empurrando Juntas (EJ)
:   Plataforma externa de conversas e opiniões, integrada ao **Brasil Participativo** por um **componente customizado**.

    *Evite:* módulo EJ, EJ interno

## Documentação

Página gerada
:   Página da documentação produzida automaticamente a partir do código e de fontes públicas, e que não se edita à mão.

    *Evite:* página automática, relatório

Série analisada
:   Período coberto pelas estatísticas do projeto, a partir de abril de 2023.

    *Evite:* histórico completo

Fator de ausência
:   Menor número de pessoas que somam metade das contribuições de código.

    *Evite:* bus factor (em texto corrido)

A confirmar
:   Marca de informação sem fonte verificável, que precisa ser levantada com a equipe atual.

    *Evite:* TBD, a definir

Medido / inferido
:   Qualificação de uma afirmação de desempenho: *medido* quando há número publicado; *inferido* quando é conclusão da leitura do código.

Transferência de tecnologia
:   Passagem da plataforma do **LabLivre/UnB** para a **equipe receptora**, em fases, com critérios de aceite.

    *Evite:* handover, repasse (repasse é só a fase de capacitação)

Estudo
:   Análise sobre a participação na plataforma, publicada com uma ficha padronizada.

    *Evite:* relatório (é o documento de origem), pesquisa

Trilha de aprendizado
:   Sequência de leitura recomendada para um perfil de leitor.

    *Evite:* tutorial

E-book
:   Versão em PDF, autônoma, de todo o conteúdo da documentação.

    *Evite:* exportação, impressão

Rodapé institucional
:   Faixa no fim de toda página que identifica quem realiza a documentação e quem é parceiro.

    *Evite:* rodapé (sozinho)

## Ambiguidades resolvidas

Palavras que aparecem com mais de um sentido no projeto, e o sentido que vale.

- **"main" × produção**: as versões em **produção** deixaram de ser marcadas na branch `main`, e as branches divergiram. Termo canônico: **produção** é o que está publicado no site oficial; `main` é só o nome de uma branch.
- **"Conferência"**: no menu da plataforma, é um **tipo de processo**. O **Decidim** também tem um espaço chamado conferência, que não é o usado nesse menu. Termo canônico: **Conferência** = tipo de processo.
- **"Instância" × "assembleia"**: são o mesmo conceito. **Instância** em todo texto para leitores; assembleia só ao falar do código ou do banco.
- **"Componente"**: no painel, é o item adicionado a um espaço; no repositório, a palavra também designa gems. Sempre qualifique: **componente** ou **componente customizado**.
- **"Texto participativo"**: o recurso em uso é o do **componente** de propostas. Existe também um **componente customizado** de mesmo nome, que não está instalado.
- **"Devolutiva"**: na política pública, é o retorno aos participantes; na interface da plataforma, também nomeia a exportação de relatórios. Explicite qual dos dois.
- **"OP"**: aparece em nomes técnicos e nos documentos do projeto para o **Orçamento do Povo**. Termo canônico: **Orçamento do Povo** em texto corrido.
- **"Orçamento participativo"**: com minúscula, é a prática de participação em geral. O **módulo Decidim** de votação de projetos com teto de gastos se chama **Orçamentos**, e o **Orçamento do Povo** não o usa: nele, os participantes votam em **propostas**. Termo canônico: **Orçamento do Povo** para o programa federal; **Orçamentos** para o módulo.
- **"Prestação de contas" × "devolutiva"**: **Prestação de contas** é o **módulo Decidim** que acompanha a execução dos resultados da participação; "accountability" fica só no nome da gem. A **devolutiva** é o retorno aos participantes e pode usar esse módulo, mas não se resume a ele. Em texto corrido, "prestação de contas" também é o dever geral de transparência do poder público. Termo canônico: **módulo Prestação de contas** para o módulo; **devolutiva** para o retorno.
- **"Administrador"**: nomeia três **papéis**, de sistema, da organização e de espaço, e era usado também para a pessoa que conduz o processo. Termo canônico: qualifique sempre o papel (por exemplo, administrador de espaço); para a pessoa, use **gestor de processo** ou **equipe de operação**.
- **"Escopo"**: no **Decidim**, classifica conteúdo por território ou tema; no **Brasil Participativo**, também guarda o cadastro de **órgãos** e **setores**. A palavra ainda aparece no login **gov.br** (escopo de autorização) e no sentido comum. Termo canônico: **órgão** e **setor** para o cadastro institucional; "escopo" só para a classificação do Decidim ou para a autorização, sempre qualificado.
- **"Fork"**: a documentação antiga chamava o **core** de "fork do Decidim". Termo canônico: **core com sobrescritas**, porque ele instala o Decidim em vez de copiar seu repositório.

??? example "Diálogo de exemplo"

    > **Equipe receptora**: Queremos corrigir um defeito e publicar. Partimos da `main`, que é a produção, certo?
    >
    > **Especialista**: Não. **Produção** é o que está publicado no site oficial, e essa versão não está marcada na `main`. Antes, reconciliem as branches e combinem como uma **versão candidata** vira **versão estável**.
    >
    > **Equipe receptora**: O defeito está numa tela de propostas. Corrigimos no **Decidim**?
    >
    > **Especialista**: Nunca no Decidim. Vejam se o arquivo já é uma **sobrescrita** no **core**. Se for, a correção vai nela, com teste. Se não for, avaliem se dá para resolver sem criar mais uma sobrescrita.
    >
    > **Equipe receptora**: Um **gestor de processo** pediu um espaço para o conselho do ministério. É um **processo participativo**?
    >
    > **Especialista**: Conselhos são **instâncias**, e a instância do órgão é criada automaticamente. Processos servem a consultas, conferências, planos e audiências, cada um com seu **tipo de processo**.
    >
    > **Equipe receptora**: E a participação pelo WhatsApp?
    >
    > **Especialista**: A **API OP-BP** conduz a conversa e pede o **login externo**. Depois do vínculo, ela usa a **impersonação** para agir em nome do participante. É o ponto de segurança mais sensível que vocês vão herdar.

## Termos técnicos

Conceitos gerais de tecnologia usados nesta documentação.

Rails Engine
:   Mini-aplicação Rails empacotada como gem. O Decidim e seus módulos são formados por engines.

Command, Form, Cell, Permission
:   Padrões de código do Decidim: regra de negócio, validação de entrada, componente de interface e regra de acesso. Veja [Arquitetura › Camadas](arquitetura.md#camadas).

Sidekiq
:   Processador de tarefas em segundo plano, que usa o Redis como fila.

whenever
:   Gem que transforma `config/schedule.rb` em tarefas do cron.

Design System gov.br
:   Padrão visual do governo federal, aplicado à interface da plataforma. Veja [Design System gov.br](../design-system/index.md).

VLibras
:   Ferramenta do governo federal que traduz conteúdo para Libras.

Mermaid
:   Linguagem de diagramas em texto usada nesta documentação.
