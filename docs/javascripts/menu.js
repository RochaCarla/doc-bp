// Um só menu: a gaveta (celular e tablet) abre na lista das abas do topo,
// e não dentro da seção da página atual (por exemplo, "Início").
// O tema marca a seção ativa como aberta; aqui fechamos todas ao carregar.
(function () {
  function abrirNoTopo() {
    document
      .querySelectorAll(".md-nav--primary .md-nav__toggle:checked")
      .forEach(function (toggle) {
        toggle.checked = false;
      });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", abrirNoTopo);
  } else {
    abrirNoTopo();
  }
})();
