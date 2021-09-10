import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.byte import Byte


@pytest.fixture(scope="module")
def byte_fixture():
    return Byte("Hello, world!", "H")


def test_byte_mode(byte_fixture):
    assert byte_fixture.mode_indicator == "0100"


def test_byte_character_count(byte_fixture):
    assert byte_fixture.encoded_character_count() == "00001101"


def test_byte_word_encoding(byte_fixture):
    assert (
        byte_fixture.encode()
        == "01001000011001010110110001101100011011110010110000100000011101110110111101110010011011000110010000100001"
    )


def test_byte_repr(byte_fixture):
    assert repr(byte_fixture) == 'Byte(string="Hello, world!", error_correction=H)'


def test_byte_string_encoding(byte_fixture):
    assert (
        str(byte_fixture)
        == "010000001101010010000110010101101100011011000110111100101100001000000111011101101111011100100110110001100100001000010000"
    )
