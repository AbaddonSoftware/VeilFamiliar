from VeilFamiliar import VeilFamiliar
from VeilFamiliarMove import VeilFamiliarMove
from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarType import VeilFamiliarType
from random import choice

# some/all of these probably should be in classes already created.
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

def calculate_damage(attacker: VeilFamiliar, defender: VeilFamiliar) -> int:

    pass


def calculate_order(
    familiar_a: VeilFamiliar, familiar_b: VeilFamiliar
) -> list[VeilFamiliar]:
    upper = 10000
    a = familiar_a.current_move.priority * upper + familiar_a.stats.speed
    b = familiar_b.current_move.priority * upper + familiar_b.stats.speed
    if a != b:
        return [familiar_a, familiar_b] if a > b else [familiar_b, familiar_a]

    return [familiar_a, familiar_b] if choice([True, False]) else [familiar_b, familiar_a]

base_stats = VeilFamiliarStats(
    health=100,
    attack=88,
    defense=77,
    special_attack=92,
    special_defense=93,
    speed=87,
)

base_stats2 = VeilFamiliarStats(
    health=100,
    attack=88,
    defense=77,
    special_attack=92,
    special_defense=93,
    speed=99,
)

# Define the primary type
water_type = VeilFamiliarType(
    type_name="Water",
    weaknesses=["Electric", "Grass"],
    resistances=["Fire", "Water", "Ice", "Steel"],
    immunities=[],
)

fire_type = VeilFamiliarType(
    type_name="Fire",
    weaknesses=["Water", "Rock"],
    resistances=["Fire", "Grass", "Ice", "Bug", "Steel", "Fairy"],
    immunities=[],
)

# Create the moves
water_gun = VeilFamiliarMove(
    name="Water Gun",
    power=40,
    power_points=35,
    accuracy=100,
    priority=0,
    category="Special",
    type="Water",
    description="A powerful water-based attack.",
    status_effects=[],
)

ice_beam = VeilFamiliarMove(
    name="Ice Beam",
    power=90,
    power_points=15,
    accuracy=100,
    priority=2,
    category="Physical",
    type="Ice",
    description="A powerful ice-based attack.",
    status_effects=["paralyzed"],
)

# Create the moveset
moveset = VeilFamiliarMoveset([water_gun, ice_beam])
swift = VeilFamiliarMove(
    name="Swift",
    power=60,
    power_points=20,
    accuracy=100,
    priority=2,
    category="Physical",
    type="Normal",
    description="A swift, fast attack.",
    status_effects=[],
)


# Create the familiar
snozzwanger = VeilFamiliar(
    given_name="Ned",
    species_name="Snozzwanger",
    is_frontline=True,
    is_conscious=True,
    level=10,
    stats=base_stats,
    primary_type=water_type,
    current_move=swift,
    secondary_type=None,
    moveset=moveset,
    description="Predator of the Oompa Loompas",
)

vermicious_knid = VeilFamiliar(
    given_name="Jed",
    species_name="Vermicious Knid",
    is_frontline=True,
    is_conscious=True,
    level=10,
    stats=base_stats2,
    primary_type=water_type,
    current_move=ice_beam,
    secondary_type=fire_type,
    moveset=moveset,
    description="Predator of the Oompa Loompas",
)

output = calculate_order(snozzwanger, vermicious_knid)
print([str(veilfamiliar) for veilfamiliar in output])
print(output)


# TODO: Simulate a battle
# BattleUtils.battle_compare(vermicious_knid)
# BattleUtils.battle_calculate_damage(snozzwanger, chosen_move)
# snozzwanger.take_damage(50)
# print(snozzwanger.base_stats.health)  # Should print 50

