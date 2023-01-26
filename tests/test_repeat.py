import pytest

from worse_itertools import repeat


def test_infinite():
    r = repeat("infinite")

    for _ in range(100):
        assert next(r) == "infinite"


@pytest.mark.parametrize("times", [-1, 0, 1, 5, 10, 50, 100, 1000])
def test_specified_times(times: int):
    r = repeat("object", times)

    for _ in range(times):
        assert next(r) == "object"

    with pytest.raises(StopIteration):
        next(r)
