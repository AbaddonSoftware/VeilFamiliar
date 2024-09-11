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
        is_frontline: bool,
        description: str,
        current_move: "VeilFamiliarMove",
        status_list: list["VeilFamiliarStatusEffect"] = None,  # if these don't persist after battle, this is probably unnecessary
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
        self.is_frontline = is_frontline
        self.description = description
        self.current_move = current_move
        self.status_list = status_list if status_list is not None else []
        self.egg_group = egg_group if egg_group is not None else []

    def get_moveset(self):
        return self.moveset

    def take_damage(self, damage):
        self.stats.health -= damage
        self.stats.health = max(self.base_stats.health, 0)
        self.is_conscious = self.base_stats.health > 0

    def take_status(self, status_effect):
        self.status_list.append(status_effect)

    def check_status(self):
        pass

    def increase_level(self) -> None:
        self.level += (
            1  # We will also include a check if a new move is learned or if "evolve?".
        )

    def __str__(self) -> str:
        return f"{self.given_name} the {self.species_name}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(given_name='{self.given_name}', species_name='{self.species_name}', level={self.level}, stats={self.stats}, primary_type={self.primary_type}, secondary_type={self.secondary_type}, moveset={self.moveset}, is_conscious={self.is_conscious}, is_frontline={self.is_frontline}, description='{self.description}', current_move={self.current_move}, status_list={self.status_list}, egg_group={self.egg_group})"