from genetic_catalyst.attribute import Attribute

class Gene:
    attribute_values: dict[Attribute, int]

    def __init__(self, attribute_values: dict[Attribute, int]):
        self.attribute_values = attribute_values

    def value(self, attribute: Attribute):
        """Returns the value of the bonus or penalty for the given attribute"""
        return self.attribute_values.get(attribute, 0)
