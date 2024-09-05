class VeilFamiliarMove:
    def __init__(self, name: str, power: int, power_points: int, accuracy: int, 
                 priority: int, category: str, type: str, description: str, 
                 status_effects=None):
        self.name = name
        self.power = power
        self.power_points = power_points
        self.accuracy = accuracy
        self.priority = priority
        self.category = category
        self.type = type
        self.description = description
        self.status_effects = status_effects if status_effects is not None else []

    def get_name(self) -> str:
        return self.name

    def get_power(self) -> int:
        return self.power

    def get_power_points(self) -> int:
        return self.power_points

    def get_accuracy(self) -> int:
        return self.accuracy

    def get_priority(self) -> int:
        return self.priority

    def get_category(self) -> str:
        return self.category

    def get_type(self) -> str:
        return self.type

    def get_description(self) -> str:
        return self.description

    def get_status_effects(self) -> list:
        return self.status_effects
    
class VeiFamiliarMoveUtil:

    @staticmethod
    def calculate_first():
        pass