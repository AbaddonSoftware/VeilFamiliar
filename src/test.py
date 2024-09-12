
from random import randint

from VeilFamiliar import VeilFamiliar
from VeilFamiliarStats import VeilFamiliarStats
from VeilFamiliarMoveset import VeilFamiliarMoveset
from VeilFamiliarStatusEffect import VeilFamiliarStatusEffect
from VeilFamiliarType import VeilFamiliarType
from VeilFamiliarMove import VeilFamiliarMove



def main():
    base_stats = VeilFamiliarStats(
        health=100,
        attack=88,
        defense=77,
        special_attack=92,
        special_defense=93,
        speed=80 + randint(0, 45),
    )

    base_stats2 = VeilFamiliarStats(
        health=100,
        attack=88,
        defense=77,
        special_attack=92,
        special_defense=93,
        speed=80 + randint(0, 45),
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

    moveset = VeilFamiliarMoveset([water_gun, ice_beam, swift], selected_move=water_gun)

    # Create the familiar
    snozzwanger = VeilFamiliar(
        given_name="Ned",
        species_name="Snozzwanger",
        is_conscious=True,
        level=10,
        stats=base_stats,
        primary_type=water_type,
        secondary_type=None,
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )

    vermicious_knid = VeilFamiliar(
        given_name="Jed",
        species_name="Vermicious Knid",
        is_conscious=True,
        level=10,
        stats=base_stats2,
        primary_type=water_type,
        secondary_type=fire_type,
        moveset=moveset,
        description="Predator of the Oompa Loompas",
    )
    output = VeilFamiliar.calculate_order(snozzwanger, vermicious_knid)
    print(base_stats2, base_stats, sep="\n")
    print([str(veilfamiliar) for veilfamiliar in output])
    print(snozzwanger.given_name, snozzwanger.get_types(), snozzwanger.moveset.selected_move.type, snozzwanger.get_typeboost())
    print(vermicious_knid.get_typeboost())
    print(vermicious_knid.battle_compare(snozzwanger))
    print(snozzwanger.battle_compare(vermicious_knid))

if __name__ == '__main__':
    main()
