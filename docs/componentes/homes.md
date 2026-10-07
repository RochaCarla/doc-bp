# decidim-module-homes

**Tipo**: Componente customizado (LabLivre/UnB)
**Gem no core**: `decidim-homes`
**Repositório**: [decidim-module-homes](https://gitlab.com/lappis-unb/decidimbr/components-brasil-participativo/decidim-module-homes)

Componente que substitui a página inicial padrão do Decidim por uma versão customizada para o Brasil Participativo.

## Funcionalidades

- **Layout customizado** — página inicial com design específico para o contexto brasileiro
- **Destaques** — seções configuráveis para destacar processos participativos ativos
- **Navegação direta** — acesso rápido aos espaços participativos mais relevantes
- **Conteúdo dinâmico** — exibição de processos em andamento, estatísticas e chamadas à ação

## Motivação

A página inicial padrão do Decidim é genérica e não atende às necessidades de comunicação do governo federal brasileiro. Este componente permite uma experiência de entrada mais direcionada e informativa para os cidadãos.

## Uso no core

- **Home das instâncias**: o job `PublicBodiesToInstancesJob` adiciona um componente `homes` a cada instância criada a partir de um órgão público.
- **Dados da home**: o core expõe `GET /api/home_processes`, que devolve os tipos de processo (com seus processos públicos) e as instâncias de primeiro nível. A resposta é cacheada por organização por 10 minutos.
- **Desempenho**: o CSS do core do Decidim deixou de ser carregado na home, e o Webpacker passou a usar `splitChunks` (janeiro de 2026).
