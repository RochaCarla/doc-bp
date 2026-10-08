# Especificação — Documentação técnica do Brasil Participativo

Site estático de documentação, com versão em e-book (PDF), que reúne o conhecimento técnico, operacional e de uso do Brasil Participativo, para que equipes de desenvolvimento, operação e gestão consigam entender, operar, usar e assumir a plataforma.

Os termos em **negrito** estão definidos em [CONTEXT.md](./CONTEXT.md). As decisões estruturais estão na § 10 e, quando exigem registro próprio, em [docs/adr/](./docs/adr/). Este documento descreve o que está construído (*as-built*, outubro de 2026) e serve de referência para mudanças futuras.

---

## 1. Escopo

**Está no escopo**

- Site em português, publicado no GitHub Pages em `https://lablivre-unb.github.io/doc-bp/`, com nove abas: Início, Documentação, Transferência, Manual de Uso, Design System, Inovação, Estudos, Estatísticas e Sobre.
- Documentação do **core** (`decidim-govbr`): arquitetura, desenvolvimento, operação, configuração, integrações, administração, **banco de dados**, **módulos** e **componentes customizados**.
- Pacote de **transferência de tecnologia** para a **equipe receptora**.
- **Manual de uso** para gestores de processos, reescrito a partir dos guias publicados na plataforma.
- **Estudos** sobre participação, com ficha padronizada.
- Indicadores de software livre (**Estatísticas**) e diferenças em relação ao Decidim (**Inovação**).
- **Páginas geradas** por scripts a partir do código e de APIs públicas.
- **E-book** com todo o conteúdo do site, gerado a cada publicação.
- Identidade visual baseada no Design System gov.br, com **rodapé institucional**.

**Não está no escopo**

- Documentação do Decidim *upstream*: só se referencia a documentação oficial.
- Alterações no código do `decidim-govbr` ou dos componentes. A documentação descreve; não corrige.
- Valores de segredos, dados pessoais de usuários da plataforma e cópias de documentos internos do projeto.
- Detalhes de vulnerabilidades ainda não corrigidas, que ficam em issue confidencial no GitLab do core ([ADR 0001](./docs/adr/0001-vulnerabilidades-nao-corrigidas-fora-da-documentacao-publica.md)).
- Marca oficial da Secretaria sem o arquivo autorizado (ver § 13).
- Tradução para outros idiomas.
- Qualquer backend: o site é estático (RNF08).

## 2. Personas e uso dominante

| Persona | Uso dominante | Ponto de entrada |
|---|---|---|
| Desenvolvedor | "Como subo o ambiente e onde mudo este comportamento?" | Trilhas › Desenvolvedor, Documentação › Desenvolvimento |
| Equipe de operação | "Como implanto, configuro e recupero a plataforma?" | Documentação › Operação, Transferência › Operação e continuidade |
| Gestor de processo | "Como crio e publico um processo participativo?" | Manual de Uso |
| **Equipe receptora** | "O que preciso receber e saber para assumir a plataforma?" | Transferência |
| Gestão e pesquisa | "Como o projeto evolui e o que ele mudou no Decidim?" | Estatísticas, Inovação, Estudos |

A home (`docs/index.md`) direciona cada persona em um clique, e a página **Trilhas de aprendizado** dá a ordem de leitura de cada uma.

## 3. Fontes de conteúdo

Todo conteúdo técnico vem de uma fonte verificável. Fontes em uso:

| Fonte | Usada em | Como é lida |
|---|---|---|
| Repositório `decidim-govbr` (branches `main` e `develop`) | Arquitetura, configuração, banco, inovação, transferência | Clone *bare* em `.cache/estatisticas/` |
| API pública do GitLab | Estatísticas | `scripts/estatisticas.py` |
| Decidim na tag `v0.27.2` | Inventário de sobrescritas, Inovação | Clone em `.cache/decidim-v0.27.2/` |
| Páginas de produção (`/processes/brasilparticipativo/f/1400/` e `f/1401/`, `/pages`) | Sobre a Plataforma, Manual de Uso | Leitura manual; reescrita com link para o original |
| Descrições de merge requests | Inovação, decisões de arquitetura | API do GitLab |
| Relatório "Orçamento do Povo" (Google Docs) | Estudos | Leitura manual; resumo com link para o original |
| `lablivre.unb.br` | Logos do rodapé e da contracapa | Arquivos copiados para `docs/assets/logos/` |
| rubygems.org e endoflife.date | Versões e fim de suporte | `scripts/estatisticas.py` e leitura manual |

