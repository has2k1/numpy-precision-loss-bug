import math
import numpy as np


def test_pypower():
    res = 10 ** -1.0
    assert res == 0.1


def test_mathpower():
    res = math.pow(10, -1.0)
    assert res == 0.1


def test_nppower():
    res = np.power(10, -1.0)
    assert res == 0.1
