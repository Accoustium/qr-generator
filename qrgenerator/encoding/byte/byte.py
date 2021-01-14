import formatting


class Byte:
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
        return f"Byte({self.decoded_string}, {self.error_correction})"

    def _encode(self):
        encoding = [
            _.encode('utf-8').hex()
            for _ in self.decoded_string
        ]

        return ''.join(map(lambda x: bin(int(x, 16))[2:].zfill(8), encoding))

    def _find_version(self) -> int:
        for k, v in formatting.capacities.items():
            if self.character_length < v[self.error_correction]:
                return k

    def _validate_version(self, version_number: int) -> bool:
        return version_number >= self._find_version()
