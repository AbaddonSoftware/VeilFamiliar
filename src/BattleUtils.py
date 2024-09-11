from VeilFamiliar import VeilFamiliar
from VeilFamiliarMove import VeilFamiliarMove
from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarType import VeilFamiliarType
from random import randint, choice

# some/all of these probably should be in classes (probably VeilFamiliar for most) already created.
def battle_compare(defender: VeilFamiliar, attacker: VeilFamiliar) -> float:
    effectiveness = (
        defender.get_primary_type() + defender.get_secondary_type()
    ).get_effectiveness()
    move_type = attacker.current_move().get_type()

    damage_modifier = {
        0: effectiveness["immunities"],
        2: effectiveness["weaknesses"],
        0.5: effectiveness["resistances"],
    }

    for damage_modifier, veilfamiliar_types in damage_modifier.items():
        if move_type in veilfamiliar_types:
            return damage_modifier ** veilfamiliar_types.count(move_type)

    return 1


def get_typeboost(attacker: VeilFamiliar) -> float:
    move_type = attacker.current_move.get_type()
    is_typeboosted = (
        attacker.primary_type.type_name == move_type
        or attacker.secondary_type.type_name == move_type
    )
    return 1.5 if is_typeboosted else 1


def calculate_damage(defender: VeilFamiliar, attacker: VeilFamiliar) -> int:

    pass


def calculate_order(
    familiar_a: VeilFamiliar, familiar_b: VeilFamiliar
) -> list[VeilFamiliar]:
    upper = 10000
    a = familiar_a.current_move.priority * upper + familiar_a.stats.speed
    b = familiar_b.current_move.priority * upper + familiar_b.stats.speed
    if a != b:
        return [familiar_a, familiar_b] if a > b else [familiar_b, familiar_a]

    return (
        [familiar_a, familiar_b] if choice([True, False]) else [familiar_b, familiar_a]
    )
