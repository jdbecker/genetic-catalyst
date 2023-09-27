"""Module containing the Allele class and supporting functions"""
from enum import Enum
import random
from creatures.models import AlleleModel, GeneModel
from creatures.attribute import Attribute, attribute_from_model
from copy import deepcopy

from creatures.utils import fibonacci_shift

MUTATION_CHANCE = 0.1


class Allele:
    """Each gene is made up of a pair of Alleles, one dominant, and one recessive.
    Recessive alleles have no affect on the creature's attributes, but when the
    creature breeds, each gene passes on one random allele to the offspring, so
    recessive genes can reappear in successive generations."""

    attributes: set[Attribute]

    def __init__(self, attributes: set[Attribute]):
        self.attributes = attributes

    def __repr__(self) -> str:
        return (
            f"Allele({sorted(self.attributes, key=lambda attribute: attribute.name)})"
        )

    def __str__(self) -> str:
        return str.join(
            ", ",
            [f"{attribute.name}: {attribute.value}" for attribute in self.attributes],
        )

    def __eq__(self, other) -> bool:
        if not isinstance(other, Allele):
            return NotImplemented
        else:
            return self.attributes == other.attributes

    def __hash__(self) -> int:
        return hash((self.attributes))

    def save(self, gene: GeneModel) -> AlleleModel:
        allele = AlleleModel.objects.create(gene=gene)
        for attribute in self.attributes:
            attribute.save(allele)
        return allele

    def value(self, attribute_name: str) -> int:
        """The cumulative value of all attributes with the given name on this allele"""
        return sum(
            attribute.value
            for attribute in self.attributes
            if attribute.name == attribute_name
        )

    def bonus(self) -> int:
        """The total positive bonus this allele provides (used in determining dominance)"""
        return sum(
            attribute.value for attribute in self.attributes if attribute.value > 0
        )

    def bonus_attribute(self) -> str:
        """return the name of the attribute with the greatest bonus"""
        return max(self.attributes, key=lambda attribute: attribute.value).name

    def penalty(self) -> int:
        """The total negative penalty this allele provides (used in mutation logic)"""
        return sum(
            attribute.value for attribute in self.attributes if attribute.value < 0
        )

    def penalty_attribute(self) -> str:
        """return the name of the attribute with the greatest penalty"""
        return min(self.attributes, key=lambda attribute: attribute.value).name

    def dominant_over(self, other: "Allele") -> bool:
        """Alleles with bonuses closer to 0 are more dominant"""
        return self.bonus() <= other.bonus()

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
                    Attribute(self.bonus_attribute(), new_bonus),
                    Attribute(self.penalty_attribute(), -fibonacci_shift(new_bonus)),
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
            Attribute("HEALTH", 10),
            Attribute("STRENGTH", 10),
            Attribute("INTELLIGENCE", 10),
            Attribute("CUNNING", 10),
            Attribute("BANDWIDTH", 10),
            Attribute("PERCEPTION", 10),
            Attribute("HARVESTING", 10),
            Attribute("ABSORPTION", 10),
        }
    )


def new_allele() -> Allele:
    """Randomly generate a brand new Allele with a +1 boost to one attribute and a -1
    penalty to another"""
    boosted_attribute, penalized_attribute = random.sample(
        [
            "HEALTH",
            "STRENGTH",
            "INTELLIGENCE",
            "CUNNING",
            "BANDWIDTH",
            "PERCEPTION",
            "HARVESTING",
            "ABSORPTION",
        ],
        2,
    )
    return Allele({Attribute(boosted_attribute, 1), Attribute(penalized_attribute, -1)})


def allele_from_model(model: AlleleModel) -> Allele:
    return Allele({attribute_from_model(attribute) for attribute in model.attributes})
