from .encoding import Encoding
from .formatting import alphanumeric


class Alphanumeric(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            alphanumeric.mode_indicator,
            alphanumeric.capacities,
            alphanumeric.character_count,
            alphanumeric.terminator,
        )

    def __repr__(self):
        return f"Alphanumeric(string={self.decoded_string}, error_correction={self.error_correction})"

    def encode(self):
        encoding = list()
        for _ in range(0, self.character_length + 1, 2):
            try:
                encoding.append(
                    bin(
                        (45 * alphanumeric.alpha_values[self.decoded_string[_]])
                        + alphanumeric.alpha_values[self.decoded_string[_ + 1]]
                    )[2:].zfill(11)
                )
            except IndexError:
                encoding.append(
                    bin(alphanumeric.alpha_values[self.decoded_string[_]])[2:].zfill(6)
                )

        encoded_word = "".join(encoding)
        encoded_word = encoded_word

        return encoded_word
