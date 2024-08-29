class VeilFamiliar:

    def __init__(self, name, health, attack, defense, special_attack, special_defense, speed, current_primary_type, current_secondary_type=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed
        self.current_primary_type = current_primary_type  
        self.current_secondary_type = current_secondary_type  # The secondary type (can be None)

    def take_damage(self, amount, attacker_type): #placeholder. I wish I had played more pokemon before this.
        effectiveness = 1
        final_damage = amount * effectiveness
        self.health -= final_damage

    def use_type_ability(self):
        print(f"{self.name} uses its primary type ability:")
        self.current_primary_type.use_ability()
        
        if self.secondary_type:
            print(f"{self.name} uses its secondary type ability:")
            self.current_secondary_type.use_ability()

    def __str__(self):
        types = f"{self.current_primary_type.type_name}"
        if self.current_secondary_type:
            types += f" / {self.current_secondary_type.type_name}"
        return f"{self.name} ({types} Type) with {self.health} HP"