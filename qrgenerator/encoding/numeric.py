from .encoding import Encoding
from .formatting import numeric

class Numeric(Encoding):
    def __init__(self, number: int, correction: str, version: int = None):
        super().__init__(
            str(number),
            correction,
            version,
            numeric.mode_indicator,
            numeric.capacities,
            numeric.character_count,
            numeric.terminator
        )

    def __repr__(self):
        return f"Numeric(number={self.decoded_string}, error_correction={self.error_correction})"

    def encode(self):
        # TODO - fix encoding to handle one and two zeros in grouping of three numbers.
        encoding = [
            self.decoded_string[_:_+3]
            for _ in range(0, self.character_length + 1, 3)
        ]

        encoded_word = ''.join(list(map(lambda x: bin(int(x))[2:], encoding)))
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word
