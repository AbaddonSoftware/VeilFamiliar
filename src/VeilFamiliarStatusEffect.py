class VeilFamiliarStatusEffect:
    def __init__(
        self,
        status_effect_name: str,
        inflicted_status: str,
        status_probability: int,
        status_time: int,
    ):
        self._status_effect_name = status_effect_name
        self._inflicted_status = inflicted_status
        self._status_probability = status_probability
        self._status_time = status_time

    def get_status_effect_name(self) -> str:
        return self._status_effect_name

    def get_inflicted_status(self) -> str:
        return self._inflicted_status

    def get_status_probability(self) -> int:
        return self._status_probability

    def get_status_time(self) -> int:
        return self._status_time

    def decrement_status_time(self):
        self._status_time = max(self._status_time - 1, 0)
