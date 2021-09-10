from .encoding import Encoding
from .formatting import eci


class ECI(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            eci.mode_indicator,
            eci.character_count,
            eci.capacities,
            eci.terminator,
        )

    def __repr__(self):
        return f"ECI(decoded_string={self.decoded_string}, error_correction={self.error_correction}"

    def encode(self):
        pass
