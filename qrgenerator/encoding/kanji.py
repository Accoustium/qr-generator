import encoding
import formatting.kanji


class Kanji(encoding.Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            formatting.kanji.mode_indicator,
            formatting.kanji.capacities,
            formatting.kanji.character_count,
            formatting.kanji.terminator
        )

    def __repr__(self):
        return f"Kanji(decoded_string={self.decoded_string}, error_correction={self.error_correction}"

    def encode(self):
        # TODO - Implement Kanji encoding of strings.
        pass