**Regras para o que a fonte não cobre**

- Informação que não está no código nem em fonte pública é marcada **a confirmar** e nunca inventada.
- Afirmação de desempenho é rotulada **medida** (número publicado num MR) ou **inferida** (leitura de código).
- Links para documentos internos (Google Drive, Docs, Figma) não são publicados. As citações ficam como "documento interno".

## 4. Arquitetura da informação

| Aba | Seções e páginas | Origem |
|---|---|---|
| Início | Home, Trilhas de aprendizado, Novidades | Manual |
| Documentação | Visão Geral (3), Desenvolvimento (5), Operação (5), Banco de Dados (13), Módulos Decidim (9), Componentes Customizados (9) | Manual, exceto Banco de Dados (gerado, menos `consultas.md`) |
| Transferência | Plano e 10 documentos | Manual, exceto `sobrescritas.md` (gerado) |
| Manual de Uso | 7 páginas | Manual, a partir de `/pages` |
| Design System | 3 páginas | Manual |
| Inovação | 4 páginas | Manual |
| Estudos | Índice e um estudo | Manual |
| Estatísticas | 5 páginas e `dados.json` | Gerado |
| Sobre | Sobre e Uso de IA | Manual |

São 80 páginas Markdown, das quais 18 são geradas, com 56 diagramas. Toda página nova entra no `nav:` do `mkdocs.yml`.

## 5. Geradores

Scripts em `scripts/`, em Python só com a biblioteca padrão (3.9+), reproduzíveis a partir de `.cache/` (ignorado pelo git). Cada página gerada traz `title` no *front matter* e o comentário `<!-- Gerado por scripts/… Não edite à mão. -->`.

| Script | Entrada | Saída |
|---|---|---|
| `estatisticas.py` | Clone do core, API do GitLab, rubygems, endoflife.date | `docs/estatisticas/*.md` e `dados.json` |
| `banco_de_dados.py` | `db/schema.rb` e `db/migrate/` da `main` | `docs/banco-de-dados/*.md`, exceto `consultas.md` |
| `sobrescritas.py` | Arquivos de `app/`, `lib/` e `config/initializers/` da `main` e o Decidim `v0.27.2` | `docs/transferencia/sobrescritas.md` |
| `gerar_pdf.cjs` | Site já construído (pasta) | E-book em PDF |

**Invariantes**

- `estatisticas.py`: a **série analisada** começa em 01/04/2023 (`SERIES_START`). Variações de nome e e-mail da mesma pessoa são agrupadas; e-mails nunca são publicados. Os gráficos usam barras e linhas (sem pizza), horizontais quando há mais de 12 rótulos, nas cores `#1351b4` e `#ff8c00`.
- `banco_de_dados.py`: cada coluna recebe a origem (Decidim, Brasil Participativo ou gem) pela migração que a criou. Referências sem chave estrangeira são inferidas pela convenção `decidim_<entidade>_id` e marcadas como tal. Os diagramas de relação saem um por grupo de tabelas conectadas, com rótulos quebrados em linhas de até 13 caracteres e direção escolhida pela menor largura.
- `sobrescritas.py`: um arquivo é **sobrescrita** quando o mesmo caminho existe numa gem do Decidim 0.27.2. A diferença é medida em linhas adicionadas e removidas.

## 6. Interface

Material for MkDocs com o tema do Design System gov.br (`docs/stylesheets/custom.css`, `overrides/`).

