"""Module containing the Allele class and supporting functions"""
import random
from genetic_catalyst.attribute import Attribute


class Allele:
    """Each gene is made up of a pair of Alleles, one dominant, and one recessive.
    Recessive alleles have no affect on the creature's attributes, but when the
    creature breeds, each gene passes on one random allele to the offspring, so
    recessive genes can reappear in successive generations."""

    attribute_values: dict[Attribute, int]

    def __init__(self, attribute_values: dict[Attribute, int]):
        self.attribute_values = attribute_values

    def __repr__(self) -> str:
        return f"Allele({self.attribute_values})"

    def __str__(self) -> str:
        return str.join(", ", [f"{k}: {v}" for k, v in self.attribute_values.items()])

    def bonus(self) -> int:
        """The total positive bonus this allele provides (used in determining dominance)"""
        return sum(i for i in self.attribute_values.values() if i > 0)

    def dominant_over(self, other: "Allele") -> bool:
        """Alleles with bonuses closer to 0 are more dominant"""
        return self.bonus() >= other.bonus()


def base_allele() -> Allele:
    """Create a 'Base' Allele. Each creature's first Gene is made up of two Base
    Alleles in order to give the creature some starting stats (before the other alleles
    begin subtracting from stats)"""
    return Allele(
        {
            Attribute.HEALTH: 10,
            Attribute.STRENGTH: 10,
            Attribute.INTELLIGENCE: 10,
            Attribute.CUNNING: 10,
            Attribute.BANDWIDTH: 10,
            Attribute.PERCEPTION: 10,
            Attribute.HARVESTING: 10,
            Attribute.ABSORPTION: 10,
        }
    )


def new_allele() -> Allele:
    """Randomly generate a brand new Allele with a +1 boost to one attribute and a -1
    penalty to another"""
    boosted_attribute, penalized_attribute = random.sample(list(Attribute), 2)
    return Allele({boosted_attribute: 1, penalized_attribute: -1})
