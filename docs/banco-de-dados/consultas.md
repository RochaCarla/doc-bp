---
icon: material/database-search
---

# Consultas úteis

Exemplos de SQL para análise e suporte. Use uma **réplica de leitura** ou um dump anonimizado; nunca rode consultas pesadas no banco de produção em horário de uso.

!!! warning "Dados pessoais"
    `decidim_users` e `decidim_identities` têm dados pessoais (e-mail, nome, CPF em `uid`). Respeite a LGPD: selecione só as colunas necessárias e não exporte dados pessoais sem base legal.

## Padrões que se repetem

| Situação | Como consultar |
|----------|----------------|
| Texto traduzível (`jsonb`) | `title->>'pt-BR'` |
| Polimorfismo | Filtre pelo tipo com o nome da classe Ruby: `participatory_space_type = 'Decidim::ParticipatoryProcess'` |
| Somente publicados | `published_at IS NOT NULL` |
| Excluir conteúdo oculto | `LEFT JOIN decidim_moderations m ON … AND m.hidden_at IS NOT NULL` + `WHERE m.id IS NULL` |
| Excluir usuários removidos | `decidim_users.deleted_at IS NULL` |

## Processos e componentes

Componentes de um processo, pelo slug:

```sql
SELECT c.id,
       c.manifest_name,
       c.name->>'pt-BR' AS nome,
       c.published_at IS NOT NULL AS publicado
FROM decidim_components c
JOIN decidim_participatory_processes p
  ON p.id = c.participatory_space_id
 AND c.participatory_space_type = 'Decidim::ParticipatoryProcess'
WHERE p.slug = 'meu-processo'
ORDER BY c.weight;
```

Processos publicados por tipo de processo:

```sql
SELECT t.title->>'pt-BR' AS tipo,
       count(*)          AS processos
FROM decidim_participatory_processes p
JOIN decidim_participatory_process_types t ON t.id = p.decidim_participatory_process_type_id
WHERE p.published_at IS NOT NULL
GROUP BY 1
ORDER BY 2 DESC;
```

## Participação

Propostas, votos e comentários por componente de um processo:

```sql
SELECT c.id                         AS componente,
       c.name->>'pt-BR'             AS nome,
       count(pr.id)                 AS propostas,
       sum(pr.proposal_votes_count) AS votos,
       sum(pr.comments_count)       AS comentarios
FROM decidim_components c
JOIN decidim_participatory_processes p
  ON p.id = c.participatory_space_id
 AND c.participatory_space_type = 'Decidim::ParticipatoryProcess'
JOIN decidim_proposals_proposals pr
  ON pr.decidim_component_id = c.id
 AND pr.published_at IS NOT NULL
WHERE p.slug = 'meu-processo'
  AND c.manifest_name = 'proposals'
GROUP BY 1, 2;
```

As 10 propostas mais votadas de um componente, sem as ocultadas pela moderação:

```sql
SELECT pr.id,
       pr.title->>'pt-BR' AS titulo,
       pr.proposal_votes_count
FROM decidim_proposals_proposals pr
LEFT JOIN decidim_moderations m
  ON m.decidim_reportable_type = 'Decidim::Proposals::Proposal'
 AND m.decidim_reportable_id = pr.id
 AND m.hidden_at IS NOT NULL
WHERE pr.decidim_component_id = 123
  AND pr.published_at IS NOT NULL
  AND m.id IS NULL
ORDER BY pr.proposal_votes_count DESC
LIMIT 10;
```

Parágrafos de um texto participativo, na ordem:

```sql
SELECT pr.position,
       pr.participatory_text_level,
       pr.title->>'pt-BR' AS titulo,
       pr.comments_count
FROM decidim_proposals_proposals pr
WHERE pr.decidim_component_id = 123
  AND pr.participatory_text_level IS NOT NULL
ORDER BY pr.position;
```

Respostas por formulário:

```sql
SELECT q.id                            AS questionario,
       count(DISTINCT a.session_token) AS respondentes,
       count(*)                        AS respostas
FROM decidim_forms_questionnaires q
JOIN decidim_forms_answers a ON a.decidim_questionnaire_id = q.id
WHERE q.questionnaire_for_type = 'Decidim::Surveys::Survey'
GROUP BY 1
ORDER BY 2 DESC;
```

## Usuários e login

Novos cadastros por mês:

```sql
SELECT date_trunc('month', created_at)::date AS mes,
       count(*)                              AS cadastros
FROM decidim_users
WHERE type = 'Decidim::User'
  AND deleted_at IS NULL
GROUP BY 1
ORDER BY 1;
```

Usuários com mais de uma identidade gov.br (o que o job `RemoveDuplicatedGovbrIdentitiesJob` corrige):

```sql
SELECT decidim_user_id,
       count(*) AS identidades
FROM decidim_identities
WHERE provider = 'govbr'
GROUP BY 1
HAVING count(*) > 1
ORDER BY 2 DESC;
```

Contas vinculadas pela [integração OP-BP](../operador/integracao-op-bp.md):

```sql
SELECT count(*)
FROM decidim_users
WHERE extended_data ? 'external_source_id';
```

## Moderação

Conteúdos denunciados ainda visíveis, por espaço:

```sql
SELECT m.decidim_participatory_space_type,
       m.decidim_participatory_space_id,
       m.decidim_reportable_type,
       count(*)            AS itens,
       sum(m.report_count) AS denuncias
FROM decidim_moderations m
WHERE m.hidden_at IS NULL
GROUP BY 1, 2, 3
ORDER BY denuncias DESC;
```

## Desempenho

Maiores tabelas do banco:

```sql
SELECT relname                                       AS tabela,
       pg_size_pretty(pg_total_relation_size(relid)) AS tamanho,
       n_live_tup                                    AS linhas
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC
LIMIT 15;
```

!!! tip "Índices"
    As colunas de referência por convenção (`decidim_*_id`) normalmente têm índice, mas não têm chave estrangeira. Antes de criar consultas novas sobre tabelas grandes, confira a lista de índices na página do domínio.