- **Tokens**: azul `#1351b4` (*blue-warm-vivid-70*), `#0c326f` e `#071d41`; cinzas e cores de status do padrão; fonte Rawline, com Raleway como reserva.
- **Cabeçalho e abas**: fundo claro, aba ativa com barra azul de 4 px. Modo escuro com fundo `#0b1a33`.
- **Componentes**: botões em pílula, *cards* com sombra do padrão, avisos com as cores de status, tabelas com cabeçalho `#edf5ff`.
- **Barra de aviso** no topo, dispensável pelo usuário.
- **Rodapé de página**, em toda página exceto a home: "Reportar um problema" (abre issue no GitHub com o título da página), "Baixar tudo em PDF" e "Sugerir uma edição".
- **Rodapé institucional**, em toda página: grupos "Realização" (LabLivre e UnB, logos em branco) e "Parceria" (Secretaria, assinatura em texto), com texto do TED, contatos e links. Os itens vêm de `extra.institucional` no `mkdocs.yml`; item sem `image` aparece como assinatura em texto.
- **Diagramas**: Mermaid 11. Fluxos verticais numerados no lugar de diagramas de sequência. Nenhum diagrama pode exceder a largura da coluna de conteúdo (RNF03).

## 7. E-book

Gerado por `scripts/gerar_pdf.cjs` a partir da página única `/print_page/` (plugin `print-site`), em quatro impressões unidas com `pdf-lib`:

| Parte | Conteúdo | Margem | Numeração |
|---|---|---|---|
| Capa | Fundo azul em página A4 inteira, título, instituições, edição | Nenhuma | Não |
| Folha de rosto e apresentação | Ficha técnica, "como citar", organização, públicos, convenções | 22 mm | Não |
| Miolo | Sumário e todo o conteúdo, uma seção por página, abas em sequência com título, blocos recolhidos abertos | 18 × 16 mm | Rodapé com título e número; marcadores do PDF |
| Contracapa | Resumo, logos, "Dinheiro público, código público." | Nenhuma | Não |

A home fica fora do e-book (`exclude: index.md`). A data da edição, a versão (`DOC_VERSION`, commit curto no CI) e o "Acesso em" da citação são preenchidos na geração. O arquivo é publicado em `/documentacao-brasil-participativo.pdf`.

## 8. Build e publicação

| Item | Valor |
|---|---|
| Ferramentas | MkDocs `>=1.6,<2`, Material 9.7.7, `mkdocs-print-site-plugin` 2.9 |
| Desenvolvimento | `docker compose up -d docs` → `http://localhost:8000/doc-bp/` (imagem do `Dockerfile`) |
| E-book local | `./scripts/pdf.sh` → `dist/`. Usa o Chrome local com Node arm64; caso contrário, o container `docker/pdf.Dockerfile` (Puppeteer 25.12.0, pdf-lib 1.17.1) |
| Publicação | Um único workflow (`.github/workflows/deploy.yml`) a cada push na `main`: `mkdocs build --strict`, geração do e-book (não bloqueia o deploy) e GitHub Pages |

## 9. Requisitos

**Funcionais**

| ID | Requisito |
|---|---|
| RF01 | O site DEVE organizar o conteúdo nas nove abas da § 4, cada uma com uma página de entrada. |
| RF02 | O site DEVE oferecer busca em português em todo o conteúdo. |
| RF03 | Toda página, exceto a home, DEVE ter o rodapé de página com reportar problema, baixar PDF e sugerir edição. |
| RF04 | O e-book DEVE conter todas as páginas do site, exceto a home, na estrutura da § 7. |
| RF05 | Toda página gerada DEVE ser reproduzível pelo seu script, sem edição manual. |
| RF06 | As Estatísticas DEVEM cobrir a série a partir de 01/04/2023 e informar a data da coleta. |
| RF07 | O Banco de Dados DEVE documentar todas as tabelas do `db/schema.rb`, com colunas, tipos, índices, referências e origem. |
| RF08 | A Transferência DEVE listar cada documento exigido e sua situação, e marcar como **a confirmar** o que não tem fonte. |
| RF09 | Todo estudo DEVE ter a ficha da § 3 do índice de Estudos e o link para o documento original. |
| RF10 | Todo guia do Manual de Uso DEVE apontar para o guia original na plataforma. |
| RF11 | O rodapé institucional DEVE exibir Realização e Parceria a partir de `extra.institucional`. |

