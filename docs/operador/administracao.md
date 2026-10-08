# Administração

Guia para quem administra o Brasil Participativo pelos painéis `/system` e `/admin`.

## Painéis

| Painel | Quem acessa | Para quê |
|--------|-------------|----------|
| `/system` | Administrador de sistema (`Decidim::System::Admin`) | Criar e editar organizações, feature flags |
| `/admin` | Administradores da organização e de espaços | Espaços, componentes, participantes, moderação |
| `/sidekiq` | Operação (Basic Auth) | Filas e jobs |

## Painel `/system`

Além dos campos padrão do Decidim (host, idiomas, modo de registro, autorizações), o formulário da organização tem as feature flags do Brasil Participativo:

| Flag | Efeito |
|------|--------|
| **Remover identidades gov.br duplicadas** | Liga o job que, a cada 5 minutos, mantém só a identidade gov.br mais antiga de usuários com mais de uma |
| **Quantidade de usuários por execução** | Quantos usuários o job processa por vez (padrão 5) |

## Papéis

| Papel | Permissões |
|-------|------------|
| **Administrador da organização** | Acesso total ao `/admin` |
| **Administrador de espaço** | Gestão de um processo ou instância, incluindo dashboard e download de anexos de formulários |
| **Moderador** | Moderação de conteúdo do espaço |
| **Avaliador** | Avaliação de propostas |
| **Colaborador** | Visualização do espaço antes da publicação |

Para promover um usuário pelo console:

```ruby
user = Decidim::User.find_by(email: "admin@gov.br")
user.update!(admin: true)
```

## Espaços participativos

As modalidades exibidas em produção correspondem a dois tipos de espaço do Decidim. Veja [Sobre a Plataforma](../visao-geral/sobre.md#modalidades-de-participacao).

### Processos participativos

Usados para Consultas Públicas, Conferências, Planos Participativos e Audiências Públicas. O **tipo de processo** define em qual menu o processo aparece.

1. Acesse **Admin → Processos** e crie o processo com título, descrição, datas e tipo.
2. Configure as fases. A fase ativa muda automaticamente a cada hora, conforme as datas e o fuso horário da organização.
3. Adicione componentes.
4. Publique.

**Votos mutuamente exclusivos**: na edição do processo, a opção faz com que o participante que votou num componente de propostas não possa votar em outro componente de propostas do mesmo processo. A interface avisa em quais componentes ele já votou.

### Instâncias (assembleias)

Usadas para Conselhos e Colegiados e Fóruns de Participação.

- **Criação automática**: um job horário cria uma instância para cada escopo de órgão público e sub-instâncias para seus setores, já com o componente `homes`.
- **Não listada**: marque **unlisted** para deixar a instância acessível só por link, fora das listagens.

## Componentes

| Componente | Uso típico |
|-----------|------------|
| Propostas | Contribuições, votação, textos participativos, Orçamento do Povo |
| Reuniões | Eventos e audiências |
| Formulários | Enquetes e questionários |
| Blog | Notícias |
| Orçamentos | Votação em projetos com limite financeiro |
| Debates | Discussões abertas |
| Páginas | Conteúdo informativo |
| Homes | Página inicial de uma instância |
| EJ | Conversas do Empurrando Juntas |

Opções específicas do Brasil Participativo estão em [Propostas](../modulos/propostas.md) e [Formulários](../modulos/formularios.md).

## Moderação

Participantes denunciam conteúdo impróprio. Moderadores revisam em **Admin → Moderações**:

- **Ocultar**: remove o conteúdo da visualização pública.
- **Desfazer denúncia**: mantém o conteúdo visível.
- **Bloquear usuário**.

Regras de comentários no Brasil Participativo:

- o autor pode editar o comentário por até **5 minutos** após criá-lo;
- administradores da organização e moderadores do espaço não têm esse limite e podem excluir comentários de outros participantes;
- a exportação de comentários traz `deletado_em` e `moderado_em`.

## Exportações e relatórios

- **Propostas**: a exportação inclui nome e ID do autor.
- **Comentários**: inclui datas de exclusão e moderação.
- **Inscrições em reuniões**: exportáveis pela rota pública de exportação do evento.
- **Estatísticas de propostas por participante**: configuradas por processo (`/admin/participatory_processes/:slug/user_proposals_statistic_settings`), com exportação e atualização forçada. Os dados são recalculados diariamente à 01:00.
- **Anexos de formulários**: download individual ou em ZIP.

## Newsletter

1. Acesse **Admin → Newsletter**.
2. Crie a newsletter.
3. Selecione os destinatários.
4. Envie.

!!! warning "LGPD"
    Envie newsletters apenas para participantes que consentiram em receber comunicações.

## Personalização

Em **Admin → Configurações → Aparência**: logo, favicon, cores e textos. Em **Admin → Páginas**: termos de uso, páginas institucionais e tópicos de páginas, que podem ser publicados e despublicados individualmente.
