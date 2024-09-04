import VeilFamiliarMoveset, VeilFamiliarType, VeilFamiliarStats


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
        self.base_stats = base_stats  # Instance of VeilFamiliarStats
        self.primary_type = primary_type  # Instance of VeilFamiliarType
        self.secondary_type = secondary_type  # Instance of VeilFamiliarType
        self.moveset = moveset  # Instance of VeilFamiliarMoveset
        self.description = description
        self.status_list = status_list if status_list is not None else []
        self.egg_group = egg_group if egg_group is not None else []

    def get_given_name(self) -> str:
        return self.given_name

    def get_species_name(self) -> str:
        return self.species_name

    def get_moves(self):
        return self.moveset

    def take_attack(self, attacker):
        # Logic for taking an attack
        pass

    def report_status(self) -> str:
        # Logic for reporting status
        pass

    def increase_level(self) -> None:
        self.level += 1 # We will also include a check for if a new power was learned with level if this is correct practice.
