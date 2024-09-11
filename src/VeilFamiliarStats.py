class VeilFamiliarStats:
    def __init__(
        self,
        health: int = 100,
        attack: int = 100,
        special_attack: int = 100,
        defense: int = 100,
        special_defense: int = 100,
        speed: int = 100,
        friendship: int = 100,
    ):
        self.health = health
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.special_defense = special_defense
        self.speed = speed
        self.friendship = friendship

    def __repr__(self) -> str:
        return f"(health={self.health}, attack={self.attack}, special_attack={self.special_attack}, defense={self.defense}, special_defense={self.special_defense}, speed={self.speed}, friendship={self.friendship})"
