# Segurança e LGPD

Controles de segurança existentes, riscos conhecidos no código e inventário de dados pessoais. Os riscos estão ordenados por gravidade e devem entrar no plano de trabalho da equipe receptora.

## Riscos conhecidos

!!! danger "1. Chave de API que permite agir como qualquer usuário"
    A estratégia `ApiImpersonationStrategy` (`lib/decidim/strategies/api_impersonation_strategy.rb`) é registrada como **estratégia padrão do Devise para todas as requisições**, não só para `/api`. Quem enviar os cabeçalhos `X-API-KEY` (igual a `OP_BP_API_KEY`, ou `N8N_SECRET_KEY` como alternativa) e `X-USER-ID` passa a agir como o usuário daquele ID na organização, **inclusive administradores**.

    **Recomendações:** restringir a estratégia às rotas da API usadas pela OP-BP; recusar usuários administradores; registrar cada uso em log de auditoria; guardar a chave em cofre e trocá-la periodicamente.

!!! danger "2. Callback do login externo sem checagem de host"
    `ExternalAuthService::PROVISIONAL_SKIP_CALLBACK_HOST_CHECK = true` desliga a allowlist de hosts do `callback_url`. Quem tiver o `OP_BP_JWT_SECRET` pode mandar CPF, nome e e-mail do usuário para qualquer endereço. **Recomendação:** mudar para `false` e configurar `OP_BP_CALLBACK_ALLOWED_HOSTS`. Veja [Integração OP-BP](../operador/integracao-op-bp.md#variaveis-de-ambiente).

!!! danger "3. Plataforma sem correções de segurança"
    Ruby 3.0 (fim do suporte em 04/2024), Rails 6.1 (10/2024) e Node 16 na imagem base (09/2023) não recebem mais correções. O Decidim 0.27 está 5 versões menores atrás. Veja o [Plano de atualização tecnológica](atualizacao.md).

!!! warning "4. HTML e JavaScript editáveis pelo painel"
    Os exemplos de ambiente (`.env.dev`, `setup/env`) ligam `DECIDIM_ENABLE_HTML_HEADER_SNIPPETS`, que permite a administradores inserir código no `<head>` das páginas. A página inicial também depende de um bloco HTML com JavaScript editado no painel e **não versionado**. Uma conta de administrador comprometida pode injetar script em todas as páginas. **Recomendação:** versionar o bloco da home, revisar quem tem papel de administrador e avaliar desligar os snippets.

!!! warning "5. Download de anexos de formulários"
    O `download_zip` busca o arquivo pelo `blob_id` sem verificar o formulário, e os ZIPs gerados não são apagados. Veja [Inovação › Desempenho](../inovacao/desempenho.md#riscos-e-regressoes).

!!! warning "6. Análises de segurança não bloqueiam o CI"
    Os jobs de Brakeman (SAST) e Trivy (SCA) têm `allow_failure: true`, e um relatório gerado (`brakeman_report.html`) está versionado. **Recomendação:** tornar os jobs bloqueantes para vulnerabilidades altas e remover o relatório do repositório.

!!! warning "7. Acesso ao painel `/system` sem restrição de IP"
    `DECIDIM_SYSTEM_ACCESSLIST_IPS` vem vazia por padrão. **Recomendação:** restringir o `/system` à rede administrativa.

## Controles existentes

| Controle | Implementação |
|----------|---------------|
| Autenticação de cidadãos | gov.br via OpenID Connect com PKCE |
| Senha de administradores | Mínimo de 15 caracteres, expiração em 90 dias, 5 senhas anteriores bloqueadas (`DECIDIM_ADMIN_PASSWORD_*`) |
| Sessão | Expira após 30 minutos de inatividade (`DECIDIM_EXPIRE_SESSION_AFTER`) |
| Limite de requisições | 100 requisições por minuto por IP (`DECIDIM_THROTTLING_*`) |
| Painel de filas | `/sidekiq` com Basic Auth em produção |
| Tokens do login externo | JWT HS256 com expiração obrigatória e allowlist de links de retorno por canal |
| API GraphQL | Leitura pública de dados públicos; ações autenticadas por JWT (`decidim-apiauth`, `SECRET_KEY_JWT`) |
| Permissões | Sistema de permissões do Decidim por espaço e componente |
| Moderação | Denúncias, ocultação e bloqueio de usuários |
| Auditoria | `decidim_action_logs` (ações administrativas) e `versions` (PaperTrail) |
| Análise no CI | RuboCop, Brakeman, Trivy |

## Gestão de vulnerabilidades

O repositório não tem política de segurança (`SECURITY.md`). Recomenda-se publicar uma, com:

- canal privado para relatar vulnerabilidades (e-mail institucional);
- prazo de resposta;
- quem decide e publica as correções.

O Decidim publica alertas de segurança no [repositório oficial](https://github.com/decidim/decidim/security/advisories). A equipe receptora deve acompanhar esses alertas, porque as correções exigem portar mudanças para as [sobrescritas](sobrescritas.md).

## Dados pessoais (LGPD)

### Inventário

| Tabela | Dados pessoais | Observação |
|--------|----------------|------------|
| `decidim_users` | `email`, `name`, `nickname`, `avatar`, `about`, `personal_url`, `current_sign_in_ip`, `last_sign_in_ip`, `extended_data`, `entity_fields` | `extended_data` guarda o vínculo OP-BP (`external_source_id`) e os campos extras de cadastro |
| `decidim_identities` | `uid` | Para o gov.br, o `uid` é o **CPF** |
| `decidim_authorizations` | `unique_id`, `metadata`, `verification_metadata` | Dados das verificações |
| `decidim_forms_answers` | `body`, `ip_hash`, `session_token` | Respostas podem conter dados pessoais e sensíveis, conforme as perguntas |
| `decidim_meetings_registrations` | vínculo usuário–reunião, `code` | |
| `decidim_messaging_messages` | `body` | Mensagens privadas entre usuários |
| `decidim_user_reports` | `reason`, `details` | Denúncias |
| `decidim_initiatives_votes` | `encrypted_metadata`, `hash_id` | Assinaturas de iniciativas |
| `versions` | `object`, `object_changes` | Histórico pode conter cópias de dados pessoais |
| `decidim_action_logs` | `extra` | Pode conter dados de quem fez a ação |
| ActiveStorage | Arquivos enviados | Anexos de respostas e comentários |

Dados de **opinião política** (votos, apoios, propostas e comentários ligados a uma pessoa) merecem cuidado de dado sensível.

### Tratamentos

| Direito ou obrigação | Como a plataforma atende |
|----------------------|--------------------------|
| Acesso aos dados | "Baixar meus dados" do Decidim; os arquivos expiram em 7 dias (`DECIDIM_DOWNLOAD_YOUR_DATA_EXPIRY_TIME`) e são apagados diariamente |
| Exclusão | Comando `DestroyAccount` do Decidim: apaga nome, apelido, e-mail e avatar, identidades, grupos e seguidores |
| Consentimento de cookies | Modal de consentimento do Decidim (`data_consent`) |
| Termos de uso | Página `/pages/terms-and-conditions` com aceite no cadastro |

!!! warning "Pontos a verificar"
    - A exclusão de conta do Decidim **não limpa** `extended_data`, `entity_fields`, `about` e `personal_url`. Avalie estender o comando.
    - Os exports de propostas e comentários incluem nome e ID do autor. Restrinja quem pode exportar e por quanto tempo os arquivos ficam disponíveis.
    - O callback OP-BP envia **CPF, nome e e-mail** a um sistema externo. Formalize a base legal e o acordo de tratamento com o operador da API OP-BP.
    - Defina a política de retenção de logs, que podem conter IPs e identificadores.

### Encarregado e bases legais

**A confirmar com a SNPS:** encarregado de dados (DPO), bases legais por finalidade (participação, comunicação, pesquisa), registro de operações de tratamento e relatório de impacto (RIPD), especialmente para a participação por mensageria.
