"""Module containing the Allele class and supporting functions"""
from enum import Enum
import random
from genetic_catalyst.attribute import Attribute
from copy import deepcopy

from genetic_catalyst.utils import fibonacci_shift

MUTATION_CHANCE = 0.1


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

    def bonus_attribute(self) -> Attribute:
        return max(self.attribute_values, key=self.attribute_values.get)  # type: ignore

    def penalty(self) -> int:
        """The total negative penalty this allele provides (used in mutation logic)"""
        return sum(i for i in self.attribute_values.values() if i < 0)

    def penalty_attribute(self) -> Attribute:
        return min(self.attribute_values, key=self.attribute_values.get)  # type: ignore

    def dominant_over(self, other: "Allele") -> bool:
        """Alleles with bonuses closer to 0 are more dominant"""
        return self.bonus() >= other.bonus()

    def propagate(self) -> "Allele":
        """logic for propagating and mutating alleles"""
        if self.penalty() == 0:
            return deepcopy(self)  # Base allele has different rules for propagation
        else:
            if random.random() < MUTATION_CHANCE:
                return self._mutate()
            else:
                return deepcopy(self)

    def _mutate(self) -> "Allele":
        new_bonus = self.bonus()
        match (random.choice(list(MutateDirection))):
            case MutateDirection.DOWN:
                new_bonus -= 1
            case MutateDirection.UP:
                new_bonus += 1
        if new_bonus <= 0:
            return new_allele()
        else:
            return Allele(
                {
                    self.bonus_attribute(): new_bonus,
                    self.penalty_attribute(): -fibonacci_shift(new_bonus),
                }
            )


class MutateDirection(Enum):
    DOWN = 1
    UP = 2


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