**Não funcionais**

| ID | Requisito |
|---|---|
| RNF01 | Todo o conteúdo DEVE estar em português do Brasil. |
| RNF02 | O build estrito NÃO PODE emitir avisos. |
| RNF03 | Nenhum diagrama PODE ser reduzido a menos de 85% do tamanho natural na coluna de conteúdo (cerca de 690 px). |
| RNF04 | Afirmações técnicas DEVEM ter fonte verificável; desempenho DEVE ser rotulado como medido ou inferido. |
| RNF05 | O repositório NÃO PODE conter valores de segredos, e-mails de contribuidores ou dados pessoais de usuários da plataforma. |
| RNF06 | As versões de ferramentas DEVEM ser fixas e iguais no Docker e no CI. |
| RNF07 | Textos e logos DEVEM ter contraste suficiente sobre o fundo (logos escuros invertidos para branco no rodapé escuro); toda imagem DEVE ter texto alternativo. |
| RNF08 | O site DEVE ser servido inteiramente pelo GitHub Pages, sem servidor próprio. |
| RNF09 | O site e o e-book NÃO PODEM detalhar vulnerabilidades ainda não corrigidas; exibem só um aviso neutro que aponta para o canal restrito. |

**Critérios de aceitação**

| ID | Critério verificável |
|---|---|
| RF01 | O `nav:` do `mkdocs.yml` tem exatamente as nove abas da § 4, cada uma com `index.md` ou página inicial. |
| RF02 | Buscar "instância" no site retorna o Glossário e Processos e instâncias. |
| RF03 | O HTML de qualquer página, exceto `/`, contém `bp-page-footer` com os três links. |
| RF04 | `./scripts/pdf.sh` (ou o log do CI) termina com "PDF gerado"; a página 1 é a capa, a 2 a folha de rosto, a 3 a apresentação, a 4 o sumário e a última a contracapa; o sumário lista todas as abas, exceto a home. |
| RF05 | Rodar os três scripts Python sobre um clone limpo não produz diferença no `git diff`, salvo datas de coleta e números que mudaram na fonte. |
| RF06 | `docs/estatisticas/index.md` mostra "Início da série analisada: 01/04/2023". |
| RF07 | O número de tabelas em `docs/banco-de-dados/index.md` é igual ao de `create_table` no `db/schema.rb`. |
| RF08 | `docs/transferencia/index.md` tem uma linha por documento do pacote, com situação. |
| RF09 | `docs/estudos/orcamento-do-povo.md` tem a tabela "Ficha" e o link do documento. |
| RF10 | Cada página em `docs/manual/`, exceto índice e cidadão, tem o botão "Guia original". |
| RF11 | Remover `image` do item UnB em `extra.institucional` faz o rodapé exibi-lo como texto, sem erro de build. |
| RNF02 | `docker compose run --rm docs build --strict` termina sem `WARNING`. |
| RNF03 | `python3 scripts/medir_diagramas.py` (Mermaid 11, coluna de 690 px) termina com código 0: todos os diagramas com escala ≥ 0,85. |
| RNF05 | `grep -rE "@(gmail|hotmail|protonmail)\.com" docs` não retorna nada. |
| RNF06 | As versões no `Dockerfile`, no `docker-compose.yml` e no `deploy.yml` coincidem. |
| RNF09 | A página Segurança e LGPD tem o aviso de canal restrito, e nenhuma página descreve como explorar uma falha aberta (revisão a cada mudança em `docs/transferencia/`, `docs/operador/` e `docs/inovacao/`). |

## 10. Decisões

