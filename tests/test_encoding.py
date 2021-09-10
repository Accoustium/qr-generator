import os
import sys
import pytest

dir_path = os.path.dirname(__file__)
sys.path.append(os.path.join(dir_path, ".."))
from qrgenerator.encoding.encoding import Encoding


@pytest.fixture(scope='module')
def encode():
    pass


