from worse_itertools import count, tee

import pytest


def test_default():
    l, r = tee(count())

    for _ in range(10):
        v1 = next(l)
        v2 = next(r)
        assert v1 == v2


def test_consume_fully_first():
    l, r = tee(iter('abc'))

    assert ''.join(s for s in l) == ''.join(s for s in r)


def test_negative_amount():
    with pytest.raises(ValueError):
        tee(count(), -1)


def test_zero():
    assert tee(count(), 0) == tuple()


@pytest.mark.parametrize("amount", [1, 5, 10, 50, 100, 1000])
def test_amount(amount: int):
    first, *rest = tee(count(), amount)

    for _ in range(10):
        v = next(first)
        assert all(next(i) == v for i in rest)
