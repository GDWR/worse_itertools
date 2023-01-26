from worse_itertools import count


def test_default():
    c = count()

    for i in range(10):
        assert next(c) == i


def test_start_at_10():
    c = count(start=10)

    for i in range(10):
        assert next(c) == 10 + i


def test_start_at_0_step_of_5():
    c = count(step=5)

    for i in range(10):
        assert next(c) == i * 5


def test_start_at_05_step_of_075():
    c = count(start=0.5, step=0.75)

    for i in range(10):
        assert next(c) == 0.5 + (0.75 * i)
