# Uso de inteligência artificial

Esta documentação foi produzida com apoio de **inteligência artificial generativa**, sob direção e responsabilidade da equipe do LabLivre/UnB. Esta página declara como a IA foi usada, que cuidados foram tomados e quais limites o leitor deve considerar.

!!! info "Resumo"
    - **Ferramenta:** Claude Code (Anthropic), com o modelo **Claude Opus 5.5**, em outubro de 2026.
    - **Papel da IA:** levantar informações no código e em fontes públicas, redigir as páginas, escrever os scripts geradores e o tema visual, e montar o e-book.
    - **Papel humano:** definir o escopo, o público e a estrutura, fornecer documentos, decidir o que publicar e responder pelo conteúdo.
    - **Responsabilidade:** o conteúdo é de responsabilidade da equipe do LabLivre/UnB, não da ferramenta.

## Ferramentas

| Ferramenta | Uso |
|------------|-----|
| Claude Code (Anthropic), modelo Claude Opus 5.5 | Agente de programação e redação, operado no repositório desta documentação |
| Subagente de pesquisa do Claude Code | Comparação do código do `decidim-govbr` com o Decidim 0.27.2 ([Inovação](../inovacao/index.md)) |
| Scripts determinísticos (Python e Node), escritos com apoio da IA | Estatísticas, dicionário de dados, inventário de sobrescritas e e-book. **Os números vêm dos scripts, não do modelo** |

## O que a IA fez e o que ficou com pessoas

| Conteúdo | Papel da IA | Papel humano | Como foi verificado |
|----------|-------------|--------------|---------------------|
| Estrutura do site (abas, trilhas, home) | Proposta e implementação, tendo a documentação do Flutter como referência indicada pela equipe | Pedido, referência e aprovação de cada aba | Navegação conferida em capturas de tela |
| Arquitetura, configuração, operação, transferência | Leitura do código (`git log`, `grep`, schema, rotas) e redação | Definição dos temas e do público | Cada fato com arquivo ou commit de origem; o que não tinha fonte ficou **a confirmar** |
| Banco de dados, estatísticas, sobrescritas | Escrita dos scripts geradores | Definição do recorte (série a partir de abril de 2023) | Saídas reproduzíveis pelos scripts; contagens comparadas com o código |
| Inovação (desempenho) | Pesquisa comparativa com o Decidim e redação | Pedido do foco no texto participativo | Números citados conferidos nas descrições dos MRs; afirmações rotuladas **medida** ou **inferida** |
| Manual de Uso | Reescrita dos guias públicos da plataforma | Indicação da fonte | Link para o guia original em cada página |
| Estudo "Orçamento do Povo" | Resumo estruturado e recriação das figuras a partir do texto | Autoria do relatório e fornecimento do documento | Ficha com link para o texto integral; figuras indicadas como recriadas |
| Design System e tema visual | Levantamento no código e implementação do tema | Pedido de aplicar o padrão gov.br | Capturas de tela em modo claro e celular |
| Diagramas | Geração em Mermaid e ajuste para leitura vertical | Pedido de legibilidade | Medição da largura de cada diagrama renderizado |
| E-book | Implementação do pipeline e da diagramação | Definição da estrutura (capa, contracapa, ficha) | Leitura das páginas do PDF gerado |

## Salvaguardas

Para reduzir o risco de informações incorretas, comuns em textos gerados por IA:

- **Fonte verificável:** toda afirmação técnica aponta para arquivo, commit, merge request ou página pública.
- **Nada inventado:** o que não estava no código nem em fonte pública aparece como **a confirmar**.
- **Rótulos:** ganhos de desempenho aparecem como **medidos** (número publicado) ou **inferidos** (leitura de código).
- **Números por script:** estatísticas e contagens são calculadas por programas reproduzíveis, não estimadas pelo modelo.
- **Conferência cruzada:** dados críticos foram checados em mais de uma fonte. Exemplo: a versão em produção foi conferida no rodapé do site oficial, o que corrigiu a suposição de que `main` era a branch de produção.
- **Build estrito:** o site é construído sem aceitar avisos, e páginas e PDF foram conferidos visualmente.
- **Histórico:** os commits feitos com a IA têm a linha `Co-Authored-By: Claude`, que permite rastrear o que foi produzido com apoio dela.

## Dados tratados

| Dado | Tratamento |
|------|------------|
| Código público do `decidim-govbr`, dos componentes e do Decidim | Lido pela IA |
| APIs e páginas públicas (GitLab, plataforma, rubygems, endoflife.date) | Lidas pela IA ou pelos scripts |
| Documentos de trabalho fornecidos pela equipe (relatório "Orçamento do Povo") | Lidos e resumidos; links para documentos internos não foram publicados |
| Nomes e e-mails do histórico do git | Processados pelo script de estatísticas; **e-mails não são publicados** |
| Segredos de produção e dados pessoais de usuários da plataforma | **Não** foram fornecidos à IA nem publicados |

## Limitações

- O texto pode conter imprecisões que escaparam à verificação, principalmente em pontos que dependem de contexto não registrado no código.
- Afirmações marcadas como **inferidas** são interpretações do código, não medições.
- O conteúdo reflete o estado do código e das fontes em outubro de 2026. Páginas geradas mostram a data da coleta.
- A IA não teve acesso aos ambientes de produção nem a documentos internos além dos fornecidos.

Encontrou um erro? Use **Reportar um problema** no rodapé da página.

## Registro de revisão humana

Recomenda-se que cada seção seja revisada por uma pessoa da equipe antes de uso oficial, como na transferência de tecnologia. Registre aqui:

| Seção | Revisada por | Data | Observações |
|-------|--------------|------|-------------|
| Visão Geral | | | |
| Desenvolvimento | | | |
| Operação | | | |
| Banco de Dados | | | |
| Transferência | | | |
| Manual de Uso | | | |
| Design System | | | |
| Inovação | | | |
| Estudos | | | |
| Estatísticas | | | |

## Contribuições futuras com IA

O uso de IA é permitido nesta documentação, com estas regras:

1. **Declare:** mantenha a linha `Co-Authored-By` nos commits feitos com apoio de IA.
2. **Verifique:** todo fato novo precisa de fonte. O que não tiver fonte fica **a confirmar**.
3. **Não exponha:** não forneça à IA segredos, dados pessoais de usuários ou documentos sem autorização.
4. **Prefira scripts:** números e listas extensas devem vir dos geradores em `scripts/`, não de texto escrito pelo modelo.
5. **Cheque o resultado:** rode o build estrito e confira visualmente páginas e diagramas antes do merge.
6. **Revise:** uma pessoa da equipe revisa e aprova a mudança.
