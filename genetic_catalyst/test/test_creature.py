from genetic_catalyst.gene import Gene
from genetic_catalyst.attribute import Attribute
from genetic_catalyst.creature import Creature


def default_creature():
    return Creature(
        [
            Gene(
                {
                    Attribute.HEALTH: 100,
                    Attribute.STRENGTH: 100,
                    Attribute.INTELLIGENCE: 100,
                    Attribute.CUNNING: 100,
                    Attribute.BANDWIDTH: 100,
                    Attribute.PERCEPTION: 100,
                    Attribute.HARVESTING: 100,
                    Attribute.ABSORPTION: 100,
                }
            ),
            Gene({Attribute.HEALTH: 1, Attribute.BANDWIDTH: -1}),
        ],
    )


def test_creature():
    creature = default_creature()
    assert creature.health == 101
    assert creature.bandwidth == 99
    assert creature.strength == 100
