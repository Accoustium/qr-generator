import formatting


class Numeric:
    def __init__(self, number: int, correction: str, version: int = None):
        self.number = number
        self.character_length = len(str(number))
        self.error_correction = correction

        if version is None:
            self.version = self._find_version()
        else:
            if self._validate_version(version):
                self.version = version
            else:
                raise ValueError('Version is to low to accommodate size of number.')

        self.encoded_number = ''.join([
            formatting.mode_indicator,
            bin(self.character_length)[2:].zfill(
                formatting.character_count[self.version]
            ),
            self._encode(),
            formatting.terminator
        ])

    def __str__(self):
        return self.encoded_number

    def __repr__(self):
        return f"Numeric({self.number}, {self.error_correction})"

    def _encode(self):
        # TODO - fix encoding to handle one and two zeros in grouping of three numbers.
        encoding = [
            str(self.number)[_:_+3]
            for _ in range(0, self.character_length + 1, 3)
        ]

        encoded_word = ''.join(list(map(lambda x: bin(int(x))[2:], encoding)))
        encoded_word = encoded_word + '0' * (7 - (len(str(encoded_word)) % 8))

        return encoded_word

    def _find_version(self) -> int:
        for k, v in formatting.capacities.items():
            if self.character_length < v[self.error_correction]:
                return k

    def _validate_version(self, version_number: int) -> bool:
        return version_number >= self._find_version()
