---
hide:
  - navigation
  - toc
hide_feedback: true
---

<div class="bp-hero" markdown>

# Documentação do Brasil Participativo

Tudo para desenvolver, operar e usar a plataforma de participação digital do governo federal, construída com software livre sobre o [Decidim](https://decidim.org/).

[Comece por aqui](visao-geral/trilhas.md){ .md-button .md-button--primary }
[Manual de Uso](manual/index.md){ .md-button }
[Arquitetura](visao-geral/arquitetura.md){ .md-button }
[:material-file-pdf-box: Baixar PDF](https://lablivre-unb.github.io/doc-bp/documentacao-brasil-participativo.pdf){ .md-button }

</div>

## Novo por aqui?

Entenda [o que é a plataforma](visao-geral/sobre.md), [suba o ambiente local](dev/setup.md) e siga a [trilha de aprendizado](visao-geral/trilhas.md) do seu perfil.

<div class="grid cards" markdown>

-   :material-code-tags:{ .lg .middle } **Desenvolvimento**

    ---

    Setup com Docker, estrutura do código, sobrescritas do Decidim, padrões de contribuição e criação de componentes.

    [:octicons-arrow-right-24: Guia do desenvolvedor](dev/index.md)

-   :material-server:{ .lg .middle } **Operação**

    ---

    Deploy, variáveis de ambiente, integrações (gov.br, OP-BP, EJ) e administração em `/system` e `/admin`.

    [:octicons-arrow-right-24: Guia do operador](operador/index.md)

-   :material-account-tie:{ .lg .middle } **Gestão de processos**

    ---

    Passo a passo para criar processos, montar a página inicial, publicar anexos, moderar e gerar relatórios.

    [:octicons-arrow-right-24: Manual de uso](manual/index.md)

-   :material-chart-line:{ .lg .middle } **Gestão e pesquisa**

    ---

    Indicadores de qualidade de software livre, diferenças em relação ao Decidim e evolução do projeto.

    [:octicons-arrow-right-24: Estatísticas](estatisticas/index.md)

</div>

## Documentos em destaque

<div class="grid cards" markdown>

-   **[Arquitetura do monolito](visao-geral/arquitetura.md)**

    ---

    Onde ficam front-end, back-end e banco, as camadas do Rails e o caminho de uma requisição.

-   **[Banco de Dados](banco-de-dados/index.md)**

    ---

    Dicionário das 147 tabelas, relacionamentos por domínio e o que o Brasil Participativo acrescentou ao Decidim.

-   **[Integração OP-BP](operador/integracao-op-bp.md)**

    ---

    Como o WhatsApp e o Telegram vinculam contas gov.br por JWT.

-   **[Design System gov.br](design-system/index.md)**

    ---

    Como o padrão visual do governo federal foi aplicado sobre o Decidim.

-   **[Inovação](inovacao/index.md)**

    ---

    O que o Brasil Participativo mudou no Decidim, com foco em desempenho do texto participativo.

-   **[Transferência de Tecnologia](transferencia/index.md)**

    ---

    Plano, inventário de ativos, operação, segurança, APIs, release e plano de atualização para assumir a plataforma.

-   **[Glossário](visao-geral/glossario.md)**

    ---

    Instância, etapa, componente, devolutiva, OP-BP e outros termos.

</div>

## Brasil Participativo em números

<div class="bp-stats" markdown>
<div><strong>1,94 mi</strong><span>usuários</span></div>
<div><strong>12,4 mi</strong><span>acessos</span></div>
<div><strong>463</strong><span>processos</span></div>
<div><strong>4.675</strong><span>commits no core desde abril de 2023</span></div>
<div><strong>44</strong><span>pessoas contribuidoras</span></div>
</div>

Usuários, acessos e processos: página [Sobre o Brasil Participativo](https://brasilparticipativo.presidencia.gov.br/processes/brasilparticipativo/f/1400/) em outubro de 2026. Commits e contribuidores: [Estatísticas](estatisticas/index.md).

## Novidades

- **Login pelo WhatsApp e Telegram**: o retorno ao canal agora vem assinado no JWT, e a tela final tem o botão "Voltar para o WhatsApp". [Integração OP-BP](operador/integracao-op-bp.md)
- **Votos mutuamente exclusivos** entre componentes de propostas de um mesmo processo. [Propostas](modulos/propostas.md)
- **Instâncias criadas automaticamente** a partir dos órgãos públicos, de hora em hora. [Administração](operador/administracao.md#instancias-assembleias)

[:octicons-arrow-right-24: Todas as novidades](novidades.md)

## Links úteis

| | |
|---|---|
| Plataforma em produção | [brasilparticipativo.presidencia.gov.br](https://brasilparticipativo.presidencia.gov.br/) |
| Código do core | [gitlab.com/lappis-unb/decidimbr/decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) |
| Componentes | [components-brasil-participativo](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo) |
| Decidim | [decidim.org](https://decidim.org/) · [documentação oficial](https://docs.decidim.org/) |
| Design System gov.br | [gov.br/ds](https://www.gov.br/ds/) |
| Sobre esta documentação | [LabLivre/UnB e TED com a Secretaria](sobre/index.md) |
