import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.alphanumeric import Alphanumeric
from qrgenerator.encoding.numeric import Numeric
from qrgenerator.encoding.byte import Byte
from qrgenerator.encoding.kanji import Kanji


@pytest.fixture(scope="module")
def alpha_fixture():
    return Alphanumeric("HELLO WORLD", "H")


@pytest.fixture(scope="module")
def numeric_fixture():
    return Numeric(8675309, "H")


@pytest.fixture(scope="module")
def byte_fixture():
    return Byte("Hello, world!", "H")


@pytest.fixture(scope="module")
def kanji_fixture():
    return Kanji("茗荷", "H")


def test_alpha_mode(alpha_fixture):
    assert alpha_fixture.mode_indicator == "0010"


def test_alpha_character_count(alpha_fixture):
    assert alpha_fixture.encoded_character_count() == "000001011"


def test_alpha_word_encoding(alpha_fixture):
    assert (
        alpha_fixture.encode()
        == "0110000101101111000110100010111001011011100010011010100001101"
    )


def test_alpha_string_encoding(alpha_fixture):
    assert (
        str(alpha_fixture)
        == "00100000010110110000101101111000110100010111001011011100010011010100001101000000"
    )


def test_numeric_mode(numeric_fixture):
    assert numeric_fixture.mode_indicator == "0001"


def test_numeric_character_count(numeric_fixture):
    assert numeric_fixture.encoded_character_count() == "0000000111"


def test_numeric_word_encoding(numeric_fixture):
    assert numeric_fixture.encode() == "110110001110000100101001"


def test_numeric_string_encoding(numeric_fixture):
    assert str(numeric_fixture) == "000100000001111101100011100001001010010000000000"


def test_byte_mode(byte_fixture):
    assert byte_fixture.mode_indicator == "0100"


def test_byte_character_count(byte_fixture):
    assert byte_fixture.encoded_character_count() == "00001101"


def test_byte_word_encoding(byte_fixture):
    assert (
        byte_fixture.encode()
        == "01001000011001010110110001101100011011110010110000100000011101110110111101110010011011000110010000100001"
    )


def test_byte_string_encoding(byte_fixture):
    assert (
        str(byte_fixture)
        == "010000001101010010000110010101101100011011000110111100101100001000000111011101101111011100100110110001100100001000010000"
    )


def test_kanji_mode(kanji_fixture):
    assert kanji_fixture.mode_indicator == "1000"


def test_kanji_character_count(kanji_fixture):
    assert kanji_fixture.encoded_character_count() == "00000010"


def test_kanji_word_encoding(kanji_fixture):
    assert kanji_fixture.encode() == "11010101010100011010010111"


def test_kanji_string_encoding(kanji_fixture):
    assert str(kanji_fixture) == "100000000010110101010101000110100101110000000000"
