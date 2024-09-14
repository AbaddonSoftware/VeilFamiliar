from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .VeilFamiliarStatusEffect import VeilFamiliarStatusEffect

class VeilFamiliarStatusEffects:
    def __init__(self, status_effects: list[VeilFamiliarStatusEffect]):
        self.status_effects = status_effects
