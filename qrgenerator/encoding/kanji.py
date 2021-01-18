from .encoding import Encoding
from .formatting import kanji


class Kanji(Encoding):
    def __init__(self, decoded_string: str, correction: str, version: int = None):
        super().__init__(
            decoded_string,
            correction,
            version,
            kanji.mode_indicator,
            kanji.capacities,
            kanji.character_count,
            kanji.terminator
        )

    def __repr__(self):
        return (f"Kanji(decoded_string={self.decoded_string},"
                f"error_correction={self.error_correction})")

    def encode(self):
        encoded_string = []
        for _ in self.decoded_string:
            if '0x8140' <= f"0x{_.encode('shift-jis').hex().upper()}" <= '0x9FFC':
                encoded_string.append(self.encoded_kanji(_, '0x8140'))
            elif '0xE040' <= f"0x{_.encode('shift-jis').hex().upper()}" <= '0xEBBF':
                encoded_string.append(self.encoded_kanji(_, '0xC140'))

        return ''.join(encoded_string)

    def encoded_kanji(self, kanji_character: str, base_kanji: hex):
        subtracted_value = hex(
            int(f'0x{kanji_character.encode("shift-jis").hex().upper()}', 16) -
            int(base_kanji, 16)
        )[2:].zfill(4)

        print(subtracted_value)

        return bin(
            (
                int(f'0x{subtracted_value[:2].upper()}', 16) * int('0xC0', 16)
            ) + int(f'0x{subtracted_value[2:].upper()}', 16)
        )[2:].zfill(13)
