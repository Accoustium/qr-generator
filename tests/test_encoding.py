import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.alphanumeric import Alphanumeric


@pytest.fixture(scope="module")
def alpha_fixture():
    return Alphanumeric("HELLO WORLD", "H")


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
