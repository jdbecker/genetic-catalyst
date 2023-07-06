import random
from genetic_catalyst.attribute import Attribute


class Allele:
    attribute_values: dict[Attribute, int]

    def __init__(self, attribute_values: dict[Attribute, int]):
        self.attribute_values = attribute_values

    def __repr__(self) -> str:
        return f"Allele({self.attribute_values})"

    def bonus(self) -> int:
        return sum(i for i in self.attribute_values.values() if i > 0)

    def dominant_over(self, other: "Allele") -> bool:
        return self.bonus() >= other.bonus()


def base_allele() -> Allele:
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
    boosted_attribute, penalized_attribute = random.sample(list(Attribute), 2)
    return Allele({boosted_attribute: 1, penalized_attribute: -1})
