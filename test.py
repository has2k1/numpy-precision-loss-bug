import numpy as np


def test_negative_power():
    res = 10 ** -1.0
    assert res == 0.1


def test_negative_numpy_power():
    res = 10 ** np.float64(-1.0)
    assert res == 0.1


def test_negative_numpyarray_power():
    res = (10 ** np.array([-1.0]))[0]
    assert res == 0.1


def test_negative_numpy_power_v2():
    res = 10 ** (np.array([-1.0])[0])
    assert res == 0.1
