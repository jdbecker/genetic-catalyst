from src.allele import Allele, base_allele
from src.gene import Gene, base_gene
from src.attribute import Attribute
from src.creature import Creature


def default_creature():
    return Creature(
        base_gene(),
        Gene(
            Allele({Attribute.HEALTH: 1, Attribute.BANDWIDTH: -1}),
            Allele({Attribute.HEALTH: 1, Attribute.BANDWIDTH: -1}),
        ),
    )


def test_creature():
    creature = default_creature()
    assert creature.health == 11
    assert creature.bandwidth == 9
    assert creature.strength == 10


def test_repr():
    assert repr(base_allele()) == repr(eval(repr(base_allele())))
    assert repr(base_gene()) == repr(eval(repr(base_gene())))
    assert repr(default_creature()) == repr(eval(repr(default_creature())))
