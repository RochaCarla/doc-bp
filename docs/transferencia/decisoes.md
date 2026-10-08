# Decisões de arquitetura

Registro das principais decisões técnicas do Brasil Participativo (ADR, *Architecture Decision Records*), reconstruído a partir do código, do histórico e dos merge requests. Serve para que a equipe receptora entenda **por que** o sistema é como é, antes de mudar.

| # | Decisão | Situação |
|---|---------|----------|
| 1 | [Construir sobre o Decidim](#adr-1-construir-sobre-o-decidim) | Aceita |
| 2 | [Customizar por sobrescrita de arquivos](#adr-2-customizar-por-sobrescrita-de-arquivos) | Aceita, com custo alto |
| 3 | [Componentes em gems separadas](#adr-3-componentes-em-gems-separadas) | Aceita |
| 4 | [Login gov.br por OpenID Connect](#adr-4-login-govbr-por-openid-connect) | Aceita |
| 5 | [Vínculo de canais por JWT com segredo compartilhado](#adr-5-vinculo-de-canais-por-jwt) | Aceita; pendência de segurança em canal restrito |
| 6 | [Impersonação por chave de API](#adr-6-impersonacao-por-chave-de-api) | Aceita; pendência de segurança em canal restrito |
| 7 | [Design System gov.br copiado para o core](#adr-7-design-system-govbr-copiado-para-o-core) | Aceita, com custo de atualização |
| 8 | [Renderização leve do texto participativo](#adr-8-renderizacao-leve-do-texto-participativo) | Aceita |
| 9 | [API JSON com cache para a home](#adr-9-api-json-com-cache-para-a-home) | Aceita; depende de ação manual |
| 10 | [Assembleias como instâncias geradas dos órgãos](#adr-10-assembleias-como-instancias) | Aceita |
| 11 | [Fluxo de branches e versões](#adr-11-fluxo-de-branches-e-versoes) | Em revisão |

---

## ADR 1 · Construir sobre o Decidim

- **Contexto:** o governo precisava de uma plataforma de participação com propostas, votações, consultas, reuniões e moderação, auditável e em software livre.
- **Decisão:** usar o Decidim, a partir da evolução do fork *decide* da Nomade, fixado na versão 0.27.2.
- **Consequências:** ganha-se um produto maduro e uma comunidade internacional. Em troca, fica-se preso ao ciclo de versões do Decidim e às suas exigências de Ruby e Rails ([Plano de atualização](atualizacao.md)).
- **Evidência:** `Gemfile` (`DECIDIM_VERSION = '0.27.2'`); README do core.

## ADR 2 · Customizar por sobrescrita de arquivos

- **Contexto:** era preciso mudar telas, regras e permissões do Decidim rapidamente.
- **Decisão:** copiar para o core os arquivos do Decidim a alterar, no mesmo caminho, e deixar o Rails carregar a cópia.
- **Consequências:** mudanças rápidas, mas **492 arquivos** e cerca de 21 mil linhas divergem do original. Cada atualização do Decidim exige revisar cada sobrescrita. Correções de segurança do Decidim não chegam automaticamente aos arquivos sobrescritos.
- **Evidência:** [Inventário de sobrescritas](sobrescritas.md).

## ADR 3 · Componentes em gems separadas

- **Contexto:** algumas funcionalidades são independentes do core (página inicial por blocos, EJ, grupos de processos).
- **Decisão:** desenvolvê-las como gems em repositórios próprios, instaladas via `Gemfile` a partir de branches git.
- **Consequências:** código isolado e reutilizável. Mas as gems apontam para branches (`main`, `develop`) em vez de tags, e a versão efetiva só fica registrada no `Gemfile.lock`.
- **Evidência:** `Gemfile`; [Estatísticas › Qualidade](../estatisticas/qualidade.md#gems-instaladas-direto-de-repositorios-git).

## ADR 4 · Login gov.br por OpenID Connect

- **Contexto:** a participação exige identidade confiável e uma conta por pessoa.
- **Decisão:** autenticar pelo Login Único gov.br com OpenID Connect, PKCE e o escopo `govbr_confiabilidades`. O CPF fica em `decidim_identities.uid`.
- **Consequências:** unicidade e confiabilidade, ao custo de excluir quem não tem conta gov.br. Um job remove identidades duplicadas.
- **Evidência:** `config/initializers/omniauth_govbr.rb`; `RemoveDuplicatedGovbrIdentitiesJob`.

## ADR 5 · Vínculo de canais por JWT

- **Contexto:** a participação por WhatsApp e Telegram precisa ligar o número do participante à conta gov.br.
- **Decisão:** a API OP-BP envia um link com JWT HS256 assinado por segredo compartilhado; o core valida, grava o vínculo em `extended_data` e avisa a API por callback.
- **Consequências:** integração simples e sem estado no core. O segredo compartilhado é ponto único de falha e precisa de rotação. Há pendência de segurança registrada em canal restrito ([Segurança e LGPD](seguranca.md#riscos-conhecidos)).
- **Evidência:** `app/services/external_auth_service.rb`; [Integração OP-BP](../operador/integracao-op-bp.md).

## ADR 6 · Impersonação por chave de API

- **Contexto:** depois do vínculo, a API OP-BP precisa registrar votos e propostas em nome do participante.
- **Decisão:** uma estratégia Warden aceita `X-API-KEY` e `X-USER-ID` e autentica como o usuário indicado.
- **Consequências:** permite a participação por mensageria sem senha, mas exige controles rigorosos sobre a chave. Há pendência de segurança registrada em canal restrito ([Segurança e LGPD](seguranca.md#riscos-conhecidos)).
- **Evidência:** estratégia de autenticação em `lib/decidim/strategies/`.

## ADR 7 · Design System gov.br copiado para o core

- **Contexto:** a plataforma precisava da identidade visual do governo federal.
- **Decisão:** copiar CSS e JS do Design System gov.br para `app/packs/*/govbr-ds/` e reescrever as views com as classes do padrão, por cima do Foundation do Decidim.
- **Consequências:** visual alinhado ao gov.br. Mas os arquivos do padrão foram editados (91 commits) e a versão de origem não foi registrada. Atualizar o padrão exige reconstrução.
- **Evidência:** [Design System gov.br](../design-system/index.md).

## ADR 8 · Renderização leve do texto participativo

- **Contexto:** textos com cerca de 2.000 parágrafos levavam ~80 s para abrir.
- **Decisão:** trocar as *cells* por parágrafo por um partial único, editar um parágrafo por vez e manter o caminho antigo só para textos publicados antes da data de corte v2.
- **Consequências:** ~2 s na medição do MR !560 (a versão atual não foi medida). Coexistência de dois caminhos de renderização.
- **Evidência:** MRs !560, !561, !615, !715; [Inovação › Texto participativo](../inovacao/texto-participativo.md).

## ADR 9 · API JSON com cache para a home

- **Contexto:** a lista de processos da home levava ~10 s com uma consulta GraphQL sem limite a cada visita.
- **Decisão:** endpoint `GET /api/home_processes` com consulta direta e cache de 10 minutos por organização.
- **Consequências:** home mais rápida. O ganho depende de atualizar o bloco HTML da home no painel, que **não é versionado**.
- **Evidência:** MR !797; [APIs](apis.md#get-apihome_processes).

## ADR 10 · Assembleias como instâncias

- **Contexto:** conselhos, colegiados e fóruns de cada órgão precisavam de espaço próprio.
- **Decisão:** usar assembleias do Decidim, chamadas de "instâncias" na interface, criadas de hora em hora a partir dos escopos de órgãos públicos e setores.
- **Consequências:** estrutura automática e padronizada. Depende do cadastro correto dos escopos.
- **Evidência:** `PublicBodiesToInstancesJob`; `config/schedule.rb`.

## ADR 11 · Fluxo de branches e versões

- **Contexto:** até a v1.9.1, `develop` era integrada em `main` e as tags ficavam em `main`. A partir da v1.9.2, as tags ficam na linha de `develop` e em branches `deploy-v*`, e `main` divergiu.
- **Decisão:** **pendente**. Proposta em [Versionamento e release](release.md#fluxo-recomendado).
- **Consequências:** enquanto não houver um fluxo único, não é trivial saber qual commit está em produção.

## Como registrar novas decisões

Para cada decisão relevante, crie uma seção nesta página (ou um arquivo `docs/transferencia/adr/NNN-titulo.md`) com **Contexto**, **Decisão**, **Consequências** e **Evidência**, e atualize a tabela.
