# Plano de Documentação — Brasil Participativo

## Sobre o Projeto

**Brasil Participativo** é a plataforma nacional de participação social digital do governo federal brasileiro, construída como um **fork direto do Decidim** (framework open source de democracia participativa em Ruby on Rails).

**Core**: https://gitlab.com/lappis-unb/decidimbr/decidim-govbr
**Componentes**: https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo
**Produção**: https://brasilparticipativo.presidencia.gov.br/
**Desenvolvimento**: LAPPIS/UnB

### Público-Alvo

| Público | Perfil | Ponto de entrada |
|---------|--------|------------------|
| **Desenvolvedores externos / comunidade** | Querem contribuir com código, criar componentes, entender a arquitetura | Guia do Desenvolvedor |
| **Gestores / operadores do governo** | Querem implantar, configurar e administrar a plataforma | Guia do Operador |

### Tom e Estilo

- **Referência** (arquitetura, módulos, componentes): técnico neutro, voz impessoal
- **Guias e tutoriais**: imperativo/segunda pessoa ("Clone o repositório", "Execute o comando")
- **Idioma**: pt-BR em todo o conteúdo

### Escopo

- **Foco**: core da plataforma (`decidim-govbr`)
- **Periférico**: componentes customizados (gems LAPPIS)
- **Fora de escopo**: documentação do Decidim upstream (referenciar docs oficiais)

---

## Arquitetura

### Relação com o Decidim

O `decidim-govbr` é um **fork direto** do Decidim — não é uma instância que apenas consome gems oficiais. Isso significa:

- Modificações diretas no código upstream
- Necessidade de merge periódico com Decidim upstream
- Componentes customizados adicionados como gems via Gemfile

### Stack

| Camada | Tecnologia | Papel |
|--------|-----------|-------|
| Framework | Decidim (Ruby on Rails) | Base da plataforma |
| Core | decidim-govbr | Fork com customizações brasileiras |
| Componentes | 8 gems customizadas | Extensões desenvolvidas pelo LAPPIS |
| Infraestrutura | Kubernetes | Ambiente de produção |
| Integração externa | EJ (Empurrando Juntas) | Opinião/votação via API |

### Módulos Decidim Ativos (nativos upstream)

Todos os 9 módulos nativos do Decidim estão ativos:

| Módulo | Gem | Função |
|--------|-----|--------|
| Propostas | `decidim-proposals` | Criação, votação, moderação de propostas |
| Reuniões | `decidim-meetings` | Agendamento, inscrição, atas |
| Formulários | `decidim-surveys` / `decidim-forms` | Enquetes e formulários |
| Blog | `decidim-blogs` | Publicação de posts |
| Orçamento Participativo | `decidim-budgets` | Votação em projetos com orçamento limitado |
| Debates | `decidim-debates` | Debates abertos entre participantes |
| Páginas | `decidim-pages` | Páginas estáticas de conteúdo |
| Accountability | `decidim-accountability` | Prestação de contas e acompanhamento |
| Sorteios | `decidim-sortitions` | Seleção aleatória de propostas |

### Componentes Customizados (LAPPIS/UnB)

| Componente | Função |
|------------|--------|
| `decidim-module-homes` | Página inicial customizada |
| `decidim-module-enhanced_templates` | Templates melhorados para processos participativos |
| `decidim-module-enhanced_process_groups_and_scopes` | Agrupamento e escopos de processos (região, tema) |
| `decidim-module-common_questions` | Perguntas frequentes compartilhadas entre processos |
| `decidim-module-questionnaires` | Customização do módulo de questionários |
| `decidim-participatory_text` | Fork do componente oficial de textos participativos |
| `decidim-api-categorization` | Extensão de API para categorização |
| `decidim-ej` | Integração com EJ via API (dependência externa) |

### Dependências Externas

| Serviço | Tipo | Status |
|---------|------|--------|
| Empurrando Juntas (EJ) | API externa — opinião/votação | Confirmado |
| Banco de dados | TBD | A detalhar |
| Cache (Redis) | TBD | A detalhar |
| E-mail | TBD | A detalhar |
| Autenticação (Login Único GovBR) | TBD | A detalhar |

---

## Documentação a Produzir

### Fase 1 — Visão Geral (Prioridade Alta)

Base para ambos os públicos. Define o que é o projeto e como se estrutura.

| Arquivo | Conteúdo |
|---------|----------|
| `docs/index.md` | Home: missão, públicos, links rápidos |
| `docs/visao-geral/sobre.md` | O que é o Brasil Participativo, relação com Decidim, histórico |
| `docs/visao-geral/arquitetura.md` | Diagrama geral: core (fork) + módulos + componentes + EJ + infra |

### Fase 2 — Guia do Desenvolvedor (Prioridade Alta)

Desbloqueia contribuidores externos.

| Arquivo | Conteúdo |
|---------|----------|
| `docs/dev/setup.md` | Pré-requisitos (Ruby, Rails, Node, PostgreSQL), clone, bundle, DB setup, servidor local |
| `docs/dev/estrutura.md` | Organização do repositório `decidim-govbr`, diretórios principais, convenções |
| `docs/dev/contribuir.md` | Fluxo de contribuição, branches, MRs, code review, padrões de commit |
| `docs/dev/criar-componente.md` | Como criar um componente customizado: generator, manifest, models, controllers, views, testes |

### Fase 3 — Guia do Operador (Prioridade Alta)

Desbloqueia implantação por equipes de governo.

| Arquivo | Conteúdo |
|---------|----------|
| `docs/operador/deploy.md` | Deploy em Kubernetes, requisitos de infra, dependências externas |
| `docs/operador/configuracao.md` | Variáveis de ambiente, configuração de serviços, integrações (EJ, e-mail, auth) |
| `docs/operador/administracao.md` | Painel de admin Decidim, gestão de usuários, moderação, espaços participativos |

