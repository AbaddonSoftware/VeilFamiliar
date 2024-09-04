class VeilFamiliarType:
    def __init__(
        self,
        type_name: str = "",
        weaknesses: list = [],
        strengths: list = [],
        immunities: list = [],
    ):

        self.type_name = type_name
        self.weaknesses = weaknesses
        self.weakness_modifier = 2
        self.strengths = strengths
        self.strength_modifier = 0.5
        self.immunities = immunities
        self.immunities_modifier = 0

    def get_type_name(self) -> str:
        return self.type_name

    def get_weaknesses(self) -> list:
        return [self.weaknesses]

    def get_strengths(self) -> list:
        return [self.strengths]

    def get_immunities(self) -> list:
        return [self.immunities]

    def get_all(self) -> dict:
        return {
            "weaknesses": self.weaknesses,
            "strengths": self.strengths,
            "immunities": self.immunities,
            "weakness_modifier": self.weakness_modifier,
            "strength_modifer": self.strength_modifier,
            "immunities_modifier": self.immunities_modifier,
        }
