{#- Elementos pré-textuais do e-book. O gerador de PDF (scripts/gerar_pdf.cjs) imprime cada bloco em separado. -#}

<div class="bp-front bp-front--capa">
  <div class="bp-capa">
    <p class="bp-capa__brand">Universidade de Brasília · LabLivre</p>
    <div class="bp-capa__main">
      <p class="bp-capa__kicker">Documentação técnica e manual de uso</p>
      <h1 class="bp-capa__title">Brasil<br>Participativo</h1>
      <p class="bp-capa__subtitle">Plataforma de participação digital do governo federal, construída com software livre sobre o Decidim</p>
    </div>
    <div class="bp-capa__footer">
      <p>Secretaria Nacional de Participação Social<br>Secretaria-Geral da Presidência da República</p>
      <p class="bp-capa__edition">Edição de <span class="bp-edition">2026</span></p>
    </div>
  </div>
</div>

<div class="bp-front bp-front--rosto">
  <p class="bp-rosto__inst">Universidade de Brasília<br>Laboratório de Competência em Software Livre (LabLivre)</p>

  <h1 class="bp-rosto__title">Brasil Participativo</h1>
  <p class="bp-rosto__subtitle">Documentação técnica e manual de uso</p>

  <p class="bp-rosto__inst">Produzido no âmbito do Termo de Execução Descentralizada (TED) entre a Universidade de Brasília e a Secretaria Nacional de Participação Social, da Secretaria-Geral da Presidência da República.</p>

  <h2 class="bp-rosto__heading">Informações gerais</h2>
  <table class="bp-ficha">
    <tr><th>Título</th><td>Brasil Participativo: documentação técnica e manual de uso</td></tr>
    <tr><th>Edição</th><td><span class="bp-edition">2026</span></td></tr>
    <tr><th>Versão do conteúdo</th><td><span class="bp-version">—</span>, gerada em <span class="bp-generated">—</span></td></tr>
    <tr><th>Realização</th><td>Laboratório de Competência em Software Livre (LabLivre), Universidade de Brasília (UnB)</td></tr>
    <tr><th>Parceria</th><td>Secretaria Nacional de Participação Social (SNPS), Secretaria-Geral da Presidência da República, por meio de Termo de Execução Descentralizada</td></tr>
    <tr><th>Plataforma</th><td>brasilparticipativo.presidencia.gov.br · hospedagem Dataprev</td></tr>
    <tr><th>Base tecnológica</th><td>Decidim 0.27.2, software livre sob licença AGPLv3</td></tr>
    <tr><th>Código-fonte</th><td>gitlab.com/lappis-unb/decidimbr/decidim-govbr</td></tr>
    <tr><th>Fontes do conteúdo</th><td>Código do <code>decidim-govbr</code>, páginas institucionais e guias da plataforma, API pública do GitLab e estudos do LabLivre</td></tr>
    <tr><th>Uso de IA</th><td>Produzido com apoio de IA generativa (Claude Code, modelo Claude Opus 5.5), sob direção e revisão da equipe. Ver Sobre › Uso de IA</td></tr>
    <tr><th>Licença</th><td>Conteúdo sob Creative Commons Atribuição 4.0 Internacional (CC BY 4.0), exceto logos e marcas institucionais. Código desta documentação e software Brasil Participativo: AGPLv3</td></tr>
    <tr><th>Versão on-line</th><td>{{ config.site_url }}</td></tr>
    <tr><th>Contato</th><td>brasilparticipativo@presidencia.gov.br · decidim@unb.br</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Como citar</h2>
  <p class="bp-rosto__cite">LABLIVRE. <strong>Brasil Participativo</strong>: documentação técnica e manual de uso. Brasília: Universidade de Brasília, <span class="bp-year">2026</span>. Disponível em: {{ config.site_url }}. Acesso em: <span class="bp-access">—</span>.</p>
</div>

<div class="bp-front bp-front--apresentacao">
  <h1 class="bp-apresentacao__title">Apresentação</h1>

  <p>O Brasil Participativo é a plataforma de participação digital do governo federal. Por ela, qualquer pessoa com conta gov.br envia e vota propostas e participa de consultas públicas, conferências, planos, formulários e enquetes promovidos por ministérios e órgãos federais.</p>

  <p>Este documento reúne, em português, o conhecimento técnico e operacional sobre a plataforma. Ele é gerado a partir da versão on-line da documentação, que é atualizada continuamente com base no código-fonte. Em caso de divergência, vale a versão on-line.</p>

  <h2 class="bp-rosto__heading">Organização</h2>
  <table class="bp-ficha">
    <tr><th>Trilhas e novidades</th><td>Por onde começar em cada perfil e mudanças recentes</td></tr>
    <tr><th>Documentação</th><td>Visão geral, arquitetura, desenvolvimento, operação, banco de dados, módulos e componentes</td></tr>
    <tr><th>Transferência</th><td>Plano de transferência, inventário, operação, segurança, APIs, release, testes e atualização tecnológica</td></tr>
    <tr><th>Manual de Uso</th><td>Guias passo a passo para gestores de processos participativos</td></tr>
    <tr><th>Design System</th><td>Como o padrão visual gov.br foi aplicado na plataforma</td></tr>
    <tr><th>Inovação</th><td>O que mudou em relação ao Decidim, com foco em desempenho</td></tr>
    <tr><th>Estudos</th><td>Análises sobre a participação na plataforma</td></tr>
    <tr><th>Estatísticas</th><td>Indicadores do projeto de software livre</td></tr>
    <tr><th>Sobre</th><td>Origem e manutenção desta documentação</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Para quem</h2>
  <table class="bp-ficha">
    <tr><th>Desenvolvedores</th><td>Documentação › Desenvolvimento, Banco de Dados, Design System e Inovação</td></tr>
    <tr><th>Equipe receptora</th><td>Transferência, Documentação e Banco de Dados</td></tr>
    <tr><th>Equipes de operação</th><td>Documentação › Operação e Banco de Dados</td></tr>
    <tr><th>Gestores de processos</th><td>Manual de Uso e Módulos</td></tr>
    <tr><th>Gestão e pesquisa</th><td>Estudos, Estatísticas e Inovação</td></tr>
  </table>

  <h2 class="bp-rosto__heading">Convenções</h2>
  <ul>
    <li>Caixas azuis trazem informações; verdes, dicas; amarelas, cuidados; vermelhas, riscos.</li>
    <li>Nomes de arquivos, tabelas, variáveis e comandos aparecem em <code>fonte monoespaçada</code>.</li>
    <li>Em Inovação e Estudos, afirmações de desempenho são marcadas como <strong>medidas</strong> ou <strong>inferidas</strong>.</li>
    <li>Conteúdos em abas na versão on-line aparecem aqui em sequência, cada um com seu título.</li>
  </ul>
</div>
