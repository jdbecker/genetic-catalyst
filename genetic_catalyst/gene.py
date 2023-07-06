from genetic_catalyst.allele import Allele, base_allele
from genetic_catalyst.attribute import Attribute


class Gene:
    alleles: tuple[Allele, Allele]

    def __init__(self, allele1: Allele, allele2: Allele):
        if allele1.dominant_over(allele2):
            self.alleles = (allele1, allele2)
        else:
            self.alleles = (allele2, allele1)

    def __repr__(self) -> str:
        return f"Gene({repr(self.alleles[0])}, {repr(self.alleles[1])})"

    def value(self, attribute: Attribute):
        """Returns the value of the bonus or penalty for the given attribute"""
        return self.alleles[0].attribute_values.get(attribute, 0)


def base_gene() -> Gene:
    return Gene(base_allele(), base_allele())
