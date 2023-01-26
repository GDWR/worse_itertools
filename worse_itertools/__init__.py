import operator
from typing import Iterable, TypeVar, Iterator, Tuple, Optional

T = TypeVar('T')


def count(start: float = 0, step: float = 1) -> Iterator[float]:
    while True:
        yield start
        start += step


def cycle(iterable: Iterable[T], /) -> Iterator[T]:
    l = iterable

    while True:
        l, r = tee(l)
        yield from r


def tee(iterable: Iterable[T], n: int = 2, /) -> Tuple[Iterator[T], ...]:
    if n < 0:
        raise ValueError("number of tees must be >= 0")

    iterable = iter(iterable)
    consumed = []

    def consumer() -> Iterable[T]:
        p = 0

        while True:
            if p == len(consumed):
                try:
                    consumed.append(next(iterable))
                except StopIteration:
                    return

            yield consumed[p]
            p += 1

    return tuple(iter(consumer()) for _ in range(n))


def repeat(o: object, times: Optional[int] = None):
    if times is None:
        while True:
            yield o
    else:
        for i in range(times):
            yield o


def accumulate(iterable: Iterable[T], func=operator.add, *, initial=None):
    iterable = iter(iterable)

    total = initial

    if total is None:
        total = next(iterable)

    yield total

    for v in iterable:
        total = func(total, v)
        yield total


def chain(*iterables: Iterable):
    for i in iterables:
        yield from i
