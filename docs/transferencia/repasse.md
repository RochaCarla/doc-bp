# Plano de repasse de conhecimento

Trilha de sessões, exercícios práticos e responsabilidades para que a equipe receptora assuma o Brasil Participativo. As sessões usam esta documentação como material de apoio.

## Perfis da equipe receptora

Proposta mínima para manter e evoluir a plataforma:

| Perfil | Quantidade sugerida | Responsabilidades |
|--------|---------------------|-------------------|
| Desenvolvimento Ruby on Rails / Decidim | 2 ou mais | Correções, evolução, atualização do Decidim |
| Front-end | 1 | Views, cells, Design System gov.br |
| Infraestrutura / DevOps | 1 | Implantação, monitoramento, backup, segurança da infraestrutura |
| Banco de dados | Parcial | Desempenho, backup e restauração |
| Produto / dono da plataforma | 1 | Priorização com a SNPS e com as áreas que criam processos |
| Suporte e moderação | Conforme a demanda | Atendimento a gestores e moderação de conteúdo |

## Trilha de sessões

Cada sessão tem cerca de 2 horas: exposição curta, demonstração e um exercício que a equipe receptora executa.

| # | Tema | Material | Exercício |
|---|------|----------|-----------|
| 1 | O produto e as modalidades de participação | [Sobre a Plataforma](../visao-geral/sobre.md), [Manual de Uso](../manual/index.md) | Criar e publicar um processo de teste em homologação |
| 2 | Arquitetura e Decidim | [Arquitetura](../visao-geral/arquitetura.md), [Decisões](decisoes.md) | Seguir o caminho de uma requisição no código |
| 3 | Ambiente e código | [Setup Local](../dev/setup.md), [Estrutura](../dev/estrutura.md), [Sobrescritas](sobrescritas.md) | Subir o ambiente e alterar um texto de uma view sobrescrita |
| 4 | Banco de dados | [Banco de Dados](../banco-de-dados/index.md), [Consultas úteis](../banco-de-dados/consultas.md) | Responder três perguntas de negócio com SQL |
| 5 | Integrações | [Integração OP-BP](../operador/integracao-op-bp.md), [APIs](apis.md) | Rodar `rake botapi:test` e explicar cada etapa |
| 6 | Interface e Design System | [Design System gov.br](../design-system/index.md) | Criar uma tela com componentes do padrão |
| 7 | Testes, CI e release | [Testes](testes.md), [Contribuir](../dev/contribuir.md), [Release](release.md) | Corrigir um defeito com teste, abrir MR e gerar uma versão candidata |
| 8 | Operação | [Operação e continuidade](operacao.md), [Deploy](../operador/deploy.md), [Configuração](../operador/configuracao.md) | Implantar a versão candidata em homologação e fazer *rollback* |
| 9 | Backup e incidentes | [Operação › Backup](operacao.md#backup-e-recuperacao) | Restaurar um backup em ambiente de teste |
| 10 | Segurança e LGPD | [Segurança e LGPD](seguranca.md) | Rotacionar `OP_BP_JWT_SECRET` sem indisponibilidade |
| 11 | Evolução tecnológica | [Plano de atualização](atualizacao.md), [Inovação](../inovacao/index.md) | Remover as sobrescritas idênticas e abrir o MR |
| 12 | Administração e suporte | [Administração](../operador/administracao.md), [Manual › Moderação](../manual/moderacao.md) | Configurar o bot de moderação num processo de teste |

Ao final de cada sessão, registre: participantes, dúvidas abertas e se o exercício foi concluído sem ajuda.

## Operação assistida

Depois da trilha, a equipe receptora conduz a operação por pelo menos **um ciclo completo de release** (sugestão: 4 a 8 semanas), com o LabLivre disponível para dúvidas:

- [ ] uma versão candidata gerada e homologada pelo receptor;
- [ ] uma versão estável implantada em produção pelo receptor;
- [ ] pelo menos um incidente ou chamado tratado pelo receptor;
- [ ] backup restaurado em teste;
- [ ] reunião semanal de acompanhamento registrada.

## Matriz de responsabilidades

Proposta para a fase de operação autônoma. **R** = executa, **A** = responde pelo resultado, **C** = é consultado, **I** = é informado.

| Atividade | Equipe receptora | SNPS | Dataprev | LabLivre |
|-----------|:----------------:|:----:|:--------:|:--------:|
| Priorizar demandas | C | A | I | C* |
| Desenvolver e corrigir | R/A | I | I | C* |
| Revisar código (MR) | R/A | — | — | C* |
| Gerar versão | R/A | I | I | — |
| Implantar em produção | R | A | R | — |
| Monitorar e responder a incidentes | R | I | R/A | — |
| Backup e restauração | C | I | R/A | — |
| Segurança e rotação de segredos | R | A | R | — |
| Atender gestores de processos | R | A | — | — |
| Moderação de conteúdo | C | R/A | — | — |
| Atualização do Decidim | R/A | C | C | C* |

\* Só durante a operação assistida ou sob demanda.

## Encerramento

A transferência termina com:

1. os [critérios de aceite](index.md#criterios-de-aceite) cumpridos;
2. contas e acessos do [Inventário](inventario.md) transferidos ou com a equipe receptora como administradora;
3. acessos do LabLivre revogados ou reduzidos ao combinado;
4. termo de aceite assinado pela SNPS.
