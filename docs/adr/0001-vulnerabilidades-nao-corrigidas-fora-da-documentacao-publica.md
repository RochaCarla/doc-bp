# Vulnerabilidades não corrigidas ficam fora da documentação pública

A documentação é pública (site e e-book) e descreve a plataforma em produção com detalhe de código. Decidimos que vulnerabilidades ainda não corrigidas são registradas apenas numa issue confidencial no GitLab do `decidim-govbr`, e que o site e o e-book trazem só um aviso neutro, porque detalhar uma falha explorável antes da correção entrega o caminho do ataque, e o que é publicado não pode ser "despublicado" (caches, cópias do PDF). Depois de corrigida e implantada, a vulnerabilidade entra na documentação como risco resolvido, com a versão da correção.

## Consequences

- O histórico do git deste repositório guarda a versão anterior das páginas. Optamos por não reescrevê-lo (force-push) e priorizar a correção no core.
- A transferência de tecnologia precisa incluir o acesso da equipe receptora às issues confidenciais.
