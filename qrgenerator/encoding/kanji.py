from .encoding import Encoding
from .formatting import kanji

class Kanji(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            kanji.mode_indicator,
            kanji.capacities,
            kanji.character_count,
            kanji.terminator
        )

    def __repr__(self):
        return f"Kanji(decoded_string={self.decoded_string}, error_correction={self.error_correction}"

    def encode(self):
        # TODO - Implement Kanji encoding of strings.
        pass
