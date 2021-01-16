import encoding
import formatting.alphanumeric


class Alphanumeric(encoding.Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            formatting.alphanumeric.mode_indicator,
            formatting.alphanumeric.capacities,
            formatting.alphanumeric.character_count,
            formatting.alphanumeric.terminator
        )

    def __repr__(self):
        return f"Alphanumeric(string={self.decoded_string}, error_correction={self.error_correction})"

    def encode(self):
        encoding = list()
        for _ in range(0, self.character_length + 1, 2):
            try:
                encoding.append(
                    bin(
                        (45 * formatting.alphanumeric.alpha_values[
                            self.decoded_string[_]
                        ]) + formatting.alphanumeric.alpha_values[
                            self.decoded_string[_ + 1]
                        ]
                    )[2:].zfill(11)
                )
            except IndexError:
                encoding.append(
                    bin(
                        formatting.alphanumeric.alpha_values[self.decoded_string[_]]
                    )[2:].zfill(6)
                )

        encoded_word = ''.join(encoding)
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word
