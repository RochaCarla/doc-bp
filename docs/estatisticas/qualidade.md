<!-- Gerado por scripts/estatisticas.py em 2026-10-07T13:21:12+00:00. Não edite à mão. -->

# Qualidade e Boas Práticas

!!! info "Coleta de 07/10/2026"
    Branches `main` e `develop` do [decidim-govbr](https://gitlab.com/lappis-unb/decidimbr/decidim-govbr) e API pública do GitLab. Série a partir de 01/04/2023. "Últimos 12 meses" = 07/10/2025 a 07/10/2026. Para atualizar, rode `python3 scripts/estatisticas.py`.


Indicadores de saúde de projeto de software livre, inspirados nas métricas da [CHAOSS](https://chaoss.community/) e nos critérios do [selo de boas práticas da OpenSSF](https://www.bestpractices.dev/pt-BR/criteria/0).

## Indicadores

|  | Indicador | Valor |
| --- | --- | --- |
| :yellow_circle: | Fator de ausência (pessoas que somam 50% dos commits) | 3 |
| :green_circle: | Contribuidores ativos | 10 |
| :green_circle: | Sucesso de pipelines na `develop` | 97% |
| :yellow_circle: | Mediana de tempo até o merge | 5,9 dias |
| :yellow_circle: | MRs com ao menos um comentário | 46% |
| :yellow_circle: | MRs integrados pelo próprio autor | 15% |
| :green_circle: | Mediana de tempo para fechar issues | 13,9 dias |
| :green_circle: | Commits no padrão Conventional Commits | 96% |
| :red_circle: | Issues abertas há mais de 1 ano | 85% |
| :green_circle: | Versões estáveis publicadas | 29 |
| :red_circle: | Ruby com suporte | 3.0.4 (fim do suporte: 23/04/2024) |
| :red_circle: | Rails com suporte | 6.1.7.2 (fim do suporte: 01/10/2024) |
| :red_circle: | Defasagem do Decidim (versões menores) | 0.27.2 → 0.32.1 (5 atrás) |

### Como ler os indicadores

As faixas abaixo são referências adotadas nesta documentação para orientar a leitura. A CHAOSS define as métricas, mas não estabelece faixas.

| Indicador | :green_circle: | :yellow_circle: | :red_circle: |
| --- | --- | --- | --- |
| Fator de ausência | 4 ou mais | 2 a 3 | 1 |
| Contribuidores ativos (12 meses) | 10 ou mais | 5 a 9 | menos de 5 |
| Sucesso de pipelines | 90% ou mais | 70% a 89% | menos de 70% |
| Mediana até o merge | até 3 dias | até 10 dias | mais de 10 dias |
| MRs com comentário | 70% ou mais | 40% a 69% | menos de 40% |
| MRs integrados pelo autor | até 10% | até 30% | mais de 30% |
| Mediana para fechar issues | até 30 dias | até 90 dias | mais de 90 dias |
| Conventional Commits | 80% ou mais | 50% a 79% | menos de 50% |
| Issues abertas há mais de 1 ano | até 20% | até 50% | mais de 50% |
| Versões estáveis em 12 meses | 4 ou mais | 1 a 3 | nenhuma |
| Ruby e Rails | com suporte | — | sem suporte |
| Defasagem do Decidim | versão atual | 1 a 2 versões menores | 3 ou mais |

## Integração contínua

| Job | Estágio | Bloqueia o pipeline? |
| --- | --- | --- |
| `Lint` | `lint` | Sim |
| `SAST` | `test` | Não (`allow_failure`) |
| `SCA` | `test` | Não (`allow_failure`) |
| `Testing` | `test` | Sim |
| `Build` | `build` | Sim |

### Pipelines nos últimos 12 meses

| Branch | Pipelines | Sucesso | Falha | Cancelados | Outros | Taxa de sucesso |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `develop` | 37 | 36 | 1 | 0 | 0 | 97% |
| `main` | 123 | 111 | 12 | 0 | 0 | 90% |
| todas as branches | 774 | 546 | 228 | 0 | 0 | 71% |

Taxa de sucesso = sucesso ÷ (sucesso + falha). Jobs com `allow_failure` não derrubam o pipeline.

## Testes e análise estática

| Item | Valor |
| --- | ---: |
| Arquivos Ruby em `app/` | 315 |
| Arquivos de teste RSpec (`spec/`) | 135 |
| Arquivos de teste Minitest (`test/`) | 1 |
| Arquivos de teste por arquivo de `app/` | 0,43 |
| Cobertura publicada | Não (SimpleCov instalado, sem relatório no CI) |
| Regras RuboCop desativadas em `.rubocop_todo.yml` | 76 |
| Ocorrências pendentes no `.rubocop_todo.yml` | 2.581 |

## Dependências e plataforma

| Item | Versão em uso | Situação |
| --- | --- | --- |
| Ruby | 3.0.4 | fim do suporte em 23/04/2024; ciclo atual 4.0 |
| Rails | 6.1.7.2 | fim do suporte em 01/10/2024; ciclo atual 8.1 |
| Decidim | 0.27.2 | versão mais recente: 0.32.1 |
| Gemfile.lock | :white_check_mark: | Versões de gems travadas |
| Lockfile JavaScript | yarn.lock | Versões de pacotes travadas |

### Gems instaladas direto de repositórios git

Gems apontadas para uma branch mudam a cada `bundle update`. A versão efetiva fica só no `Gemfile.lock`.

| Gem | Branch | Tag ou commit fixo? |
| --- | --- | --- |
| `decidim-apiauth` | padrão | :x: |
| `decidim-extra_user_fields` | `develop` | :x: |
| `decidim-ej` | `main` | :x: |
| `decidim-homes` | padrão | :x: |
| `decidim-enhanced_process_groups_and_scopes` | `main` | :x: |
| `decidim-mobile` | `main` | :x: |

## Checklist de boas práticas

|  | Prática | Observação |
| --- | --- | --- |
| :white_check_mark: | Licença de software livre | AGPLv3. O nome do arquivo não é o padrão (`LICENSE`), por isso o GitLab não detecta a licença |
| :white_check_mark: | README |  |
| :white_check_mark: | Guia de contribuição | Os links de issues apontam para outro projeto |
| :white_check_mark: | Código de conduta |  |
| :x: | Política de segurança (`SECURITY.md`) | Sem canal documentado para relatar vulnerabilidades |
| :x: | Registro de mudanças (`CHANGELOG`) | 123 tags, sem notas de versão |
| :white_check_mark: | Template de merge request |  |
| :x: | Template de issue |  |
| :white_check_mark: | Lint no CI |  |
| :white_check_mark: | Testes automatizados no CI |  |
| :white_check_mark: | Análise de segurança (SAST) | Não bloqueia o pipeline |
| :white_check_mark: | Análise de dependências (SCA) | Não bloqueia o pipeline |
| :x: | Sem relatórios gerados versionados | `brakeman_report.html` no repositório |

## Limitações

- **Diversidade de organizações** (*Elephant Factor*, CHAOSS) não é calculada: quase todos os commits usam e-mails pessoais, que não indicam a instituição.
- **Revisão de código** é estimada pelo número de comentários do MR, que inclui comentários do próprio autor. Aprovações não estão disponíveis sem autenticação.
- **Issues confidenciais** não aparecem na API pública.
- **Cobertura de testes** não é publicada pelo CI. A razão entre arquivos de teste e de código é só um indicativo.

