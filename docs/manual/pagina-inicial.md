---
icon: material/view-dashboard-edit
---

# Página Inicial do processo

O componente **Página Inicial** monta a apresentação visual de um processo participativo com **blocos** configuráveis: cabeçalho, notícias, cards, etapas, vídeos, enquetes e outros. Apesar do nome, pode ser usado em qualquer etapa para destacar informações.

[:material-open-in-new: Guia original com capturas de tela](https://brasilparticipativo.presidencia.gov.br/pages/tutorial-pagina-inicial){ .md-button }

É o primeiro contato do participante com o processo. Uma página bem configurada atrai, informa, facilita a navegação e reforça a identidade visual do processo.

!!! note "Para desenvolvedores"
    O componente é a gem [`decidim-homes`](../componentes/homes.md).

## Criar o componente

1. No painel de administrador, abra o processo.
2. Na barra lateral, clique em **Componentes**.
3. Clique em **Adicionar componente** e escolha **Página Inicial**.
4. Preencha as informações e clique em **Adicionar componente**.

## Adicionar blocos

1. Clique no ícone de **lápis** do componente Página Inicial.
2. Clique em **Adicionar componente** e escolha o tipo de bloco.
3. Clique no lápis do bloco para configurá-lo.

## Definir como Página Inicial do processo

1. Na barra lateral, clique em **Informação geral**.
2. Em **Configurações avançadas**, escolha o componente como **Página Inicial do Processo Participativo**.
3. Clique em **Atualizar** ou **Publicar**.

## Blocos disponíveis

| Bloco | Para que serve | O que configurar |
|-------|----------------|------------------|
| **Header** | Título e descrição do processo, convite à participação | Título e subtítulo |
| **Notícias** | Destaque das notícias do processo | Componente de notícias (blog) de origem; as mais recentes ficam no centro |
| **Mapa do Brasil** | Participação por território | Informações do mapa |
| **Chamada à ação** | Convite com texto e imagem | Texto, link e imagem (aparece à direita) |
| **Carrossel** | Sequência de imagens | Lista de URLs das imagens |
| **Apoiadores e organizadores** | Logos de parceiros | Tipo (apoiador ou organizador) e imagem da logo |
| **Logos oficiais** | Assinatura institucional | Conjunto de logos oficiais |
| **Etapas do processo** | Linha do tempo das etapas | Título e descrição da seção |
| **Cards** | Atalhos e destaques | Tipo de card e lista de cards (veja abaixo) |
| **Proposta** | Destaque de um componente de propostas | Componente, título e subtítulo |
| **Enquete EJ** | Conversa do Empurrando Juntas | Componente, primeira pergunta, comentário e limite de comentários por pessoa |
| **Texto participativo** | Destaque de textos participativos | Título, descrição e ordem dos textos |
| **Processos relacionados** | Processos ligados a uma instância | Título e descrição. Só em instâncias (assembleias) |
| **Espaços participativos filhos** | Sub-instâncias | Só em instâncias. A instância filha deve indicar a instância pai em **Visibilidade** |
| **Dados do processo** | Responsáveis, datas, secretaria, órgão e link do DOU | Recomendado em todo processo |
| **Estatísticas do espaço** | Números de participantes, comentários, propostas e eventos | — |

### Tipos de card

=== "Card participativo"

    Título, subtítulo, link de redirecionamento e ícone.

=== "Card descritivo"

    Rótulo (faixa azul em destaque), título e descrição.

=== "Card de etapa"

    Título, etapa, link, datas de início e fim, descrição e ícone. Os nomes de ícones vêm do [Font Awesome](https://fontawesome.com/search?ic=free). Cards podem ser marcados para destaque em azul.

Use **Adicionar card** para criar vários cards do mesmo tipo.

### Processos relacionados e espaços filhos

Estes dois blocos só existem em **instâncias** (assembleias):

- **Processos relacionados**: em **Informações** da instância, escolha os processos em "Processos participativos relacionados" e clique em **Atualizar**. A instância precisa estar pública e publicada.
- **Espaços participativos filhos**: na instância filha, em **Visibilidade**, escolha a instância pai e publique a filha.

## Próximos passos

- [Publicar anexos](anexos.md)
- [Criar e publicar um processo](informacoes-gerais.md)