### Fase 4 — Módulos Decidim (Prioridade Média)

Documentação dos módulos nativos conforme usados no Brasil Participativo.

| Arquivo | Conteúdo |
|---------|----------|
| `docs/modulos/propostas.md` | Criação, votação, moderação de propostas |
| `docs/modulos/reunioes.md` | Agendamento, inscrição, atas |
| `docs/modulos/formularios.md` | Enquetes e formulários |
| `docs/modulos/blog.md` | Publicação de posts |
| `docs/modulos/orcamento.md` | Votação em projetos com orçamento limitado |
| `docs/modulos/debates.md` | Debates abertos |
| `docs/modulos/paginas.md` | Páginas estáticas |
| `docs/modulos/accountability.md` | Prestação de contas |
| `docs/modulos/sorteios.md` | Seleção aleatória |

### Fase 5 — Componentes Customizados (Prioridade Média)

Uma página por componente.

| Arquivo | Conteúdo |
|---------|----------|
| `docs/componentes/homes.md` | Página inicial customizada |
| `docs/componentes/enhanced-templates.md` | Templates melhorados |
| `docs/componentes/enhanced-process-groups.md` | Agrupamento e escopos |
| `docs/componentes/common-questions.md` | Perguntas frequentes compartilhadas |
| `docs/componentes/questionnaires.md` | Questionários customizados |
| `docs/componentes/participatory-text.md` | Textos participativos |
| `docs/componentes/api-categorization.md` | API de categorização |
| `docs/componentes/ej.md` | Integração com EJ (API externa) |

---

## Navegação (`mkdocs.yml`)

```yaml
nav:
  - Home: index.md
  - Visão Geral:
    - Sobre a Plataforma: visao-geral/sobre.md
    - Arquitetura: visao-geral/arquitetura.md
  - Guia do Desenvolvedor:
    - Setup Local: dev/setup.md
    - Estrutura do Código: dev/estrutura.md
    - Como Contribuir: dev/contribuir.md
    - Criar Componente: dev/criar-componente.md
  - Guia do Operador:
    - Deploy: operador/deploy.md
    - Configuração: operador/configuracao.md
    - Administração: operador/administracao.md
  - Módulos:
    - Propostas: modulos/propostas.md
    - Reuniões: modulos/reunioes.md
    - Formulários: modulos/formularios.md
    - Blog: modulos/blog.md
    - Orçamento Participativo: modulos/orcamento.md
    - Debates: modulos/debates.md
    - Páginas: modulos/paginas.md
    - Accountability: modulos/accountability.md
    - Sorteios: modulos/sorteios.md
  - Componentes Customizados:
    - decidim-module-homes: componentes/homes.md
    - decidim-module-enhanced_templates: componentes/enhanced-templates.md
    - decidim-module-enhanced_process_groups_and_scopes: componentes/enhanced-process-groups.md
    - decidim-module-common_questions: componentes/common-questions.md
    - decidim-module-questionnaires: componentes/questionnaires.md
    - decidim-participatory_text: componentes/participatory-text.md
    - decidim-api-categorization: componentes/api-categorization.md
    - decidim-ej: componentes/ej.md
```

---

## Decisões de Design (Registro)

| # | Decisão | Contexto |
|---|---------|----------|
| 1 | Foco no core (`decidim-govbr`), componentes periféricos | Core é onde está a complexidade; componentes são extensions |
| 2 | Nome: "Brasil Participativo — Documentação Técnica" | Explicita que é doc técnica, não manual de usuário |
| 3 | Fork direto do Decidim | Não é instância que consome gems — modificações diretas no upstream |
| 4 | Dois públicos: devs externos + operadores governo | Seções separadas na nav (Guia Dev / Guia Operador) |
| 5 | "Módulo Decidim" vs "Componente customizado" | Terminologia distinta para nativos vs LAPPIS |
| 6 | EJ como dependência externa via API | decidim-ej consome API, não embute nem reimplementa |
| 7 | Infraestrutura: Kubernetes | Demais deps (banco, cache, e-mail, auth) a detalhar |
| 8 | 9 módulos nativos todos ativos | Propostas, reuniões, formulários, blog, orçamento, debates, páginas, accountability, sorteios |

---

## Identidade Visual

| Propriedade | Valor |
|-------------|-------|
| **Paleta** | `primary: purple`, `accent: purple` |
| **Schemes** | `default` (light), `slate` (dark), auto-detect |
| **Font texto** | Inter (Google Fonts) |
| **Font código** | JetBrains Mono |
| **CSS custom** | `docs/stylesheets/custom.css` |
| **Copyright** | LAPPIS/UnB 2025 |
| **Deploy** | GitHub Pages → `https://rochacarla.github.io/doc-bp/` |

---

## Ordem de Execução

| Fase | Seção | Arquivos | Prioridade |
|------|-------|----------|-----------|
| 1 | Visão Geral | 3 | 🔴 Alta |
| 2 | Guia do Desenvolvedor | 4 | 🔴 Alta |
| 3 | Guia do Operador | 3 | 🔴 Alta |
| 4 | Módulos | 9 | 🟡 Média |
| 5 | Componentes Customizados | 8 | 🟡 Média |
| **Total** | — | **27** | — |

---

## Pendências

- [ ] Detalhar dependências externas de infra (banco, cache, e-mail, autenticação)
- [ ] Obter acesso ao repo `decidim-govbr` para analisar estrutura do código
- [ ] Preencher conteúdo dos stubs (todos criados com TODOs)
- [ ] Validar links internos após preenchimento

---

**Status**: 📋 Estrutura montada, stubs criados, conteúdo pendente
**Última atualização**: 2026-05-21
