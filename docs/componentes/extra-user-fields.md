# decidim-extra_user_fields

**Tipo**: Componente customizado (LabLivre/UnB)
**Gem no core**: `decidim-extra_user_fields` (branch `develop`)
**Repositório**: [decidim-extra_user_fields](https://gitlab.com/lappis-unb/decidimbr/decidim-extra_user_fields)

Adiciona campos extras ao cadastro e ao perfil do participante, além dos campos padrão do Decidim.

## Uso no core

- Os dados coletados ficam em `extended_data` do usuário, o mesmo campo usado para guardar o vínculo da [integração OP-BP](../operador/integracao-op-bp.md) (`external_source_id`).

!!! note "Branch de desenvolvimento"
    O `Gemfile` do core aponta para a branch `develop` deste repositório, não para uma versão fixa. O commit efetivo fica registrado no `Gemfile.lock`.
