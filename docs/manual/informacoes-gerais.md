---
icon: material/file-document-edit
---

# Criar e publicar um processo

Este guia orienta o gestor de processo no preenchimento das **Informações Gerais** e na criação de etapas e componentes, até a publicação do processo. Vale para todos os tipos de processo participativo.

[:material-open-in-new: Guia original com capturas de tela](https://brasilparticipativo.presidencia.gov.br/pages/tutorial-informacoes-gerais){ .md-button }

## O que são as Informações Gerais

São a base de configuração do processo: nome, endereço público (URL), datas, imagens e dados do órgão responsável. Os componentes (formulários, propostas, anexos etc.) dependem dessas informações para funcionar e aparecer corretamente.

!!! warning "Etapa obrigatória"
    Sem as Informações Gerais preenchidas, não é possível criar nem vincular os componentes do processo. Preencha-as primeiro, com o ponto focal da Coordenação-Geral de Participação Digital.

Ao abrir o processo no painel de administração, os recursos de configuração ficam na coluna à esquerda. Clique em **Informação geral**.

## Etapa 1: Criar o processo

1. Acesse o painel de **Admin** e clique em **Processos**.
2. Clique em **Novo processo**.
3. Preencha os dados e clique em **Criar**:

| Grupo | Campos |
|-------|--------|
| Identificação | Nome do processo, tipo de processo participativo, link amigável (slug) |
| Moderação | Identificador do grupo do Telegram para moderação ([veja Moderação](moderacao.md#configuracao-no-brasil-participativo)) |
| Descrição | Resumo do processo |
| Prazo | Data de início e de encerramento |
| Imagens | Capa para celular e para computador, até 3840 × 3840 pixels |
| Dados do processo | Órgão ou instituição, setor, telefone ou e-mail institucional, responsável pela consulta, data e link da publicação no Diário Oficial da União |
| Filtros | Área de interesse, secretaria |

!!! tip "Tipo de processo"
    O tipo define em qual menu o processo aparece no site: Consultas Públicas, Conferências, Planos Participativos ou Audiências Públicas.

### Configurações avançadas

No fim da página há opções de exibição:

- **Mostrar dados participativos**
- **Mostrar métricas**
- **Mostrar mobilização**: exibe a aba de mobilização, usada também para os [anexos](anexos.md#etapa-2-publicar-os-anexos)
- Título e posição da aba de mobilização
- Ordem do processo em relação aos outros
- Palavras-chave
- Formulários "Informações da organização" e "Registre o que aconteceu"
- Componente usado como **Página Inicial do processo** ([veja Página Inicial](pagina-inicial.md#definir-como-pagina-inicial-do-processo))

## Etapa 2: Configurar etapas

Uma **etapa** é uma fase do processo com período definido. Alguns componentes, como Eventos e Propostas, dependem de uma etapa ativa ou usam o período dela.

Todo processo novo já vem com a etapa **Introdução**, que deve ser atualizada. As demais são criadas manualmente.

=== "Atualizar a primeira etapa"

    1. No processo, clique em **Etapas**.
    2. Clique no ícone de lápis da etapa.
    3. Preencha os dados e clique em **Atualizar**.

=== "Adicionar uma nova etapa"

    1. Em **Etapas**, clique em **Nova etapa**.
    2. Preencha os dados e clique em **Criar**.

!!! info "Troca automática"
    A plataforma muda a etapa ativa automaticamente, de hora em hora, de acordo com as datas cadastradas.

## Etapa 3: Criar componentes

Todos os componentes são criados de forma parecida. O exemplo usa **Propostas**; alguns campos mudam conforme o componente.

1. Clique em **Componentes**.
2. Clique em **Adicionar componente** e escolha **Propostas**.
3. Preencha os dados e clique em **Adicionar componente**.

Opções específicas de cada componente estão em [Módulos](../modulos/propostas.md).

## Etapa 4: Visualizar o componente

1. Clique em **Componentes** na barra lateral.
2. Clique no nome do componente. Você verá a página como o cidadão vê.
3. Para voltar ao painel, clique em **Editar componente**.

## Etapa 5: Publicar o componente

1. Em **Componentes**, encontre o componente.
2. Clique no ícone de **check** (:material-check:). O componente passa a ser público.

## Etapa 6: Publicar o processo

1. Volte em **Informação geral**.
2. Clique em **Publicar**.

O processo fica visível para qualquer pessoa.

## Próximos passos

- [Montar a Página Inicial do processo](pagina-inicial.md)
- [Publicar anexos](anexos.md)
- [Configurar a moderação](moderacao.md)