| Decisão | Motivo |
|---|---|
| MkDocs com Material, fixado em `<2` | O MkDocs 2.0 remove plugins e *overrides* usados aqui |
| Conteúdo gerado por scripts em Python sem dependências | Reproduzível em qualquer máquina e no CI, sem ambiente extra |
| Clone *bare* do core em `.cache/` | Lê `main` e `develop` sem tocar no clone de trabalho de ninguém |
| E-book montado em partes com Puppeteer e `pdf-lib` | Capa e contracapa sem margem e miolo numerado exigem impressões diferentes; o Chrome renderiza os diagramas Mermaid |
| Espera dos diagramas pela troca de `pre.mermaid` por `div.mermaid` | O Material desenha os diagramas em shadow DOM fechado |
| Diagramas verticais e gráficos horizontais | Diagramas largos são reduzidos até ficarem ilegíveis |
| Secretaria como assinatura em texto | Falta o arquivo oficial da marca e há regras próprias no período eleitoral |
| Um único workflow de deploy | Três workflows publicavam no mesmo destino e podiam apagar o e-book |
| Manual reescrito, com link para o original | As capturas da plataforma estão em links temporários |
| Repositório na organização `lablivre-unb` | A URL fica gravada no e-book e nas citações, e o GitHub não redireciona endereços do Pages; uma conta pessoal prende o produto a uma pessoa. Ver [ADR 0002](./docs/adr/0002-documentacao-na-organizacao-lablivre-unb.md) |
| Vulnerabilidades abertas só em issue confidencial | Detalhar falha antes da correção entrega o caminho do ataque; ver [ADR 0001](./docs/adr/0001-vulnerabilidades-nao-corrigidas-fora-da-documentacao-publica.md) |

## 11. Regras editoriais

- Voz direta, frases curtas, termos do [CONTEXT.md](./CONTEXT.md). Na interface, "instância", nunca "assembleia".
- Guias e tutoriais no imperativo; referência em tom neutro.
- Toda página termina com links de "Próximos passos" ou "Veja também" quando houver continuidade.
- Achados de risco aparecem em aviso vermelho (`danger`); pendências, em amarelo (`warning`).
- Commits em Conventional Commits; commits feitos com apoio de IA mantêm a linha `Co-Authored-By`.
- O uso de IA segue a declaração em `docs/sobre/uso-de-ia.md` (ferramentas, salvaguardas e regras de contribuição).

## 12. Riscos

| Risco | Mitigação |
|---|---|
| Lançamento do MkDocs 2.0 | Versões fixas no Docker e no CI (§ 8) |
| API do GitLab muda ou limita requisições | `GITLAB_TOKEN` opcional; páginas geradas ficam versionadas até a próxima coleta |
| Conteúdo de produção muda (guias, números) | Datas de coleta nas páginas; links para os originais |
| Itens **a confirmar** envelhecem | Listados no Inventário e em Segurança e LGPD como pendências da fase de preparação |
| Geração do e-book falha no CI | Etapa não bloqueia o deploy; o site continua publicado |
| Nomes de contribuidores nas Estatísticas | Vêm do histórico público do git; e-mails nunca são publicados |

## 13. Questões em aberto

Adiadas de propósito:

- Licença do conteúdo da documentação (o software é AGPLv3).
- Número e vigência do TED; nomes da equipe na folha de rosto.
- Arquivo oficial da marca da Secretaria, conforme as regras do período eleitoral.
- Migração do domínio `api-opbp.lablivre.rocks` para a equipe receptora.
- Domínio próprio para a documentação, sob `lablivre.unb.br`.

## 14. Verificação

```sh
docker compose run --rm docs build --strict          # RNF02, RF01, RF03
python3 scripts/estatisticas.py                      # RF05, RF06
python3 scripts/banco_de_dados.py                    # RF05, RF07
python3 scripts/sobrescritas.py                      # RF05
./scripts/pdf.sh                                     # RF04 (dist/documentacao-brasil-participativo.pdf)
python3 scripts/medir_diagramas.py                   # RNF03 (requer Google Chrome)
grep -rE "@(gmail|hotmail|protonmail)\.com" docs     # RNF05: sem saída
```
