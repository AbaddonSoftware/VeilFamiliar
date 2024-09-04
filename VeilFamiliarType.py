class VeilFamiliarType:
    def __init__(self, name: str, weaknesses: list, weakness_modifier: float, 
                 strengths: list, strength_modifier: float, immunities: list, 
                 description: str):
        self.name = name
        self.weaknesses = weaknesses  
        self.weakness_modifier = weakness_modifier
        self.strengths = strengths  
        self.strength_modifier = strength_modifier
        self.immunities = immunities  
        self.description = description

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_weaknesses(self) -> list:
        return [self.weaknesses]

    def get_strengths(self) -> list:
        return [self.strengths]

    def get_immunities(self) -> dict:
        return [self.immunities]