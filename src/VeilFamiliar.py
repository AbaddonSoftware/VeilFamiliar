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

    def __str__(self) -> str:
        return f"{self.given_name}, the {self.species_name}"

    @staticmethod
    def _special_round(number):
        if number % 1 > 0.5:
            return int(number + 1)
        return int(number)

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
        damage_values = [4, 2, 1, 0.5, 0.25]
        move = attacker.moveset.selected_move
        types = self.get_types()
        resistant = 0
        weak = 0
        for type in types:
            weak -= type.is_weak(move)
            resistant += type.is_resistant(move)
        return damage_values[(weak + resistant) + 2]

    def calculate_typeboost(self) -> int:
        move = self.moveset.selected_move
        types = self.get_types()
        for type in types:
            if type.is_typeboosted_move(move):
                return 4096 + 2048
        return 4096

    def calculate_base_damage(self, attacker: VeilFamiliar) -> int:
        move_category = attacker.moveset.selected_move.category
        power_of_move = attacker.moveset.selected_move.power
        attacker_level = attacker.stats.level
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
        damage = self._special_round(
            ((2 * attacker_level / 5 + 2) * power_of_move * attack / defense) / 50
        )
        return damage

    def calculate_final_damage(self, random_value: int, attacker: VeilFamiliar) -> int:
        offset32 = 0xFFFFFFFF
        typeboost = attacker.calculate_typeboost()
        effectiveness = self.calculate_effectiveness(attacker)
        base_damage = self.calculate_base_damage(attacker)
        final_damage = int(base_damage * (85 + random_value) / 100) & offset32
        if typeboost != 4096:
            final_damage = (
                int(self._special_round((final_damage * typeboost) / 4096)) & offset32
            )
        final_damage = int(final_damage * effectiveness) & offset32
        return final_damage

    def take_damage(self, damage):
        self.stats.health -= damage
        self.stats.health = max(self.stats.health, 0)
        self.is_conscious = self.stats.health > 0

    def take_status(self, status_effect):
        self.status_effects.append(status_effect)

    def check_status(self):
        # Implement status effect checking logic here
        pass

    # TODO This will need be written to handle a list of VeilFamiliars so as to accomodate more possibilities for combat initiative
    @staticmethod
    def calculate_order(
        familiar_a: VeilFamiliar, familiar_b: VeilFamiliar
    ) -> list[VeilFamiliar]:  # This belongs in BattleArena Code.
        from random import choice

        a = (familiar_a.moveset.selected_move.priority << 15) + familiar_a.stats.speed
        b = (familiar_b.moveset.selected_move.priority << 15) + familiar_b.stats.speed
        if a != b:
            return [familiar_a, familiar_b] if a > b else [familiar_b, familiar_a]
        return (
            [familiar_a, familiar_b]
            if choice([True, False])
            else [familiar_b, familiar_a]
        )
