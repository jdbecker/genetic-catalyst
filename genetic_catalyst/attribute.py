from enum import Enum

class Attribute(Enum):
    """These are the names for the different types of Attributes a Creature can 
    have"""
    HARVESTING = "Harvesting"
    ABSORPTION = "Absorption"
    STRENGTH = "Strength"
    INTELLIGENCE = "Intelligence"
    CUNNING = "Cunning"
    HEALTH = "Health"
    PERCEPTION = "Perception"
    BANDWIDTH = "Bandwidth"
