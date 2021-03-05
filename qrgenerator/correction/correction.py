from .formatting.correction import *
from .polynomial import Message, Generator


class ErrorCorrection:
    def __init__(self, encoding: str, version: int, correction_level: str):
        self.required_bits: int = self.__find_required_bits_number(correction_level, version)
        self.padded_encoding: str = self.__pad_string(encoding)
        self.error_encoding: str = self.__create_error_words(correction_level, version)
        self.word_blocks: list[str] = self.__create_blocks(self.padded_encoding, correction_level, version)
        self.error_blocks: list[str] = self.__create_blocks(self.error_encoding, correction_level, version)

    def __find_required_bits_number(
        self, correction_level: str, version_number: int
    ) -> int:
        numbers = correction_table[f"{version_number}-{correction_level}"]

        return numbers.ec_codewords * 8

    def __pad_string(self, encoded_string: str) -> str:
        if len(encoded_string) == self.required_bits:
            return encoded_string

        padding_bits: float = (self.required_bits - len(encoded_string)) / 2 + 1
        padded_string: str = "".join([encoded_string, filler * int(padding_bits)])
        return padded_string[: self.required_bits]

    def __create_error_words(self, correction_level: str, version_number: int) -> str:
        numbers = correction_table[f"{version_number}-{correction_level}"]
        message = Message(self.padded_encoding)
        generator = Generator(numbers.ec_codewords)

        code_words = message / generator

        return code_words.bin()

    def __create_blocks(self, encoding: str, correction_level: str, version_number: int) -> list[str]:
        numbers = correction_table[f"{version_number}-{correction_level}"]
        blocks = list()

        for block1 in range(numbers.blocks_group_1):
            start = block1 * numbers.dc_group_1 * 8
            blocks.append(encoding[start: start + (numbers.dc_group_1 * 8)])

        for block2 in range(numbers.blocks_group_2):
            start = ((numbers.blocks_group_1 * numbers.dc_group_1) + (block2 * numbers.dc_group_2)) * 8
            blocks.append(encoding[start: start + (numbers.dc_group_2 * 8)])

        return blocks
