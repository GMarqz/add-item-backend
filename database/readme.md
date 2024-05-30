# Documentação do Banco de Dados de Itens de RPG

Esta documentação descreve a estrutura JSON utilizada para armazenar itens em um jogo de RPG básico. Cada item possui atributos que definem suas características e efeitos no jogo.

## Estrutura Geral do Item

Cada item deve ter os seguintes atributos:

- **name**: Nome do item.
- **id**: Identificador único do item.
- **type**: Tipo do item (por exemplo, arma, armadura, poção).
- **hp**: Pontos de vida (Health Points).
- **mp**: Pontos de mana (Magic Points).
- **atk**: Ataque.
- **def**: Defesa.
- **str**: Força.
- **int**: Inteligência.
- **agi**: Agilidade.
- **speed**: Velocidade, com sub-atributos `mvt` (movimento) e `atk` (ataque).
- **evasion**: Evasão.
- **critical**: Crítico, com sub-atributos `rate` (taxa) e `damage` (dano).

## Esquema JSON para os Itens

```json
{
    "name": "item's name",          // Nome do item
    "id": "item's id",              // ID único do item
    "type": "item's type",          // Tipo de item
    "hp": 0,                        // Pontos de vida
    "mp": 0,                        // Pontos de mana
    "atk": 0,                       // Ataque
    "def": 0,                       // Defesa
    "str": 0,                       // Força
    "int": 0,                       // Inteligência
    "agi": 0,                       // Agilidade
    "speed": {
        "mvt": 0,                   // Velocidade de movimento
        "atk": 0                    // Velocidade de ataque
    },
    "evasion": 0,                   // Evasão
    "critical": {
        "rate": 0,                  // Taxa de crítico
        "damage": 0                 // Dano crítico
    }
}
```


### 5. Exemplos de Itens

Forneça exemplos específicos de itens com comentários explicativos.

```markdown
## Exemplos de Itens

### Exemplo de Escudo

```json
{
    "name": "Escudo da Ira",          // Nome do item
    "id": "19eu2da24fa8",             // ID único do item
    "type": "Shield",                 // Tipo de item
    "hp": 10,                         // Pontos de vida
    "mp": 0,                          // Pontos de mana
    "atk": 0,                         // Ataque
    "def": 30,                        // Defesa
    "str": 8,                         // Força
    "int": 0,                         // Inteligência
    "agi": 0,                         // Agilidade
    "speed": {
        "mvt": 0,                     // Velocidade de movimento
        "atk": 0                      // Velocidade de ataque
    },
    "evasion": 0,                     // Evasão
    "critical": {
        "rate": 0,                    // Taxa de crítico
        "damage": 0                   // Dano crítico
    }
}
```

Neste exemplo, o escudo "Escudo da Ira" aumenta os atributos de HP, DEF e STR. A visualização deve ocultar os atributos não utilizados, como atk, mp, e agi.


### 6. Considerações Finais

Adicione qualquer consideração final ou nota sobre a implementação.

```markdown
## Notas Finais

- **Valores Padrão**: Se um atributo não é aplicável a um item específico, ele deve ser definido como 0.
- **Exibição**: A responsabilidade de ocultar atributos não utilizados na interface do usuário é do frontend e backend do sistema.
