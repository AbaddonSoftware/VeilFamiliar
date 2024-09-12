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

    def get_type_name(self) -> str:
        return self.type_name

    def get_effectiveness(self) -> dict:
        return {
            "weaknesses": self.weaknesses,
            "resistances": self.resistances,
            "immunities": self.immunities,
        }
    
    def __str__(self):
        return self.type_name

    def __add__(self, other):
        if isinstance(other, VeilFamiliarType):
            return VeilFamiliarType(
                type_name=f"{self.type_name} {other.type_name}",
                weaknesses=self.weaknesses + other.weaknesses,
                resistances=self.resistances + other.resistances,
                immunities=self.immunities + other.immunities,
            )
        else:
            raise TypeError(
                "Unsupported operand type(s) for +: 'VeilFamiliarType' and '{}'".format(
                    type(other).__name__
                )
            )
