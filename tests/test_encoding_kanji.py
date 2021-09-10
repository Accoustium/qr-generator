import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.kanji import Kanji


@pytest.fixture(scope="module")
def kanji_fixture():
    return Kanji("茗荷", "H")


def test_kanji_mode(kanji_fixture):
    assert kanji_fixture.mode_indicator == "1000"


def test_kanji_character_count(kanji_fixture):
    assert kanji_fixture.encoded_character_count() == "00000010"


def test_kanji_word_encoding(kanji_fixture):
    assert kanji_fixture.encode() == "11010101010100011010010111"


def test_kanji_repr(kanji_fixture):
    assert repr(kanji_fixture) == 'Kanji(decoded_string=茗荷,error_correction=H)'


def test_kanji_string_encoding(kanji_fixture):
    assert str(kanji_fixture) == "100000000010110101010101000110100101110000000000"


def test_kanji_version_match():
    kj = Kanji("茗荷", "H", version=1)
    assert kj.version == 1
