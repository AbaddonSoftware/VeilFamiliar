from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarType import VeilFamiliarType
from VeilFamiliarMove import VeilFamiliarMove


class VeilFamiliar:
    def __init__(
        self,
        given_name: str,
        species_name: str,
        is_frontline: bool,
        level: int,
        base_stats: VeilFamiliarStats,
        primary_type: VeilFamiliarType,
        secondary_type: VeilFamiliarType,
        moveset: VeilFamiliarMoveset,
        description: str,
        status_list=None,
        egg_group=None,
    ):
        self.given_name = given_name
        self.species_name = species_name
        self.is_frontline = is_frontline
        self.level = level
        self.base_stats = base_stats
        self.primary_type = primary_type
        self.secondary_type = secondary_type
        self.moveset = moveset
        self.description = description
        self.status_list = status_list if status_list is not None else []
        self.egg_group = egg_group if egg_group is not None else []

    def get_given_name(self) -> str:
        return self.given_name

    def get_species_name(self) -> str:
        return self.species_name

    def get_moves(self):
        return self.moveset
    
    def get_all_strengths(self):
        return self.primary_type.get_strengths() + self.secondary_type or self.secondary_type.get_strengths()


    def take_attack(self, attacker):
        strengths = self.get_all_strengths()
        print(strengths)

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
    primary_type = VeilFamiliarType(
        name="Water",
        weaknesses=["Fire", "Grass"],
        weakness_modifier=1.5,
        strengths=["Water", "Ice"],
        strength_modifier=0.5,
        immunities=[],
        description="A type of water-based Pokémon.",
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
    veil_familiar = VeilFamiliar(
        given_name="Ned",
        species_name="LilFyrMan",
        is_frontline=True,
        level=10,
        base_stats=base_stats,
        primary_type=primary_type,
        secondary_type=[],
        moveset=moveset,
        description="A little fireman. His bark is bigger than his bite.",
    )

    veil_familiar.take_attack(veil_familiar)
