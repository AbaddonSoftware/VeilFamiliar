

class VeilFamiliarType:
    def __init__(
        self,
        type_name: str = "",
        weaknesses: list = [],
        resistances: list = [],
        immunities: list = [],
    ):
        self.type_name = type_name
        self.weaknesses = weaknesses
        self.resistances = resistances
        self.immunities = immunities


    def get_all(self) -> dict:
        return {
            "weaknesses": self.weaknesses,
            "resistances": self.resistances,
            "immunities": self.immunities,
        }

class VeilFamiliarMoveTypeCompare:

    @staticmethod
    def battle_compare(defender: VeilFamiliarType, attacker: VeilFamiliarType, move_type: str):
        pass