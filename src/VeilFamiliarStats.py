class VeilFamiliarStats:
    def __init__(
        self,
        health: int = 1,
        attack: int = 1,
        special_attack: int = 1,
        defense: int = 1,
        special_defense: int = 1,
        speed: int = 1,
        friendship: int = 1,
        level=1,
    ):
        self.health = health
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.special_defense = special_defense
        self.speed = speed
        self.friendship = friendship
        self.level = level

    def __str__(self):
        return (
            f"VeilFamiliarStats("
            f"Health: {self.health}, "
            f"Attack: {self.attack}, "
            f"Special Attack: {self.special_attack}, "
            f"Defense: {self.defense}, "
            f"Special Defense: {self.special_defense}, "
            f"Speed: {self.speed}, "
            f"Friendship: {self.friendship}, "
            f"Level: {self.level})"
        )
