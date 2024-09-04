class VeilFamiliarType:
    def __init__(self, name: str, weaknesses: list, weakness_modifier: float, 
                 strengths: list, strength_modifier: float, immunities: list, 
                 description: str):
        self.name = name
        self.weaknesses = weaknesses  # List of VeilFamiliarType instances
        self.weakness_modifier = weakness_modifier
        self.strengths = strengths  # List of VeilFamiliarType instances
        self.strength_modifier = strength_modifier
        self.immunities = immunities  # List of VeilFamiliarType instances
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_weaknesses(self) -> dict:
        return {'weaknesses': self.weaknesses, 'weakness_modifier': self.weakness_modifier}

    def get_strengths(self) -> dict:
        return {'strengths': self.strengths, 'strength_modifier': self.strength_modifier}

    def get_immunities(self) -> dict:
        return {'immunities': self.immunities}