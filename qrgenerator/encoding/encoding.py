class Encoding:
    def __init__(
        self,
        decoded_string: str,
        error_correction: str,
        version: int = None,
        mode_indicator: str = None,
        capacities: dict = None,
        character_count: dict = None,
        terminator: str = None,
    ):
        self.decoded_string = decoded_string
        self.character_length = len(decoded_string)
        self.mode_indicator = mode_indicator
        self.capacities = capacities
        self.character_count = character_count
        self.terminator = terminator

        if error_correction in ["L", "M", "Q", "H"]:
            self.error_correction = error_correction
        else:
            raise ValueError("Error correction value not valid.")

        if version:
            if self.validate_version(version):
                self.version = version
            else:
                raise ValueError("Version input is not high enough for decoded string.")
        else:
            self.version = self.find_version()

    def __str__(self):
        encoding = "".join(
            [
                self.mode_indicator,
                self.encoded_character_count(),
                self.encode(),
                self.terminator,
            ]
        )

        return encoding + "0" * (8 - (len(str(encoding)) % 8))

    def __repr__(self):
        return f"Encoding(string={self.decoded_string}, correction={self.error_correction})"

    def encoded_character_count(self) -> str:
        return bin(self.character_length)[2:].zfill(self.character_count[self.version])

    def encode(self) -> str:
        raise NotImplementedError("This function has not been implemented yet.")

    def find_version(self) -> int:
        for k, v in self.capacities.items():
            if self.character_length < v[self.error_correction]:
                return k

    def validate_version(self, version_number: int) -> bool:
        return version_number >= self.find_version()
