import random
from genetic_catalyst.attribute import Attribute


class Allele:
    attributeValues: dict[Attribute, int]

    def __init__(self, attribute_values: dict[Attribute, int]):
        self.attribute_values = attribute_values

    def bonus(self) -> int:
        return sum(i for i in self.attribute_values.values() if i > 0)

    def dominant_over(self, other: "Allele") -> bool:
        return self.bonus() >= other.bonus()


class BaseAllele(Allele):
    def __init__(self):
        super().__init__(
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
        )
