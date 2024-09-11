# from VeilFamiliarStatusEffect import VeilFamiliarStatusEffect
from typing import List
class VeilFamiliarMove:
    def __init__(
        self,
        name: str,
        power: int,
        power_points: int,
        accuracy: int,
        priority: int,
        category: str,
        type: str,
        description: str,
        status_effects: list['VeilFamiliarStatusEffect']
    ):
        self.name = name
        self.power = power
        self.power_points = power_points
        self.accuracy = accuracy
        self.priority = priority
        self.category = category
        self.type = type
        self.description = description
        self.status_effects = status_effects
