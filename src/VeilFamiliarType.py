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
    
    def get_all(self) -> dict:
        return {
            "weaknesses": self.weaknesses,
            "resistances": self.resistances,
            "immunities": self.immunities,
        }
    
class VeilFamiliarMoveTypeCompare:
    #TODO: Consider making this comparison case insensitive

    @staticmethod
    def battle_compare(
        defender: VeilFamiliarType, move_type: str
    ) -> float:
        effectiveness = defender.get_all()
        if move_type in effectiveness["immunities"]:
            return 0
        damage_mod = 1
        if move_type in effectiveness["weaknesses"]:
            return 2 * damage_mod
        if move_type in effectiveness["resistances"]:
            return 0.5 * damage_mod
        return 1 * damage_mod
    
    @staticmethod
    def get_typeboost(attacker: VeilFamiliarType, move_type: str) -> float:
            if attacker.get_type_name() == move_type:
                return 1.5
            return 1


if __name__ == "__main__":
    # Test the battle_compare method
    defender = VeilFamiliarType(
        type_name="Fire",
        weaknesses=["Water", "Rock"],
        resistances=["Fire", "Ice"],
        immunities=["Dragon"],
    )
    attacker = VeilFamiliarType(
        type_name="Water",
        weaknesses=["Electric", "Grass"],
        resistances=["Fire", "Water"],
        immunities=["Dragon"],
    )

    result = VeilFamiliarMoveTypeCompare.battle_compare(defender, attacker, "Water")
    print(result)  # Should output 2, since Water is a weakness for Fire type
    temp = defender
    defender = attacker
    attacker = temp
    result = VeilFamiliarMoveTypeCompare.battle_compare(defender, attacker, "Dragon")
    print(result)  # Should output 2, since Water is a weakness for Fire type