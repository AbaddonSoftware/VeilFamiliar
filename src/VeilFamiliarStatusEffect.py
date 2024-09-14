class VeilFamiliarStatusEffect:
    def __init__(
        self,
        status_effect_name: str,
        status_probability: int,
        is_volatile: bool,
        status_time: int,
    ):
        self._status_effect_name = status_effect_name
        self._status_probability = status_probability
        self._is_volatile = is_volatile
        self._status_time = status_time

    def get_status_effect_name(self) -> str:
        return self._status_effect_name

    def get_status_probability(self) -> int:
        return self._status_probability

    def get_status_time(self) -> int:
        return self._status_time
