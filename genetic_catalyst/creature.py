from functools import reduce
from genetic_catalyst.attribute import Attribute
from genetic_catalyst.gene import Gene


class Creature:
    """The Creature is the basic unit of gameplay. Each has a list of Genes from
    which the Creature's Attribute values are derived and each Gene gives a
    bonus to one Attribute and a penalty to another."""

    genes: list[Gene]

    def __init__(self, genes: list[Gene]):
        self.genes = genes

    @property
    def health(self):
        return sum([gene.value(Attribute.HEALTH) for gene in self.genes])

    @property
    def strength(self):
        return sum([gene.value(Attribute.STRENGTH) for gene in self.genes])

    @property
    def intelligence(self):
        return sum([gene.value(Attribute.INTELLIGENCE) for gene in self.genes])

    @property
    def cunning(self):
        return sum([gene.value(Attribute.CUNNING) for gene in self.genes])

    @property
    def bandwidth(self):
        return sum([gene.value(Attribute.BANDWIDTH) for gene in self.genes])

    @property
    def perception(self):
        return sum([gene.value(Attribute.PERCEPTION) for gene in self.genes])

    @property
    def harvesting(self):
        return sum([gene.value(Attribute.HARVESTING) for gene in self.genes])

    @property
    def absorption(self):
        return sum([gene.value(Attribute.ABSORPTION) for gene in self.genes])
