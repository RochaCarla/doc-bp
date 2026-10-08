# Inventário de ativos

Tudo o que precisa mudar de mãos. Os itens marcados **a confirmar** não estão registrados no código e devem ser levantados com a equipe atual antes da [fase de preparação](index.md#fases).

!!! warning "Segredos"
    Este inventário lista **nomes** de credenciais, nunca valores. Entregue os valores por canal seguro (cofre de senhas da instituição) e troque-os depois da transferência.

## Repositórios de código

| Repositório | Conteúdo | Branches | Onde é usado |
|-------------|----------|----------|--------------|
| [decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) | Core da plataforma | `develop` (padrão no GitLab), `main`, `deploy-v*` (ver [Release](release.md)) | Aplicação |
| [decidim-module-homes](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo/decidim-module-homes) | Página inicial por blocos | padrão | Gemfile |
| [decidim-module-enhanced_process_groups_and_scopes](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo/decidim-module-enhanced_process_groups_and_scopes) | Grupos e escopos | `main` | Gemfile |
| [decidim-ej](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo/decidim-ej) | Integração com o Empurrando Juntas | `main` | Gemfile |
| [decidim-extra_user_fields](https://gitlab.com/lappis-unb/decidimbr/decidim-extra_user_fields) | Campos extras de cadastro | `develop` | Gemfile |
| [decidim-module-mobile](https://gitlab.com/lappis-unb/decidimbr/bp-mobile/decidim-module-mobile) | Suporte ao app móvel | `main` | Gemfile |
| [decidim-whatsapp-integration](https://gitlab.com/lappis-unb/decidimbr/decidim-whatsapp-integration) | Integração com WhatsApp | — | Estudo [Orçamento do Povo](../estudos/orcamento-do-povo.md) |
| [multi-channel-participation](https://gitlab.com/lappis-unb/decidimbr/multi-channel-participation) | Participação multicanal (API OP-BP) | — | Estudo Orçamento do Povo |
| [doc-bp](https://github.com/lablivre-unb/doc-bp) | Esta documentação | `main` | GitHub Pages |

O grupo [`lappis-unb/decidimbr`](https://gitlab.com/lappis-unb/decidimbr) pertence ao laboratório. A transferência deve definir se os repositórios **migram** para um grupo institucional ou se o receptor ganha papel de *maintainer* no grupo atual.

## Dependências de terceiros

| Dependência | Origem | Observação |
|-------------|--------|------------|
| Decidim 0.27.2 e módulos oficiais | rubygems.org | Versão fixa no `Gemfile` |
| `decidim-decidim_awesome` 0.10.2 | rubygems.org | Comunidade Decidim |
| `decidim-apiauth` | github.com/mainio/decidim-module-apiauth | Sem versão fixa: segue a branch padrão (commit travado no `Gemfile.lock`) |
| Design System gov.br | Arquivos copiados para `app/packs/*/govbr-ds/` | Versão de origem não registrada. Veja [Design System](../design-system/index.md) |

## Imagens e artefatos

| Ativo | Onde | Como é gerado |
|-------|------|---------------|
| Imagem base `lappis/decidim-govbr:v1-release` | Docker Hub, conta `lappis` | `scripts/generate_dockerhub_image.sh` a partir do `Dockerfile.DockerHub` (Ruby 3.0.4, Node 16) |
| Imagens de deploy de produção | **a confirmar** (registry da Dataprev?) | **a confirmar** |
| Tags de versão (`v1.x.y`, `v1.x.y-rc.n`) | GitLab | [Versionamento e release](release.md) |
| Site e PDF desta documentação | GitHub Pages | GitHub Actions |

## Ambientes

| Ambiente | Endereço | Hospedagem | Situação |
|----------|----------|------------|----------|
| Produção | brasilparticipativo.presidencia.gov.br | Dataprev | Em operação |
| Laboratório / homologação | **a confirmar** (há referência a `lab-decide.dataprev.gov.br` no `.env.example`) | Dataprev | **a confirmar** |
| API OP-BP | `api-opbp.lablivre.rocks` (padrão do código) | LabLivre | **a confirmar** se fica com o receptor |
| Desenvolvimento | Docker Compose local | Máquina do desenvolvedor | [Setup local](../dev/setup.md) |

## Serviços externos e contas

| Serviço | Uso | Credenciais (nomes) | Dono atual |
|---------|-----|---------------------|------------|
| gov.br (Login Único) | Autenticação | `OMNIAUTH_GOVBR_CLIENT_ID`, `OMNIAUTH_GOVBR_CLIENT_SECRET`/`OMNIAUTH_GOVBR_SECRET_KEY` | **a confirmar** (cadastro do cliente no MGI) |
| API OP-BP / bot de mensagens | Participação por WhatsApp e Telegram | `OP_BP_JWT_SECRET`, `OP_BP_API_KEY`, `OP_BP_CALLBACK_API_KEY` | LabLivre |
| Bot de moderação no Telegram `@moderacao_bp_bot` | Alertas de moderação | Token do bot (**a confirmar**) | **a confirmar** |
| Bot do Telegram de participação | Participação por Telegram | `TELEGRAM_TOKEN` | **a confirmar** |
| Empurrando Juntas | Conversas e enquetes | `EJ_JWT_SECRET`, `EJ_SECRET_KEY` | LabLivre |
| Airflow | Relatórios | `HOST_AIRFLOW`, `USER_AIRFLOW`, `PASSWORD_AIRFLOW` | **a confirmar** |
| SMTP | E-mails | `SMTP_*` | **a confirmar** |
| Storage de arquivos | Uploads | `STORAGE_PROVIDER` e credenciais do provedor | **a confirmar** |
| Mapas | Geocodificação e mapas | `MAPS_*` | **a confirmar** |
| Elastic APM | Monitoramento de desempenho (gem `elastic-apm` no grupo de produção) | Variáveis `ELASTIC_APM_*` (não versionadas) | **a confirmar** |
| Painel Sidekiq | Filas | `ADMIN_USERNAME`, `ADMIN_PASSWORD` | Operação |
| GitLab CI | Pipeline e relatório do Brakeman por e-mail | `SMTP_PASSWORD`, `SMTP_TO_EMAILS`, `SMTP_FROM_EMAIL` (variáveis do CI) | LabLivre |
| Docker Hub `lappis` | Imagem base | Conta do laboratório | LabLivre |
| WhatsApp Business | Canal oficial de mensagens | — | Inexistente (ver [Orçamento do Povo](../estudos/orcamento-do-povo.md)) |
| Verificação de CPF (Serpro/ConectaGov) | Identificação na mensageria | — | Contrato institucional inexistente |

## Segredos da aplicação

Segredos que a aplicação exige em produção e que devem ser gerados pelo receptor:

| Segredo | Uso | Como gerar |
|---------|-----|-----------|
| `SECRET_KEY_BASE` | Sessões e cookies do Rails | `bin/rails secret` |
| `SECRET_KEY_JWT` | Tokens da API (`decidim-apiauth`) | `bin/rails secret` |
| `OP_BP_JWT_SECRET` | Tokens do login externo | Segredo aleatório compartilhado com a API OP-BP |

Trocar `SECRET_KEY_BASE` desloga todos os usuários. Trocar `SECRET_KEY_JWT` invalida os tokens da API.

## Domínios

| Domínio | Uso | Responsável |
|---------|-----|-------------|
| brasilparticipativo.presidencia.gov.br | Produção | Presidência/Dataprev |
| api-opbp.lablivre.rocks | API OP-BP | LabLivre (**a migrar**) |
| lablivre-unb.github.io/doc-bp | Documentação | LabLivre (organização `lablivre-unb`). O endereço antigo, `rochacarla.github.io/doc-bp`, não redireciona |

O domínio de produção também está escrito no código da [listagem do Orçamento do Povo](../modulos/propostas.md#listagem-do-orcamento-do-povo). Uma troca de domínio exige alterar esse arquivo.
