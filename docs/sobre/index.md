# Sobre esta documentação

Esta documentação é resultado do trabalho do **Laboratório de Competência em Software Livre (LabLivre) da Universidade de Brasília (UnB)**, realizado no âmbito de um **Termo de Execução Descentralizada (TED)** firmado com a **Secretaria Nacional de Participação Social**, da Secretaria-Geral da Presidência da República, responsável pela gestão do Brasil Participativo.

## Objetivo

Reunir, em um só lugar e em português, o conhecimento técnico e operacional sobre o Brasil Participativo, para que:

- **desenvolvedores** da comunidade e de outros órgãos consigam entender, executar e evoluir a plataforma;
- **equipes de operação** consigam implantar, configurar e integrar a plataforma;
- **gestores de processos participativos** encontrem os guias de uso;
- **gestão e pesquisa** acompanhem a evolução do software e seus indicadores de qualidade.

## Quem faz o Brasil Participativo

| Papel | Instituição |
|-------|-------------|
| Gestão da plataforma | Secretaria Nacional de Participação Social, Secretaria-Geral da Presidência da República |
| Desenvolvimento e documentação | LabLivre/UnB |
| Hospedagem | Dataprev |
| Apoio | Ministério da Gestão e da Inovação em Serviços Públicos (ColaboraGov) |
| Base tecnológica | [Decidim](https://decidim.org/), software livre de democracia participativa |

## O que é o TED

O **Termo de Execução Descentralizada** é o instrumento pelo qual um órgão da administração pública federal transfere crédito orçamentário a outro órgão ou entidade federal, como uma universidade, para a execução de ações de interesse comum. Neste caso, a parceria entre a Secretaria e a UnB viabiliza o desenvolvimento, a manutenção e a documentação do Brasil Participativo pelo LabLivre, com participação de estudantes e professores.

## Como esta documentação foi produzida

| Fonte | Uso |
|-------|-----|
| Código do [`decidim-govbr`](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) (branches `main` e `develop`) | Arquitetura, configuração, módulos, inovação |
| Repositórios do grupo [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo) | Componentes customizados |
| API pública do GitLab | [Estatísticas](../estatisticas/index.md) |
| Páginas institucionais da [plataforma](https://brasilparticipativo.presidencia.gov.br/) | Visão geral e modalidades de participação |
| [Guias e tutoriais](https://brasilparticipativo.presidencia.gov.br/pages) da plataforma | [Manual de Uso](../manual/index.md) |
| Código-fonte do Decidim 0.27.2 | Comparações em [Inovação](../inovacao/index.md) |

As informações refletem o código na data da última atualização de cada página. Mudanças recentes estão em [Novidades](../novidades.md).

## Versão em PDF

Todo o conteúdo deste site também está disponível como e-book, com capa, folha de rosto, ficha técnica, sumário e contracapa. O PDF é gerado automaticamente a cada atualização da documentação.

[:material-file-pdf-box: Baixar a documentação completa em PDF](https://lablivre-unb.github.io/doc-bp/documentacao-brasil-participativo.pdf){ .md-button .md-button--primary }

Para gerar localmente: `./scripts/pdf.sh` (resultado em `dist/`).

## Uso de inteligência artificial

Esta documentação foi produzida com apoio de IA generativa (Claude Code, modelo Claude Opus 5.5), sob direção e responsabilidade da equipe do LabLivre/UnB. Ferramentas, papéis, salvaguardas e limites estão em [Uso de IA](uso-de-ia.md).

## Licença do software

O Brasil Participativo é software livre, distribuído sob a licença **GNU Affero General Public License v3 (AGPLv3)**, a mesma do Decidim.

## Contribua com a documentação

O código-fonte desta documentação está em [github.com/lablivre-unb/doc-bp](https://github.com/lablivre-unb/doc-bp). Para corrigir ou sugerir algo:

- use o botão de edição :material-file-edit-outline: no topo de cada página; ou
- abra uma [issue](https://github.com/lablivre-unb/doc-bp/issues/new).

O site é gerado com [MkDocs](https://www.mkdocs.org/) e [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), com visual baseado no [Design System gov.br](https://www.gov.br/ds/).

## Contato

- **Plataforma**: brasilparticipativo@presidencia.gov.br
- **Equipe de desenvolvimento**: decidim@unb.br
- **Comunidade**: [grupo no Telegram](https://t.me/+nm4bkXxYukFlOWZh)
