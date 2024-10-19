from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .VeilFamiliarStatusEffects import VeilFamiliarStatusEffects
    from .myTypes.EssenceTypes import EssenceType


class VeilFamiliarMove:
    def __init__(
        self,
        name: str,
        power: int,
        power_points: int,
        accuracy: int,
        priority: int,
        category: str,
        type_name: EssenceType,
        description: str,
        status_effects: VeilFamiliarStatusEffects,
    ):
        self.name = name
        self.power = power
        self.power_points = power_points
        self.accuracy = accuracy
        self.priority = priority
        self.category = category
        self.type_name = type_name
        self.description = description
        self.status_effects = status_effects

    def __str__(self):
        return self.name
