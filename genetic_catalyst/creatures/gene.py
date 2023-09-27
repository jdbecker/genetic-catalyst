import random
from creatures.models import CreatureModel, GeneModel
from creatures.allele import Allele, allele_from_model, base_allele, new_allele


class Gene:
    alleles: tuple[Allele, Allele]

    def __init__(self, allele1: Allele, allele2: Allele):
        alleles = [allele1, allele2]
        if alleles[0].dominant_over(alleles[1]):
            self.alleles = (alleles[0], alleles[1])
        else:
            self.alleles = (alleles[1], alleles[0])

    @classmethod
    def new(cls, allele1: Allele, allele2: Allele) -> "Gene":
        alleles = [allele1, allele2]
        if alleles[0].dominant_over(alleles[1]):
            return Gene(alleles[0], alleles[1])
        else:
            return Gene(alleles[1], alleles[0])

    def __repr__(self) -> str:
        return f"Gene({repr(self.alleles[0])}, {repr(self.alleles[1])})"

    def __str__(self) -> str:
        return f"DOMINANT: ({self.alleles[0]}) | recessive: ({self.alleles[1]})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Gene):
            return NotImplemented
        else:
            return (
                self.alleles[0] == other.alleles[0]
                and self.alleles[1] == other.alleles[1]
            )

    def __hash__(self) -> int:
        return hash((self.alleles[0], self.alleles[1]))

    def save(self, creature: CreatureModel) -> GeneModel:
        gene = GeneModel.objects.create(creature=creature)
        for allele in self.alleles:
            allele.save(gene)
        return gene

    def value(self, attribute: str) -> int:
        """Returns the value of the bonus or penalty for the given attribute"""
        return self.alleles[0].value(attribute)

    def propagate_allele(self) -> Allele:
        """Used by Creature to breed. Calls propagate on a random Allele in order to
        allow the Allele to check for mutation before being copied to the new Gene."""
        return random.choice(self.alleles).propagate()


def base_gene() -> Gene:
    return Gene(base_allele(), base_allele())


def new_gene() -> Gene:
    return Gene(new_allele(), new_allele())


def gene_from_model(model: GeneModel) -> Gene:
    return Gene(*(allele_from_model(allele) for allele in model.alleles))
