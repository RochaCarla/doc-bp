# Como usar no desenvolvimento

Orientações para quem vai criar ou alterar telas no Brasil Participativo.

## Antes de criar uma tela

1. Procure o componente na [documentação do Design System gov.br](https://www.gov.br/ds/components).
2. Veja se a plataforma já usa esse componente em outra tela ([Componentes usados](componentes.md)) e copie a marcação existente.
3. Só escreva CSS novo se o componente não atender. Nesse caso, coloque o estilo em `app/packs/stylesheets/custom/` e importe-o em `decidim_application.scss`.

## Usar um componente

Use a marcação HTML da documentação oficial dentro da view ou cell. O JavaScript do padrão já está carregado em todas as páginas.

```erb
<%# Botão primário do padrão %>
<button class="br-button primary" type="submit">
  <%= t(".submit") %>
</button>

<%# Mensagem de sucesso %>
<div class="br-message success" role="alert">
  <div class="icon"><i class="fas fa-check-circle fa-lg" aria-hidden="true"></i></div>
  <div class="content"><%= t(".success") %></div>
</div>
```

Para sobrescrever uma view do Decidim, copie o arquivo da gem para o mesmo caminho em `app/views` e troque as classes do Foundation pelas do padrão.

## Regras

| Faça | Evite |
|------|-------|
| Use tokens: `var(--blue-warm-vivid-70)`, `var(--surface-rounder-md)`, `var(--font-family-base)` | Escrever cores e tamanhos fixos (`#1351b4`, `8px`) |
| Coloque ajustes em `custom/` ou `main.scss` | Editar `govbr-ds/core.scss` ou `govbr-ds/core.js` |
| Use o prefixo do padrão (`br-`) só para componentes oficiais | Criar classes `br-*` próprias; prefira um prefixo do projeto |
| Use `br-modal` para diálogos novos | Misturar `data-reveal` (Foundation) e `br-modal` na mesma tela |
| Use textos via I18n (`t(".chave")`) | Escrever texto fixo na view |
| Teste com o widget de alto contraste e com zoom de 200% | Usar só a cor para transmitir informação |

## Checklist de acessibilidade

- [ ] Todo controle interativo é alcançável e operável pelo teclado.
- [ ] O foco é visível em todos os elementos.
- [ ] Imagens informativas têm `alt`. Ícones decorativos têm `aria-hidden="true"`.
- [ ] Mensagens de erro e sucesso usam `br-message` com `role="alert"`.
- [ ] O contraste segue o modo `high-contrast` do widget.
- [ ] Os campos de formulário têm `label` associado.

## Onde mexer

| Quero mudar… | Arquivo |
|--------------|---------|
| Cor primária | `govbr-ds/main.scss` (`--primary`) e `_decidim-settings.scss` (`$primary-color`) |
| Cabeçalho | `app/views/layouts/decidim/_wrapper.html.erb` |
| Rodapé | `app/views/layouts/decidim/_main_footer.html.erb` |
| Estilo de uma tela | `app/packs/stylesheets/custom/<tela>.scss` |
| Comportamento JS de uma tela | `app/packs/src/<arquivo>.js`, importado em `decidim_application.js` ou em um entrypoint |
| Fontes e ícones | `_wrapper.html.erb` (`<link>` no `<head>`) |
