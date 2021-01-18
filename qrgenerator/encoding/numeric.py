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
        encoding = [
            self.decoded_string[_:_+3]
            for _ in range(0, self.character_length + 1, 3)
        ]

        encoded_word = ''.join(list(map(self.encoding_number, encoding)))
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word

    def encoding_number(self, number):
        if number.startswith('00') or len(number) == 1:
            return bin(int(number))[2:].zfill(4)
        elif number.startswith('0') or len(number) == 2:
            return bin(int(number))[2:].zfill(7)
        else:
            return bin(int(number))[2:].zfill(10)
