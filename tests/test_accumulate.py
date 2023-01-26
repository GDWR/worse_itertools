import operator

from worse_itertools import accumulate


def test_sum():
    assert list(accumulate([1, 2, 3, 4, 5])) == [1, 3, 6, 10, 15]


def test_inital():
    assert list(accumulate([1, 2, 3, 4, 5], initial=100)) == [100, 101, 103, 106, 110, 115]


def test_func():
    assert list(accumulate([1, 2, 3, 4, 5], operator.mul)) == [1, 2, 6, 24, 120]
