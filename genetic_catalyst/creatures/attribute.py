from creatures.models import AlleleModel, AttributeModel


class Attribute:
    """These are the name / value pairs for the Attributes a Creature can have"""

    name: str
    value: int

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        return f'Attribute("{self.name}", {self.value})'

    def __str__(self) -> str:
        return self.name[0] + self.name[1:].lower()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Attribute):
            return NotImplemented
        else:
            return self.name == other.name and self.value == other.value

    def __hash__(self) -> int:
        return hash((self.name, self.value))

    def save(self, allele: AlleleModel) -> AttributeModel:
        return AttributeModel.objects.create(
            allele=allele, name=self.name, value=self.value
        )


def attribute_from_model(model: AttributeModel) -> Attribute:
    return Attribute(model.name, model.value)
