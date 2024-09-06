class VeilFamiliarStatusEffects:
    def __init__(
        self, status_effect_name: str, inflicted_status: str, status_probability: int, status_time: int
    ):
        self.status_effect_name = status_effect_name
        self.inflicted_status = inflicted_status
        self.status_probability = status_probability
        self.status_time = status_time

    def get_status_effect_name(self) -> str:
        return self.status_effect_name

    def get_inflicted_status(self) -> str:
        return self.inflicted_status

    def get_status_probability(self) -> int:
        return self.status_probability
