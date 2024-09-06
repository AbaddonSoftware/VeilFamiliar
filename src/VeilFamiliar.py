from VeilFamiliarMove import VeilFamiliarMove
from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarType import VeilFamiliarType


class VeilFamiliar:
    def __init__(
        self,
        given_name: str,
        species_name: str,
        level: int,
        base_stats: VeilFamiliarStats,
        primary_type: VeilFamiliarType,
        secondary_type: VeilFamiliarType,
        moveset: VeilFamiliarMoveset,
        is_conscious: bool,
        is_frontline: bool,
        description: str,
        status_list=None,
        egg_group=None,
    ):
        self.given_name = given_name
        self.species_name = species_name
        self.level = level
        self.base_stats = base_stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.moveset = moveset
        self.is_conscious = is_conscious
        self.is_frontline = is_frontline
        self.description = description
        self.status_list = status_list if status_list is not None else []
        self.egg_group = egg_group if egg_group is not None else []

    def get_given_name(self) -> str:
        return self.given_name

    def get_species_name(self) -> str:
        return self.species_name

    def get_moves(self):
        return self.moveset

    def take_damage(self, damage):
        self.base_stats.health -= damage
        self.base_stats.health = max(self.base_stats.health, 0)
        self.is_conscious = self.base_stats.health > 0

    def take_status(self, status_list):
        self.status_list.extend(status_list)

    def report_status(self) -> str:
        pass

    def increase_level(self) -> None:
        self.level += 1  # We will also include a check for if a new power was learned with level if this is correct practice.


if __name__ == "__main__":

    base_stats = VeilFamiliarStats(
        health=100,
        attack=88,
        defense=77,
        special_attack=92,
        special_defense=93,
        speed=87,
    )

    # Define the primary type
    water_type = VeilFamiliarType(
        type_name="Water",
        weaknesses=["Electric", "Grass"],
        resistances=["Fire", "Water", "Ice", "Steel"],
        immunities=[],
    )

    fire_type = VeilFamiliarType(
        type_name="Fire",
        weaknesses=["Water", "Rock"],
        resistances=["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"],
        immunities=[],
    )

    # Create the moves
    water_gun = VeilFamiliarMove(
        name="Water Gun",
        power=40,
        power_points=35,
        accuracy=100,
        priority=0,
        category="Special",
        type="Water",
        description="A powerful water-based attack.",
        status_effects=[],
    )

    ice_beam = VeilFamiliarMove(
        name="Ice Beam",
        power=90,
        power_points=15,
        accuracy=100,
        priority=2,
        category="Physical",
        type="Ice",
        description="A powerful ice-based attack.",
        status_effects=["paralyzed"],
    )

    # Create the moveset
    moveset = VeilFamiliarMoveset([water_gun, ice_beam])

    # Create the familiar
    snozzwanger = VeilFamiliar(
        given_name="Ned",
        species_name="Snozzwanger",
        is_frontline=True,
        level=10,
        base_stats=base_stats,
        primary_type=water_type,
        secondary_type=VeilFamiliarType(),
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )

    vermicious_knid = VeilFamiliar(
        given_name="Jed",
        species_name="Vermicious Knid",
        is_frontline=True,
        level=10,
        base_stats=base_stats,
        primary_type=water_type,
        secondary_type=fire_type,
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )

    # TODO: Simulate a battle
