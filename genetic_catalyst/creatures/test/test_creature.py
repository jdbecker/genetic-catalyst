from django.test import TestCase
from creatures.allele import Allele, base_allele
from creatures.gene import Gene, base_gene
from creatures.attribute import Attribute
from creatures.creature import Creature


class TestCreatures(TestCase):
    def default_creature(self):
        return Creature(
            base_gene(),
            Gene(
                Allele({Attribute("HEALTH", 1), Attribute("BANDWIDTH", -1)}),
                Allele({Attribute("HEALTH", 1), Attribute("BANDWIDTH", -1)}),
            ),
        )

    def test_creature(self):
        creature = self.default_creature()
        self.assertEqual(creature.health, 11)
        self.assertEqual(creature.bandwidth, 9)
        self.assertEqual(creature.strength, 10)

    def test_repr(self):
        self.assertEqual(repr(base_allele()), repr(eval(repr(base_allele()))))
        self.assertEqual(repr(base_gene()), repr(eval(repr(base_gene()))))
        self.assertEqual(
            repr(self.default_creature()), repr(eval(repr(self.default_creature())))
        )
