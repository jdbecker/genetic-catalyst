import random
from genetic_catalyst.allele import Allele, base_allele, new_allele
from genetic_catalyst.attribute import Attribute


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

    def value(self, attribute: Attribute):
        """Returns the value of the bonus or penalty for the given attribute"""
        return self.alleles[0].attribute_values.get(attribute, 0)

    def random_allele(self) -> Allele:
        return random.choice(self.alleles)


def base_gene() -> Gene:
    return Gene(base_allele(), base_allele())


def new_gene() -> Gene:
    return Gene(new_allele(), new_allele())
