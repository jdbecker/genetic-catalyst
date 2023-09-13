from enum import Enum


class Attribute(Enum):
    """These are the names for the different types of Attributes a Creature can
    have"""

    HEALTH = 0
    STRENGTH = 1
    INTELLIGENCE = 2
    CUNNING = 3
    BANDWIDTH = 4
    PERCEPTION = 5
    HARVESTING = 6
    ABSORPTION = 7

    def __repr__(self) -> str:
        return f"Attribute.{self.name}"

    def __str__(self) -> str:
        return self.name[0] + self.name[1:].lower()
