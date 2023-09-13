import random
from src.allele import Allele, base_allele, new_allele
from src.attribute import Attribute


class Gene:
    alleles: tuple[Allele, Allele]

    def __init__(self, allele1: Allele, allele2: Allele):
        alleles = [allele1, allele2]
        random.shuffle(alleles)
        if alleles[0].dominant_over(alleles[1]):
            self.alleles = (alleles[0], alleles[1])
        else:
            self.alleles = (alleles[1], alleles[0])

    def __repr__(self) -> str:
        return f"Gene({repr(self.alleles[0])}, {repr(self.alleles[1])})"

    def __str__(self) -> str:
        return f"DOMINANT: ({self.alleles[0]}) | recessive: ({self.alleles[1]})"

    def value(self, attribute: Attribute):
        """Returns the value of the bonus or penalty for the given attribute"""
        return self.alleles[0].attribute_values.get(attribute, 0)

    def propagate_allele(self) -> Allele:
        """Used by Creature to breed. Calls propagate on a random Allele in order to
        allow the Allele to check for mutation before being copied to the new Gene."""
        return random.choice(self.alleles).propagate()


def base_gene() -> Gene:
    return Gene(base_allele(), base_allele())


def new_gene() -> Gene:
    return Gene(new_allele(), new_allele())
