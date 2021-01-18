from .formatting


class ErrorCorrection:
    def __init__(self, encoding: str, version: int, correction_level: str):
        self.required_bits = self._find_required_bits_number(correction_level, version)
        self.padded_encoding = self._pad_string(encoding)

    def _find_required_bits_number(
        self, correction_level: str, version_number: int
    ) -> int:
        numbers = formatting.correction_table[f"{version_number}-{correction_level}"]

        group_1_block = int(numbers[1])
        group_1_codeword = int(numbers[2])
        group_2_block = numbers[3] if numbers[3] != "" else 0
        group_2_codeword = numbers[4] if numbers[4] != "" else 0

        return (group_1_codeword * group_1_block) + (group_2_codeword * group_2_block)

    def _pad_string(self, encoded_string: str) -> str:
        if len(encoded_string) == self.required_bits:
            return encoded_string

        padding_bits = (self.required_bits - len(encoded_string)) / 2 + 1
        padded_string = "".join([encoded_string, formatting.filler * padding_bits])
        return padded_string[: self.required_bits]
