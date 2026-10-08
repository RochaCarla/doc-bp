# Novidades

Resumo das mudanças relevantes no `decidim-govbr` (branch `main`), agrupadas por tema. Última revisão: commit `eb410c31` (agosto de 2026).

!!! info "Fluxo de branches"
    Desde maio de 2026 as features são integradas primeiro em `develop` e depois promovidas para `main` (merge `64b70ecf`, junho de 2026).

## 2026

### Autenticação e integração OP-BP

- **Login externo via WhatsApp/Telegram** — o fluxo `/external_auth/link` vincula a conta do Brasil Participativo ao usuário de um canal de mensagens. O redirecionamento pós-vínculo agora vem assinado no JWT (não mais configurado no admin), e a tela de sucesso exibe um botão "Voltar para o WhatsApp". Detalhes em [Integração OP-BP](operador/integracao-op-bp.md).
- **Novas variáveis** `OP_BP_JWT_SECRET`, `OP_BP_API_KEY`, `OP_BP_CALLBACK_API_KEY`, `OP_BP_CALLBACK_ALLOWED_HOSTS` e `OP_BP_FALLBACK_WHATSAPP_URL`. `EXTERNAL_AUTH_SECRET` e `N8N_SECRET_KEY` continuam aceitas como fallback legado, com aviso no log.
- **Tokens exigem `exp`**: links capturados do histórico de conversa não podem ser reutilizados indefinidamente.
- **Callback para a API OP-BP** envia `cpf`, `name` e `email` e usa `Authorization: Bearer`.
- **Tela de login simplificada** quando acessada pelo login externo (`?external=true`), com auto-submit para o gov.br e proteção contra loop.
- **Identidades gov.br duplicadas** — novo job `RemoveDuplicatedGovbrIdentitiesJob`, ativado por organização via feature flag no painel `/system`.

### Propostas

- **Votos mutuamente exclusivos** entre componentes de propostas de um mesmo processo (opção do processo participativo).
- **Exibir votos** — nova opção `show_votes` no componente de propostas.
- **Listagem customizada para o Orçamento do Povo** — página única, ordenação, cards e contador de votos.
- **Exportação** passa a incluir nome e ID do autor.
- **Componente "Texto participativo"** na lista de componentes: habilita os textos participativos e esconde configurações que não se aplicam (MR !777). Detalhes em [Inovação › Texto participativo](inovacao/texto-participativo.md).

### Formulários

- **Notificação por e-mail** ao participante quando ele responde um formulário.
- **Limite de arquivos** (`max_files`, 1–50, padrão 10) em perguntas do tipo arquivo, também suportado na importação de perguntas por JSON.
- **Administradores de espaço** podem visualizar e baixar anexos das respostas.
- Correção: perguntas com condicional não eram salvas.

### Comentários

- **Edição limitada a 5 minutos** após a criação; administradores só editam o próprio comentário.
- **Exportação de comentários** inclui as colunas `deletado_em` e `moderado_em`.

### Espaços participativos

- **Instâncias a partir de órgãos públicos** — job horário `PublicBodiesToInstancesJob` cria assembleias (instâncias) e sub-instâncias a partir dos escopos de órgãos e setores.
- **Assembleias não listadas** (`unlisted`) — ficam acessíveis por link mas fora das listagens.
- **Troca automática de fase** — job horário que respeita o fuso horário da organização.
- **Dashboard** liberado para administradores de espaço.
- **Página de eventos** redesenhada (filtros padrão, cards, rótulo do espaço relacionado, mapa só com reuniões geocodificadas).

### Página inicial e desempenho

- **Endpoint `GET /api/home_processes`** — JSON com tipos de processo e instâncias públicas, cacheado por organização (10 min).
- Remoção do CSS do core do Decidim na home e habilitação de `splitChunks`.
- Instalação como PWA desabilitada.

### Revertido ou removido

| Mudança | Situação |
|---------|----------|
| Módulo `decidim-api-categorization` | Removido do core (junho de 2026) |
| Cidade e estado em formulários | Revertido (março de 2026) |
| Correções de SEO (favicon, og:image, dados estruturados) | Revertido (junho de 2026) |
| Páginas de erro 404/500 estilizadas | Revertido (agosto de 2026); valem as páginas estáticas de `public/` |

### CI

- Versão do Trivy fixada em 0.69.3 no job de SCA.
