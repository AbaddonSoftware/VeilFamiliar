from random import randint

from src.VeilFamiliar import VeilFamiliar
from src.VeilFamiliarMove import VeilFamiliarMove
from src.VeilFamiliarMoveset import VeilFamiliarMoveset
from src.VeilFamiliarStats import VeilFamiliarStats
from src.VeilFamiliarType import VeilFamiliarType
from src.myTypes.EssenceTypes import EssenceType


def main():
    base_stats = VeilFamiliarStats(
        health=290,
        attack=177,
        defense=216,
        special_attack=279,
        special_defense=250,
        speed=123,
        level=91,
    )

    base_stats2 = VeilFamiliarStats(
        health=429,
        attack=180,
        defense=189,
        special_attack=119,
        special_defense=128,
        speed=163,
        level=87,
    )

    water_type = VeilFamiliarType(
        type_name=EssenceType.WATER,
        weaknesses=[EssenceType.ELECTRIC, EssenceType.GRASS],
        resistances=[
            EssenceType.FIRE,
            EssenceType.WATER,
            EssenceType.ICE,
            EssenceType.STEEL,
        ],
        immunities=[],
    )

    grass_type = VeilFamiliarType(
        type_name=EssenceType.ELECTRIC,
        weaknesses=[
            EssenceType.FIRE,
            EssenceType.FLYING,
            EssenceType.POISON,
            EssenceType.BUG,
        ],
        resistances=[
            EssenceType.WATER,
            EssenceType.ELECTRIC,
            EssenceType.GRASS,
            EssenceType.GROUND,
        ],
        immunities=[],
    )

    normal_type = VeilFamiliarType(
        type_name=EssenceType.NORMAL,
        weaknesses=[EssenceType.FIGHTING],
        resistances=[],
        immunities=[],
    )

    fire_type = VeilFamiliarType(
        type_name=EssenceType.FIRE,
        weaknesses=[EssenceType.WATER, EssenceType.ROCK],
        resistances=[
            EssenceType.FIRE,
            EssenceType.GRASS,
            EssenceType.ICE,
            EssenceType.BUG,
            EssenceType.STEEL,
            EssenceType.FAIRY,
        ],
        immunities=[],
    )

    # Create the moves

    energy_ball = VeilFamiliarMove(
        name="energy_ball",
        power=90,
        power_points=10,
        accuracy=100,
        priority=0,
        category="Special",
        type_name=EssenceType.ELECTRIC,
        description="A powerful water-based attack.",
        status_effects=[],
    )

    water_gun = VeilFamiliarMove(
        name="Water Gun",
        power=40,
        power_points=35,
        accuracy=100,
        priority=0,
        category="Special",
        type_name=EssenceType.WATER,
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
        type_name=EssenceType.ICE,
        description="A powerful ice-based attack.",
        status_effects=["paralyzed"],
    )

    # Create the moveset
    swift = VeilFamiliarMove(
        name="Swift",
        power=60,
        power_points=20,
        accuracy=100,
        priority=2,
        category="Physical",
        type_name=EssenceType.NORMAL,
        description="A swift, fast attack.",
        status_effects=[],
    )

    moveset = VeilFamiliarMoveset(
        [water_gun, ice_beam, swift], selected_move=energy_ball
    )

    # Create the familiar
    snozzwanger = VeilFamiliar(
        given_name="Ned",
        species_name="Snozzwanger",
        stats=base_stats2,
        primary_type=water_type,
        secondary_type=None,
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )

    vermicious_knid = VeilFamiliar(
        given_name="Jed",
        species_name="Vermicious Knid",
        stats=base_stats,
        primary_type=grass_type,
        secondary_type=normal_type,
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )

    vermicious_knid.moveset.selected_move = energy_ball
    snozzwanger.moveset.selected_move = energy_ball
    output = VeilFamiliar.calculate_order(snozzwanger, vermicious_knid)
    print(base_stats2, base_stats, sep="\n")
    print([str(veilfamiliar) for veilfamiliar in output])
    print(
        snozzwanger.given_name,
        [str(type) for type in snozzwanger.get_types()],
        snozzwanger.moveset.selected_move.type_name,
        snozzwanger.calculate_typeboost(),
    )
    type_boost_value = vermicious_knid.calculate_typeboost()
    effectiveness = snozzwanger.calculate_effectiveness(vermicious_knid)
    print(type_boost_value, effectiveness)
    print(snozzwanger.calculate_base_damage(vermicious_knid))
if __name__ == "__main__":
    main()
