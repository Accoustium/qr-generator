import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.numeric import Numeric


@pytest.fixture(scope="module")
def numeric_fixture():
    return Numeric(8675309, "H")


def test_numeric_mode(numeric_fixture):
    assert numeric_fixture.mode_indicator == "0001"


def test_numeric_character_count(numeric_fixture):
    assert numeric_fixture.encoded_character_count() == "0000000111"


def test_numeric_word_encoding(numeric_fixture):
    assert numeric_fixture.encode() == "110110001110000100101001"


def test_numeric_repr(numeric_fixture):
    assert repr(numeric_fixture) == 'Numeric(number=8675309, error_correction=H)'


def test_numeric_string_encoding(numeric_fixture):
    assert str(numeric_fixture) == "000100000001111101100011100001001010010000000000"


def test_encoding_for_number_2():
    en = Numeric(76, 'L')
    assert str(en) == '00010000000010100110000000000000'


@pytest.mark.xfail(raises=ValueError)
def test_numeric_fail_version_too_low():
    num = Numeric(12345698751321658978531489, 'H', version=1)
