import encoding
import formatting.byte


class Byte(encoding.Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            formatting.byte.mode_indicator,
            formatting.byte.capacities,
            formatting.byte.character_count,
            formatting.byte.terminator
        )

    def __repr__(self):
        return f"Byte(string={self.decoded_string}, error_correction={self.error_correction})"

    def encode(self):
        encoding = [
            _.encode('utf-8').hex()
            for _ in self.decoded_string
        ]

        encoded_word = ''.join(map(lambda x: bin(int(x, 16))[2:].zfill(8), encoding))
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word
