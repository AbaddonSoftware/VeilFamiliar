class VeilFamiliarStats:
    def __init__(
        self,
        health: int, 
        attack: int,
        special_attack: int,
        defense: int,
        special_defense: int,
        speed: int,
    ):
        self.health = health
        self.attack = attack
        self.special_attack = special_attack
        self.defense = defense
        self.special_defense = special_defense
        self.speed = speed
    
    def get_health(self):
        return self.health

    def get_attack(self) -> int:
        return self.attack

    def get_special_attack(self) -> int:
        return self.special_attack

    def get_defense(self) -> int:
        return self.defense

    def get_special_defense(self) -> int:
        return self.special_defense

    def get_speed(self) -> int:
        return self.speed
