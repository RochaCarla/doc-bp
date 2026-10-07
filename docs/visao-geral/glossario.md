# Glossário

Termos usados no Brasil Participativo e nesta documentação. Quando o nome na interface difere do nome no código, os dois aparecem.

## Plataforma e instituições

Brasil Participativo
:   Plataforma de participação digital do governo federal, construída sobre o Decidim.

Decidim
:   Framework de democracia participativa em Ruby on Rails, criado pela Prefeitura de Barcelona. O Brasil Participativo usa a versão 0.27.2.

`decidim-govbr`
:   Repositório principal (core) do Brasil Participativo. Sobrescreve partes do Decidim para o contexto brasileiro.

SNPS
:   Secretaria Nacional de Participação Social, da Secretaria-Geral da Presidência da República. Administra a plataforma.

LabLivre/UnB
:   Laboratório de Competência em Software Livre da Universidade de Brasília. Desenvolve a plataforma.

TED
:   Termo de Execução Descentralizada. Instrumento de cooperação entre a Secretaria e a UnB. Veja [Sobre](../sobre/index.md).

Dataprev
:   Empresa pública que hospeda a plataforma.

## Participação

Espaço participativo
:   Contêiner onde a participação acontece. No Brasil Participativo, é um **processo participativo** ou uma **instância**.

Processo participativo
:   Espaço com etapas e prazo. Classificado por tipo: Consulta Pública, Conferência, Plano Participativo ou Audiência Pública. No código: `Decidim::ParticipatoryProcess`.

Instância
:   Nome usado na interface para a assembleia do Decidim. Agrupa Conselhos e Colegiados e Fóruns de Participação. No código: `Decidim::Assembly`.

Sub-instância
:   Instância filha de outra. Órgãos públicos viram instâncias, e seus setores, sub-instâncias.

Etapa
:   Fase de um processo participativo, com período definido. Muda automaticamente conforme as datas. No código: *step*.

Componente
:   Funcionalidade adicionada a um espaço: propostas, reuniões, formulários, blog, Página Inicial etc.

Proposta
:   Contribuição de um participante. Pode ser votada, comentada e moderada.

Texto participativo
:   Documento dividido em parágrafos, cada um aberto a comentários e emendas. Implementado sobre o componente de propostas.

Devolutiva
:   Retorno do poder público aos participantes. Na interface, também designa a exportação de relatórios.

OP
:   Orçamento Participativo. Usa o componente de propostas com listagem e votação próprias.

Votos mutuamente exclusivos
:   Opção do processo que impede votar em mais de um componente de propostas do mesmo processo.

Moderação
:   Análise e ocultação de conteúdo que viola os termos de uso.

## Integrações

gov.br
:   Login único do governo federal, usado por OpenID Connect.

OP-BP
:   API que leva a participação para WhatsApp e Telegram e vincula a conta gov.br por um token JWT. Veja [Integração OP-BP](../operador/integracao-op-bp.md).

EJ (Empurrando Juntas)
:   Plataforma externa de conversas e opiniões, integrada pelo componente `decidim-ej`.

VLibras
:   Ferramenta do governo federal que traduz conteúdo para Libras.

Design System gov.br
:   Padrão visual do governo federal, aplicado à interface da plataforma. Veja [Design System gov.br](../design-system/index.md).

## Técnica

Módulo Decidim
:   Funcionalidade nativa do Decidim (propostas, reuniões, formulários…), distribuída como gem.

Componente customizado
:   Gem desenvolvida pelo LabLivre que estende o Decidim, como `decidim-homes`.

Sobrescrita
:   Arquivo do core com o mesmo caminho de um arquivo do Decidim. O Rails carrega a versão do core.

Engine
:   Mini-aplicação Rails empacotada como gem. O Decidim é formado por engines.

Command, Form, Cell, Permission
:   Padrões de código do Decidim. Veja [Arquitetura › Camadas](arquitetura.md#camadas).

Organização
:   *Tenant* do Decidim, identificado pelo host. Configurado em `/system`.

Sidekiq
:   Processador de tarefas em segundo plano, usando Redis.

whenever
:   Gem que transforma `config/schedule.rb` em tarefas do cron.

Fator de ausência
:   Menor número de pessoas que somam metade dos commits. Veja [Estatísticas](../estatisticas/contribuicoes.md).
