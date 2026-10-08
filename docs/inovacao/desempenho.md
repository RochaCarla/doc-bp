---
icon: material/speedometer
---

# Desempenho

Otimizações de desempenho do Brasil Participativo além do [texto participativo](texto-participativo.md), comparadas com o Decidim 0.27.2.

## Melhorias em produção

### Home: API própria com cache

| | |
|---|---|
| **Antes** | A lista de processos da home fazia uma consulta GraphQL sem limite (todos os processos, tipos e instâncias, sem paginação) a cada visita. **Medido (MR !797): "~10 segundos para carregar".** |
| **Depois** | Endpoint `GET /api/home_processes`: consulta direta ao banco, só as colunas usadas, `with_attached_hero_image` (evita N+1), só espaços públicos, cache no Redis por **10 minutos** por organização e cabeçalho `Cache-Control: public, max-age=300, stale-while-revalidate=600` |
| **Evidência** | `app/controllers/api/home_processes_controller.rb`; MR !797 (jun/2026) |

```ruby
data = Rails.cache.fetch("home_processes_v1/org_#{org.id}",
                         expires_in: 10.minutes, race_condition_ttl: 30.seconds) do
  build_home_processes_data
end
expires_in 5.minutes, public: true, stale_while_revalidate: 10.minutes
```

!!! warning "Depende de uma ação manual"
    O ganho só vale se o bloco HTML da home, editado no admin e não versionado, for atualizado para chamar o novo endpoint. O MR !797 descreve o passo a passo. O JavaScript versionado no core (`renderProcesses.js`) ainda usa GraphQL.

### Comentários: paginação e fim do *polling*

| | Decidim 0.27.2 | Brasil Participativo |
|---|---|---|
| Consulta | Pré-carrega autor, grupo, votos positivos e negativos. Ordens "mais votados" e "mais discutidos" ordenam em Ruby, carregando tudo | Sem pré-carregar votos. Só ordens "recentes" e "antigos", feitas no banco |
| Paginação | Nenhuma | 30 por página, com botão "carregar mais" |
| Atualização | *Polling* contínuo a cada **15 s** por página aberta | Um carregamento ao abrir e um novo só depois que o próprio usuário comenta |

**Efeito (inferido):** menos linhas e consultas por requisição e fim do tráfego em segundo plano. Com o Decidim, cada página aberta faz 4 requisições por minuto.

Evidência: `app/queries/decidim/comments/sorted_comments.rb`, `app/controllers/decidim/comments/comments_controller.rb`, `app/packs/src/decidim/comments/comments.component.js`; MR !716 (out/2025), originado no MR !298.

### Front-end: divisão de bundles

| | |
|---|---|
| **Antes** | Um pacote JS/CSS único. Qualquer mudança na aplicação invalidava o cache de tudo |
| **Depois** | `splitChunks` e `runtimeChunk: 'single'` separam bibliotecas (`vendors`), Decidim (`decidim_vendor`) e aplicação |
| **Efeito (medido, MR !767)** | A primeira visita baixa os mesmos bytes, em 3 conexões em vez de 1. O ganho está nas visitas seguintes a um deploy, porque as bibliotecas continuam em cache |
| **Evidência** | `config/webpack/custom.js`; MR !767 (fev/2026) |

A remoção do CSS do Decidim na home (economia estimada de 1,5 MB) foi **revertida** no MR !771: "a economia de performance não foi significativa".

### Outras

| Mudança | Antes | Depois | Efeito | Evidência |
|---------|-------|--------|--------|-----------|
| Exportação de comentários | O serializador do BP buscava a raiz da conversa 2 a 3 vezes por comentário | Memoização (`@root_commentable ||=`) | Inferido: 1 a 2 consultas a menos por comentário exportado | `lib/decidim/comments/comment_serializer.rb` |
| Filtro de categorias | Uma consulta por categoria raiz | Uma consulta ordenada e cache do HTML | Inferido: menos consultas. Ver riscos | `app/helpers/decidim/check_boxes_tree_helper.rb` |
| Rake de autorização gov.br | `NOT IN (subconsulta)` | `LEFT JOIN` com `IS NULL`, em lotes de 1.000 | Inferido: consulta mais eficiente | `app/commands/decidim/govbr/grant_authorization_to_govbr_users.rb` |
| Ativação de etapa | Um `update!` por etapa | `update_all` | Correção funcional; uma atualização em vez de N | `activate_participatory_process_step.rb` |
| Cache da aplicação | Memória do processo | Redis (`REDIS_CACHE_URL`) | Cache compartilhado entre processos | `config/environments/production.rb` |

## Só na branch `develop`

| Mudança | Efeito |
|---------|--------|
| Cascata de vínculos de instâncias usa `ancestors` (`ltree`) em vez de subir a hierarquia nível a nível (`0b4af305`) | Uma consulta em vez de uma por nível |

## Itens que não são ganho em relação ao Decidim

Para evitar interpretações erradas sobre commits com "performance" na mensagem:

| Commit | Situação |
|--------|----------|
| `526878b2` "pequena melhoria na performance" | Revertido em `46f6db96`; não está em vigor |
| `ae705d7e` "pequena melhoria na perfomance" | Mudança no fluxo de login externo, sem efeito de desempenho identificado |
| `dcfa845b`, `c33bd492` (paginação) | O Decidim já pagina propostas e eventos; os commits só ajustam a interface ou o schema |
| `dd563cdb` (remove jquery-ui estático) | O arquivo não era importado; sem efeito em execução |
| `ead87e4b`, `20fda7b9` (eventos geocodificados) | O Decidim já filtra; os commits só acrescentam testes |
| `d1feb6b6` (N+1 em grupos de processos) | O código foi removido do core em janeiro de 2025 |

## Riscos e regressões

!!! danger "Regressão: listagem do Orçamento do Povo sem paginação (inferido)"
    A listagem própria do Orçamento do Povo usa `.page(params[:page]).per(proposals.size)`, ou seja, carrega **todas** as propostas numa página (`proposals_controller.rb`). Em processos com muitas propostas, isso pode ficar lento.

!!! warning "Download de anexos de formulários (inferido)"
    O serviço que gera ZIPs de até 300 MB (MR !709):

    - roda dentro da requisição GET e pode estourar o tempo limite;
    - não limpa o diretório temporário entre ZIPs, então os ZIPs seguintes acumulam os arquivos dos anteriores;
    - não apaga os arquivos gerados;
    - verifica anexos resposta a resposta (N+1).

    Pendências de segurança deste serviço estão em canal restrito ([Segurança e LGPD](../transferencia/seguranca.md#riscos-conhecidos)).

!!! warning "Cache do filtro de categorias (inferido)"
    O HTML em cache inclui o estado marcado das caixas de seleção e um id de objeto, que não fazem parte da chave do cache. Um usuário pode receber o filtro com marcações de outro.

## Configuração de servidor

O repositório tem duas configurações do Puma:

| Arquivo | Configuração | Usado por |
|---------|-------------|-----------|
| `config/puma.rb` | `RAILS_MAX_THREADS` (padrão 5) | `Procfile` |
| `setup/puma.production.rb` | 16 *workers*, 10 a 20 *threads* | `decide-puma.service` |

Não foi possível confirmar qual delas está em uso em produção.

## Índices de banco

Não há índices criados pelo Brasil Participativo em tabelas de propostas ou comentários. Os índices próprios estão nas tabelas `decidim_govbr_*` e de páginas estáticas. Veja o [Banco de Dados](../banco-de-dados/index.md).
