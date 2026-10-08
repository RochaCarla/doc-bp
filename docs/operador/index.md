---
icon: material/server
---

# Guia de Operação

Para a **equipe de operação**: quem implanta, configura, integra e administra o Brasil Participativo.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **[Deploy](deploy.md)**

    ---

    Processos (`web`, `worker`, `cron`), pré-requisitos e passo a passo de implantação.

-   :material-tune:{ .lg .middle } **[Configuração](configuracao.md)**

    ---

    Referência das variáveis de ambiente: Decidim, banco, Redis, SMTP, storage e integrações.

-   :material-whatsapp:{ .lg .middle } **[Integração OP-BP](integracao-op-bp.md)**

    ---

    Vínculo de contas gov.br vindas do WhatsApp e do Telegram, com JWT e callback.

-   :material-shield-crown:{ .lg .middle } **[Administração](administracao.md)**

    ---

    Painéis `/system` e `/admin`, feature flags, papéis, moderação e exportações.

</div>

## Checklist rápido

- [ ] PostgreSQL, Redis (fila e cache), SMTP e storage disponíveis
- [ ] `ALLOW_HOSTS`, `SECRET_KEY_BASE` e `SECRET_KEY_JWT` definidas
- [ ] Credenciais do gov.br configuradas
- [ ] `worker` e `cron` rodando
- [ ] `/sidekiq` protegido

Detalhes em [Deploy › Checklist](deploy.md#checklist).

## Riscos conhecidos

!!! danger "Plataforma sem suporte de segurança"
    Ruby 3.0 e Rails 6.1 já não recebem correções de segurança, e o Decidim está 5 versões menores atrás da mais recente. Veja [Estatísticas › Qualidade](../estatisticas/qualidade.md#dependencias-e-plataforma).

!!! warning "Vulnerabilidades em acompanhamento"
    Há vulnerabilidades conhecidas registradas em canal restrito. Veja [Segurança e LGPD](../transferencia/seguranca.md#riscos-conhecidos).
