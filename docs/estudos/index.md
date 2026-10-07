# Estudos

Análises sobre a participação social no Brasil Participativo: estudos de caso, avaliações de processos e, progressivamente, análises de ciência de dados sobre como as pessoas participam da plataforma.

Os estudos são produzidos pelo LabLivre/UnB no âmbito do TED com a Secretaria Nacional de Participação Social. Cada estudo traz uma ficha com tipo, período, fontes e situação, para deixar claro o que foi medido e o que foi inferido.

## Estudos publicados

<div class="grid cards" markdown>

-   :material-cash-multiple:{ .lg .middle } **[Orçamento do Povo](orcamento-do-povo.md)**

    ---

    Integração do Brasil Participativo com o WhatsApp no orçamento participativo federal: construção técnica, metodologia de participação e dimensão política.

    *Estudo de caso avaliativo · 2026 · versão de trabalho*

</div>

## Ficha de um estudo

Todo estudo publicado aqui segue a mesma estrutura:

| Campo | Conteúdo |
|-------|----------|
| **Questão** | Pergunta que o estudo responde |
| **Tipo** | Estudo de caso, análise exploratória de dados, avaliação de impacto, experimento… |
| **Período e recorte** | Processos, territórios e datas analisados |
| **Fontes** | Documentos, banco de dados, API, entrevistas, registros de teste |
| **Método** | Como as fontes foram analisadas |
| **Resultados** | Achados, separando o que foi medido do que foi inferido |
| **Limitações** | O que o estudo não permite concluir |
| **Situação** | Versão de trabalho, revisada ou publicada |

## Agenda de ciência de dados

O primeiro estudo é qualitativo e registra a ausência de dados quantitativos de participação como lacuna. A documentação técnica já oferece a base para os próximos estudos:

| Pergunta | Fonte disponível |
|----------|------------------|
| Quantas pessoas participam, por processo, município e canal? | Tabelas de propostas, votos e respostas ([Banco de Dados](../banco-de-dados/index.md)) |
| Onde as pessoas desistem no fluxo de participação? | Registros do fluxo de login externo e do canal de mensagens ([Integração OP-BP](../operador/integracao-op-bp.md)) |
| Quais temas e propostas concentram votos e comentários? | `decidim_proposals_proposals`, `decidim_comments_comments` ([Consultas úteis](../banco-de-dados/consultas.md)) |
| Como a participação se distribui no tempo? | Datas de criação de propostas, votos e cadastros |
| Como o software que sustenta a participação evolui? | [Estatísticas](../estatisticas/index.md) do repositório |

!!! warning "Dados pessoais"
    Análises sobre participação usam dados pessoais protegidos pela LGPD. Trabalhe com bases anonimizadas ou agregadas e publique só resultados agregados.
