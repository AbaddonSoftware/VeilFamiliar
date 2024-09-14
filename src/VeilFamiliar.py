from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .VeilFamiliarMoveset import VeilFamiliarMoveset
    from .VeilFamiliarStats import VeilFamiliarStats
    from .VeilFamiliarStatusEffects import VeilFamiliarStatusEffects
    from .VeilFamiliarType import VeilFamiliarType


class VeilFamiliar:
    def __init__(
        self,
        given_name: str,
        species_name: str,
        stats: VeilFamiliarStats,
        primary_type: VeilFamiliarType,
        secondary_type: VeilFamiliarType,
        moveset: VeilFamiliarMoveset,
        is_conscious: bool = True,
        description: str = "A mysterious creature from across the veil.",
        status_effects: VeilFamiliarStatusEffects = None,
        egg_group: list = None,
    ):
        self.given_name = given_name
        self.species_name = species_name
        self.stats = stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.moveset = moveset
        self.is_conscious = is_conscious
        self.description = description
        self.status_effects = status_effects
        self.egg_group = egg_group if egg_group is not None else []

    def get_moveset(self):
        return self.moveset

    def take_damage(self, damage):
        self.stats.health -= damage
        self.stats.health = max(self.stats.health, 0)
        self.is_conscious = self.stats.health > 0

    def take_status(self, status_effect):
        self.status_effects.append(status_effect)

    def check_status(self):
        # Implement status effect checking logic here
        pass

    def get_types(self):
        return filter(None, (self.primary_type, self.secondary_type))

    def calculate_effectiveness(self, attacker: VeilFamiliar) -> float:
        damage_values = [4, 2, 1, .5, .25]
        move = attacker.moveset.selected_move
        types = self.get_types()
        resistant = 0
        weak = 0
        for type in types:
            weak -= type.is_weak(move)
            resistant += type.is_resistant(move)
        return damage_values[(weak + resistant) + 2]

    def get_typeboost(self) -> float:
        move = self.moveset.selected_move
        types = self.get_types()
        for type in types:
            if type.is_typeboosted_move(move):
                return 1.5
        return 1

    def calculate_damage(self, attacker: VeilFamiliar) -> int:
        move_category = attacker.moveset.selected_move.category
        power_of_move = attacker.moveset.selected_move.power
        attacker_level = attacker.stats.level
        effectiveness_modifier = self.calculate_effectiveness(attacker)
        typeboost_modifier = attacker.get_typeboost()
        defense = (
            self.stats.special_defense
            if move_category == "Special"
            else self.stats.defense
        )
        attack = (
            attacker.stats.special_attack
            if move_category == "Special"
            else attacker.stats.attack
        )
        print(self.given_name, self.stats, "\n", attacker.given_name, attacker.stats, "\n", move_category, power_of_move, attacker_level)
        print(self.calculate_effectiveness(attacker))
        print(attacker.get_typeboost())
        return int(
            (
                (((2 * attacker_level / 5 + 2) * attack * power_of_move / defense)
                / 50)
                + 2
            )
            * typeboost_modifier
            * effectiveness_modifier
        )

    @staticmethod
    def calculate_order(
        familiar_a: VeilFamiliar, familiar_b: VeilFamiliar
    ) -> list[VeilFamiliar]:  # This belongs in BattleArena Code.
        from random import choice

        upper = 10000
        a = familiar_a.moveset.selected_move.priority * upper + familiar_a.stats.speed
        b = familiar_b.moveset.selected_move.priority * upper + familiar_b.stats.speed
        if a != b:
            return [familiar_a, familiar_b] if a > b else [familiar_b, familiar_a]
        return (
            [familiar_a, familiar_b]
            if choice([True, False])
            else [familiar_b, familiar_a]
        )

    def __str__(self) -> str:
        return f"{self.given_name}, the {self.species_name}"
