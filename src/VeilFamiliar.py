from random import choice

from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarStatusEffect import VeilFamiliarStatusEffect
from VeilFamiliarType import VeilFamiliarType
class VeilFamiliar:
    def __init__(
        self,
        given_name: str,
        species_name: str,
        level: int,
        stats: "VeilFamiliarStats",
        primary_type: "VeilFamiliarType",
        secondary_type: "VeilFamiliarType",
        moveset: "VeilFamiliarMoveset",
        is_conscious: bool,
        description: str,
        status_list: list["VeilFamiliarStatusEffect"] = None,
        egg_group: list = None,
    ):
        self.given_name = given_name
        self.species_name = species_name
        self.level = level
        self.stats = stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.moveset = moveset
        self.is_conscious = is_conscious
        self.description = description
        self.status_list = status_list if status_list is not None else []
        self.egg_group = egg_group if egg_group is not None else []

    def get_moveset(self):
        return self.moveset

    def take_damage(self, damage):
        self.stats.health -= damage
        self.stats.health = max(self.stats.health, 0)
        self.is_conscious = self.stats.health > 0

    def take_status(self, status_effect):
        self.status_list.append(status_effect)

    def check_status(self):
        # Implement status effect checking logic here
        pass

    def get_types(self):
        return [str(self.primary_type), str(self.secondary_type)]

    def increase_level(self) -> None:
        self.level += 1
        # Include logic for learning new moves or evolving if needed

    def battle_compare(self, attacker: "VeilFamiliar") -> float:
        move_type = attacker.moveset.selected_move.type
        if self.secondary_type:
            effectiveness = (
                self.primary_type + self.secondary_type
            ).get_effectiveness()
        else:
            effectiveness = self.primary_type.get_effectiveness()

        damage_modifier = {
            0: effectiveness["immunities"],
            2: effectiveness["weaknesses"],
            0.5: effectiveness["resistances"],
        }

        for modifier, types in damage_modifier.items():
            if move_type in types:
                return modifier ** types.count(move_type)

        return 1

    def get_typeboost(self) -> float:
        move_type = self.moveset.selected_move.type
        if self.secondary_type:
            is_typeboosted = (
                self.primary_type.type_name == move_type or
                self.secondary_type.type_name == move_type
            )
        else:
            is_typeboosted = self.primary_type.type_name == move_type

        return 1.5 if is_typeboosted else 1

    def calculate_damage(self, attacker: "VeilFamiliar") -> int:
        pass

    @staticmethod
    def calculate_order(familiar_a: "VeilFamiliar", familiar_b: "VeilFamiliar") -> list["VeilFamiliar"]: # This belongs in BattleArena Code.
        upper = 10000
        a = familiar_a.moveset.selected_move.priority * upper + familiar_a.stats.speed
        b = familiar_b.moveset.selected_move.priority * upper + familiar_b.stats.speed
        if a != b:
            return [familiar_a, familiar_b] if a > b else [familiar_b, familiar_a]

        return (
            [familiar_a, familiar_b] if choice([True, False]) else [familiar_b, familiar_a]
        )

    def __str__(self) -> str:
        return f"{self.given_name} the {self.species_name}"

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}(given_name='{self.given_name}', "
                f"species_name='{self.species_name}', level={self.level}, "
                f"stats={self.stats}, primary_type={self.primary_type}, "
                f"secondary_type={self.secondary_type}, moveset={self.moveset}, "
                f"is_conscious={self.is_conscious}, description='{self.description}', "
                f"status_list={self.status_list}, egg_group={self.egg_group})"
                f"egg_group={self.egg_group})")