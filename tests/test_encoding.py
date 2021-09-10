import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.encoding import Encoding


@pytest.fixture(scope="module")
def passing_encoding():
    return Encoding("This is a test", "L", version=1, capacities={1: {"L": 999}})


@pytest.mark.xfail(raises=ValueError)
def test_failing_encode():
    en = Encoding("This is a Test", "X")


@pytest.mark.xfail(raises=NotImplementedError)
def test_failing_version_encode():
    en = Encoding(
        "This is a Test and it needs to be crazy long so it will want to say its a higher version",
        "H",
        version=1,
    )


@pytest.mark.xfail(raises=NotImplementedError)
def test_failing_encoding_encode(passing_encoding):
    value = passing_encoding.encode()
