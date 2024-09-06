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


class VeilFamiliarTypeUtil:
    # TODO: Consider making this comparison case insensitive

    @staticmethod
    def battle_compare(defender: VeilFamiliarType, move_type: str) -> float:
        effectiveness = defender.get_all()
        damage_modifier = {
            0: effectiveness["immunities"],
            2: effectiveness["weaknesses"],
            0.5: effectiveness["resistances"],
        }
        for damage_modifier, veilfamiliar_types in damage_modifier.items():
            print(damage_modifier)
            if move_type in veilfamiliar_types:
                return damage_modifier
        return 1

    @staticmethod
    def get_typeboost(attacker: VeilFamiliarType, move_type: str) -> float:
        is_typeboosted = attacker.get_type_name() == move_type
        return 1.5 if is_typeboosted else 1


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

    result = VeilFamiliarTypeUtil.battle_compare(defender, "Water")
    print(result)
    temp = defender
    defender = attacker
    attacker = temp
    result = VeilFamiliarTypeUtil.battle_compare(defender, "Dragon")
    print(result)
