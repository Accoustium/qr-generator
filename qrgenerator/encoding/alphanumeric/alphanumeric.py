import formatting


class Alphanumeric:
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        self.decoded_string = decoded_string
        self.character_length = len(decoded_string)
        self.error_correction = correction

        if version is None:
            self.version = self._find_version()
        else:
            if self._validate_version(version):
                self.version = version
            else:
                raise ValueError('Version is to low to accommodate size of string.')

        self.encoded_string = ''.join([
            formatting.mode_indicator,
            bin(self.character_length)[2:].zfill(
                formatting.character_count[self.version]
            ),
            self._encode(),
            formatting.terminator
        ])

    def __str__(self):
        return self.encoded_string

    def __repr__(self):
        return f"Alphanumeric({self.decoded_string}, {self.error_correction})"

    def _encode(self):
        encoding = []
        for _ in range(0, self.character_length + 1, 2):
            try:
                encoding.append(
                    bin(
                        (45 * formatting.alpha_values[
                            self.decoded_string[_]
                        ]) + formatting.alpha_values[
                            self.decoded_string[_ + 1]
                        ]
                    )[2:].zfill(11)
                )
            except IndexError:
                encoding.append(
                    bin(
                        formatting.alpha_values[self.decoded_string[_]]
                    )[2:].zfill(6)
                )

        encoded_word = ''.join(encoding)
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word

    def _find_version(self) -> int:
        for k, v in formatting.capacities.items():
            if self.character_length < v[self.error_correction]:
                return k

    def _validate_version(self, version_number: int) -> bool:
        return version_number >= self._find_version()
