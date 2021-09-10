from .encoding import Encoding
from .formatting import byte


class Byte(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            byte.mode_indicator,
            byte.capacities,
            byte.character_count,
            byte.terminator,
        )

    def __repr__(self):
        return f'Byte(string="{self.decoded_string}", error_correction={self.error_correction})'

    def encode(self):
        encoding = [_.encode("utf-8").hex() for _ in self.decoded_string]

        encoded_word = "".join(map(lambda x: bin(int(x, 16))[2:].zfill(8), encoding))

        return encoded_word
