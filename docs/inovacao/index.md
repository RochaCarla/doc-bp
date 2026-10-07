# Inovação

O Brasil Participativo parte do **Decidim 0.27.2**, mas o código em produção é bem diferente do original. Esta seção documenta essas diferenças, com foco em **desempenho**, a começar pelo **texto participativo**.

<div class="grid cards" markdown>

-   :material-file-document-multiple:{ .lg .middle } **[Texto participativo](texto-participativo.md)**

    ---

    Renderização leve, edição parágrafo a parágrafo e criação por copiar e colar. Página com 2.000 parágrafos: de ~80 s para ~2 s na medição do MR !560.

-   :material-speedometer:{ .lg .middle } **[Desempenho](desempenho.md)**

    ---

    API própria da home (de ~10 s para cache de 10 min), divisão de bundles, comentários paginados sem polling e outras otimizações.

-   :material-star-plus:{ .lg .middle } **[Funcionalidades](funcionalidades.md)**

    ---

    gov.br, OP-BP, votos exclusivos, comentários como devolutiva, instâncias, formulários e acessibilidade.

</div>

## Resumo

| Área | Decidim 0.27.2 | Brasil Participativo | Ganho |
|------|----------------|----------------------|-------|
| Texto participativo: leitura | Uma *cell* por parágrafo, com consultas ao banco dentro de cada uma | Renderização inline, sem consultas por parágrafo | :material-gauge-full: ~80 s → ~2 s com 2.000 parágrafos (medição local do MR !560) |
| Texto participativo: edição | Um formulário com todos os parágrafos; salvar regrava todos | Operações em um parágrafo por vez, via AJAX | Custo por edição deixa de crescer com o tamanho do texto |
| Texto participativo: criação | Importação de Markdown e ODT | + DOCX (pandoc), tabelas Excel e copiar/colar com formatação | Funcional |
| Home | Consulta GraphQL sem limite a cada visita (~10 s) | Endpoint JSON com cache de 10 minutos por organização | :material-gauge-full: ~10 s antes (MR !797) |
| Comentários | Pré-carrega votos, sem paginação, *polling* a cada 15 s | Sem votos, 30 por página com "carregar mais", sem *polling* contínuo | Menos consultas e menos tráfego em segundo plano |
| Front-end | Um bundle único | `splitChunks` (bibliotecas, Decidim e app separados) | Cache entre deploys |

## Como ler esta seção

Cada afirmação traz evidência (arquivo, commit ou merge request) e um rótulo:

| Rótulo | Significado |
|--------|-------------|
| **Medido** | Número publicado na descrição de um merge request. Não há benchmark versionado no repositório |
| **Fato** | Verificado no código ou no histórico git |
| **Inferido** | Dedução a partir da leitura do código, sem medição |

!!! warning "Medições"
    O único número sobre o texto participativo (MR !560) foi medido em ambiente local, sobre um código que foi revertido uma semana depois e reescrito no MR !561. **A versão em produção hoje não foi medida.** Recomenda-se criar um benchmark reproduzível antes de citar ganhos fora desta documentação.

## Método

A comparação usou:

- o `decidim-govbr` nas branches `main` (produção) e `develop`;
- o código do Decidim na tag `v0.27.2`, a versão fixada no `Gemfile`;
- as descrições dos merge requests no GitLab.

Para ver o que o Brasil Participativo acrescentou ao banco, consulte [Banco de Dados › O que o Brasil Participativo acrescentou](../banco-de-dados/index.md#o-que-o-brasil-participativo-acrescentou).
