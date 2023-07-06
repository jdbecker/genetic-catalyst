from tabulate import tabulate
from genetic_catalyst.attribute import Attribute
from genetic_catalyst.gene import Gene, base_gene, new_gene


class Creature:
    """The Creature is the basic unit of gameplay. Each has a list of Genes from
    which the Creature's Attribute values are derived and each Gene gives a
    bonus to one Attribute and a penalty to another."""

    genes: tuple[Gene, ...]

    def __init__(self, *genes: Gene):
        self.genes = genes

    def __repr__(self) -> str:
        return f"Creature({str.join(', ', [str(gene) for gene in self.genes])})"

    def __str__(self) -> str:
        table = tabulate(
            [
                [
                    "Health",
                    "Strength",
                    "Intelligence",
                    "Cunning",
                    "Bandwidth",
                    "Perception",
                    "Harvesting",
                    "Absorption",
                ],
                [
                    self.health,
                    self.strength,
                    self.intelligence,
                    self.cunning,
                    self.bandwidth,
                    self.perception,
                    self.harvesting,
                    self.absorption,
                ],
            ]
        )
        return str(table)

    @property
    def health(self):
        return sum(gene.value(Attribute.HEALTH) for gene in self.genes)

    @property
    def strength(self):
        return sum(gene.value(Attribute.STRENGTH) for gene in self.genes)

    @property
    def intelligence(self):
        return sum(gene.value(Attribute.INTELLIGENCE) for gene in self.genes)

    @property
    def cunning(self):
        return sum(gene.value(Attribute.CUNNING) for gene in self.genes)

    @property
    def bandwidth(self):
        return sum(gene.value(Attribute.BANDWIDTH) for gene in self.genes)

    @property
    def perception(self):
        return sum(gene.value(Attribute.PERCEPTION) for gene in self.genes)

    @property
    def harvesting(self):
        return sum(gene.value(Attribute.HARVESTING) for gene in self.genes)

    @property
    def absorption(self):
        return sum(gene.value(Attribute.ABSORPTION) for gene in self.genes)

    def breed(self, other: "Creature") -> "Creature":
        return Creature(*(Gene(genes[0].random_allele(), genes[1].random_allele()) for genes in zip(self.genes, other.genes)))


def new_creature() -> Creature:
    return Creature(base_gene(), *(new_gene() for _ in range(7)))
