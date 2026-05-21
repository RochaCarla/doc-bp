# Administração

Guia para administradores que operam o painel administrativo do Brasil Participativo.

## Painel Administrativo

O Decidim inclui um painel admin completo acessível em `/admin`. Apenas usuários com role de administrador têm acesso.

### Acesso

```
https://<domínio>/admin
```

Use as credenciais de administrador configuradas no seed ou criadas manualmente.

## Gestão de Usuários

### Roles

| Role | Permissões |
|------|------------|
| **Super Admin** | Acesso total — configuração do sistema, gestão de organizações |
| **Admin** | Gestão de espaços participativos, componentes, usuários |
| **Moderador** | Moderação de conteúdo (propostas, comentários, denúncias) |
| **Colaborador** | Criação de conteúdo sem permissões administrativas |

### Criar um administrador via console

```bash
bin/rails console
```

```ruby
user = Decidim::User.find_by(email: "admin@gov.br")
user.update!(admin: true)
```

### Convidar administradores pelo painel

1. Acesse **Admin → Participantes → Admins**
2. Clique em **Convidar participante**
3. Preencha e-mail e role desejado

## Espaços Participativos

Os espaços são os containers organizacionais onde a participação acontece:

### Processo Participativo

O tipo mais comum. Possui fases temporais:

1. **Acesse** Admin → Processos
2. **Crie** um novo processo com título, descrição e datas
3. **Configure fases** (informação, debate, votação, resultados)
4. **Adicione componentes** (propostas, reuniões, formulários, etc.)
5. **Publique** quando estiver pronto

### Assembleia

Espaço permanente para órgãos colegiados:

1. Acesse Admin → Assembleias
2. Crie com nome, descrição e tipo (consultiva, deliberativa, etc.)
3. Adicione membros e componentes

### Conferência

Espaço para eventos com programação:

1. Acesse Admin → Conferências
2. Configure datas, local, palestrantes e programação

## Componentes

Dentro de cada espaço, adicione componentes conforme a necessidade:

| Componente | Uso típico |
|-----------|------------|
| Propostas | Coletar contribuições dos participantes |
| Reuniões | Agendar encontros presenciais ou virtuais |
| Formulários | Enquetes e questionários |
| Blog | Comunicar atualizações |
| Orçamento | Votação em projetos com limite financeiro |
| Debates | Discussões abertas |
| Páginas | Conteúdo informativo estático |

Para adicionar:

1. Dentro do espaço, acesse **Componentes**
2. Clique em **Adicionar componente**
3. Escolha o tipo e configure as opções

## Moderação

### Denúncias

Participantes podem denunciar conteúdo impróprio. Moderadores revisam em:

**Admin → Moderação**

Ações disponíveis:

- **Ocultar** — remove o conteúdo da visualização pública
- **Rejeitar denúncia** — mantém o conteúdo visível
- **Suspender usuário** — bloqueia temporariamente

### Moderação de Propostas

1. Acesse o componente de propostas no espaço
2. Use filtros para encontrar propostas denunciadas
3. Aplique a ação apropriada

## Newsletter

Envie comunicações aos participantes:

1. Acesse **Admin → Newsletter**
2. Crie uma nova newsletter com título e corpo
3. Selecione os destinatários (todos, segmento específico)
4. Envie ou agende

!!! warning "LGPD"
    Respeite a Lei Geral de Proteção de Dados. Envie newsletters apenas para participantes que consentiram em receber comunicações.

## Personalização

### Aparência

Em **Admin → Configuração → Aparência**:

- Logo e favicon
- Cores do tema
- Texto de boas-vindas
- Rodapé customizado

### Páginas estáticas

Em **Admin → Páginas**:

- Termos de uso
- Política de privacidade
- Perguntas frequentes
- Páginas informativas customizadas
