from .formatting.correction import *
from .polynomial import Message, Generator


class ErrorCorrection:
    def __init__(self, encoding: str, version: int, correction_level: str):
        self.required_bits = self.__find_required_bits_number(correction_level, version)
        self.padded_encoding = self.__pad_string(encoding)

    def __find_required_bits_number(
        self, correction_level: str, version_number: int
    ) -> int:
        numbers = correction_table[f"{version_number}-{correction_level}"]

        return (numbers.blocks_group_1 + numbers.dc_group_1) + (numbers.blocks_group_2 + numbers.dc_group_2)

    def __pad_string(self, encoded_string: str) -> str:
        if len(encoded_string) == self.required_bits:
            return encoded_string

        padding_bits: float = (self.required_bits - len(encoded_string)) / 2 + 1
        padded_string: str = "".join([encoded_string, filler * padding_bits])
        return padded_string[: self.required_bits]
