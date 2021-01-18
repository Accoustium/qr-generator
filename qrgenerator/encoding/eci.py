from .encoding import Encoding
from .formatting import eci


class ECI(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            formatting.eci.mode_indicator,
            formatting.eci.character_count,
            formatting.eci.capacities,
            formatting.eci.terminator,
        )

    def __repr__(self):
        return f"ECI(decoded_string={self.decoded_string}, error_correction={self.error_correction}"

    def encode(self):
        pass
