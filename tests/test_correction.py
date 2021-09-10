import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.correction.correction import ErrorCorrection
from qrgenerator.correction.galois import Galois
from qrgenerator.correction.term import Term
from qrgenerator.correction.polynomial import Polynomial, Message, Generator



@pytest.fixture(scope='module')
def _galois():
    return Galois()


@pytest.fixture(scope='module')
def term():
    return Term(1, 0)


def test_term(term):
    assert str(term) == '1'
