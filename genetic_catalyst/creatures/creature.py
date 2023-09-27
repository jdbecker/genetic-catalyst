from tabulate import tabulate
from creatures.models import CreatureModel
from creatures.gene import Gene, base_gene, gene_from_model, new_gene


class Creature:
    """The Creature is the basic unit of gameplay. Each has a list of Genes from
    which the Creature's Attribute values are derived and each Gene gives a
    bonus to one Attribute and a penalty to another."""

    genes: tuple[Gene, ...]

    def __init__(self, *genes: Gene):
        self.genes = genes

    def __repr__(self) -> str:
        return f"Creature({str.join(', ', [repr(gene) for gene in self.genes])})"

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

    def __eq__(self, other) -> bool:
        if not isinstance(other, Creature):
            return NotImplemented
        else:
            return self.genes == other.genes

    def __hash__(self) -> int:
        return hash((self.genes))

    def save(self) -> CreatureModel:
        creature = CreatureModel.objects.create()
        for gene in self.genes:
            gene.save(creature)
        return creature

    def inspect(self) -> str:
        return "INSPECTING CREATURE:\n" + str.join(
            "\n", [str(gene) for gene in self.genes]
        )

    @property
    def health(self):
        return sum(gene.value("HEALTH") for gene in self.genes)

    @property
    def strength(self):
        return sum(gene.value("STRENGTH") for gene in self.genes)

    @property
    def intelligence(self):
        return sum(gene.value("INTELLIGENCE") for gene in self.genes)

    @property
    def cunning(self):
        return sum(gene.value("CUNNING") for gene in self.genes)

    @property
    def bandwidth(self):
        return sum(gene.value("BANDWIDTH") for gene in self.genes)

    @property
    def perception(self):
        return sum(gene.value("PERCEPTION") for gene in self.genes)

    @property
    def harvesting(self):
        return sum(gene.value("HARVESTING") for gene in self.genes)

    @property
    def absorption(self):
        return sum(gene.value("ABSORPTION") for gene in self.genes)

    def breed(self, other: "Creature") -> "Creature":
        return Creature(
            *(
                Gene.new(genes[0].propagate_allele(), genes[1].propagate_allele())
                for genes in zip(self.genes, other.genes)
            )
        )


def new_creature() -> Creature:
    return Creature(base_gene(), *(new_gene() for _ in range(8)))


def creature_from_model(model: CreatureModel) -> Creature:
    return Creature(*(gene_from_model(gene) for gene in model.genes))
