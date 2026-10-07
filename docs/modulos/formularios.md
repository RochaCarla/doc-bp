# Formulários

**Gems**: `decidim-surveys` + `decidim-forms` (com sobrescritas no core)

O módulo de formulários permite criar enquetes e questionários dentro de processos e instâncias.

## Funcionalidades

- **Perguntas variadas**: texto curto e longo, escolha única e múltipla, ordenação, matriz, arquivos.
- **Lógica condicional**: exibir perguntas conforme respostas anteriores.
- **Obrigatoriedade** por pergunta.
- **Respostas anônimas**.
- **Exportação** em CSV, JSON ou Excel.
- **Importação de perguntas** por JSON.

## Opções do Brasil Participativo

| Recurso | Descrição |
|---------|-----------|
| **Limite de arquivos** | Perguntas do tipo arquivo têm `max_files` (1 a 50, padrão 10). O limite aparece no rótulo da pergunta e é validado no envio. Também é aceito na importação por JSON |
| **E-mail de confirmação** | O participante recebe um e-mail quando a resposta é registrada com sucesso |
| **Download de anexos** | Administradores da organização e do espaço baixam os anexos das respostas individualmente ou em ZIP (`/surveys/:id/download_attachments`, `/surveys/:id/download_zip`) |
| **Importação segura** | A importação de perguntas remove bytes ocultos do arquivo |

## Tipos de pergunta

| Tipo | Descrição |
|------|-----------|
| Texto curto | Resposta em uma linha |
| Texto longo | Resposta em várias linhas |
| Escolha única | Uma opção |
| Múltipla escolha | Várias opções |
| Ordenação | Ordenar opções |
| Matriz | Grade de perguntas e opções |
| Arquivos | Upload de anexos, com `max_files` |
| Separador / Título | Organização visual |

## Referência

- [Documentação oficial do Decidim: Surveys](https://docs.decidim.org/en/develop/admin/components/surveys/)
