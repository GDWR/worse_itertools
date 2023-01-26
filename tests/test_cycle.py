from worse_itertools import cycle


def test_1_2_3():
    c = cycle([1, 2, 3])

    for _ in range(3):
        for i in range(1, 4):
            assert next(c) == i


def test_range_10():
    c = cycle(range(10))

    for _ in range(3):
        for i in range(10):
            assert next(c) == i
