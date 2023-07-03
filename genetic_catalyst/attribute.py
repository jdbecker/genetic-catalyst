from enum import Enum

class Attribute(Enum):
    """These are the names for the different types of Attributes a Creature can 
    have"""
    HEALTH = "Health"
    STRENGTH = "Strength"
    INTELLIGENCE = "Intelligence"
    CUNNING = "Cunning"
    BANDWIDTH = "Bandwidth"
    PERCEPTION = "Perception"
    HARVESTING = "Harvesting"
    ABSORPTION = "Absorption"
