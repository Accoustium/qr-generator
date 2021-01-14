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
                formatting.character_count[self.character_length]
            ),
            self._encode(),
            formatting.terminator
        ])

    def __str__(self):
        return f"Numeric({self.number}, {self.error_correction})"

    def __repr__(self):
        return f"Numeric({self.number}, {self.error_correction})"

    def _encode(self):
        encoding = [
            str(self.number)[_:_+3]
            for _ in range(0, self.character_length + 1, 3)
        ]

        return ''.join(list(map(
            lambda x: bin(int(x))[2:],
            encoding
        )))

    def _find_version(self) -> int:
        for k, v in formatting.capacities.items():
            if self.character_length < v[self.error_correction]:
                return k

    def _validate_version(self, version_number: int) -> bool:
        return version_number >= self._find_version()
