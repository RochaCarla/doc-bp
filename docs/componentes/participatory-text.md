# decidim-participatory_text

**Tipo**: Componente customizado (LabLivre/UnB) — fork do componente oficial
**Repositório**: [decidim-participatory_text](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo/decidim-participatory_text)

!!! warning "Não instalado no core"
    Este componente existe no grupo de componentes, mas não está no `Gemfile` do `decidim-govbr` (verificado em agosto de 2026). A descrição abaixo é do componente, não de um recurso disponível em produção.

Fork/customização do componente oficial de textos participativos do Decidim (`decidim-participatory_texts`), adaptado para as necessidades do Brasil Participativo.

!!! info "Textos participativos no core"
    Em produção, os textos participativos usam o recurso nativo do componente de propostas (`decidim-proposals`), com sobrescritas no core (comandos `UpdateParticipatoryText`, `CreateParticipatoryTextFromCopyAndPaste` e configuração automática ao criar o componente). Veja [Propostas](../modulos/propostas.md).

## Funcionalidades

- **Edição colaborativa de textos** — participantes comentam e propõem emendas a documentos
- **Estrutura de parágrafos** — texto dividido em seções e parágrafos individuais
- **Emendas por parágrafo** — propostas de alteração vinculadas a trechos específicos
- **Import de documentos** — upload de documentos Markdown ou ODT para edição participativa
- **Votação de emendas** — participantes votam nas emendas propostas

## Diferenças do Componente Oficial

Este é um **fork** do componente oficial `decidim-participatory_texts` com customizações para o contexto brasileiro. As diferenças incluem adaptações de interface e fluxo que não foram incorporadas ao upstream.

!!! warning "Fork"
    Por ser um fork, atualizações do componente oficial não são aplicadas automaticamente. Merges manuais são necessários para incorporar melhorias upstream.

## Referência

- Componente oficial: [decidim-participatory_texts](https://github.com/decidim/decidim/tree/develop/decidim-participatory_texts)
