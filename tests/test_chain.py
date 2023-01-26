from worse_itertools import chain


def test_abcdef():
    c = chain("ABC", "DEF")
    assert ''.join(s for s in c) == "ABCDEF"


def test_abcdefghi():
    c = chain("ABC", "DEF", "GHI")
    assert ''.join(s for s in c) == "ABCDEFGHI"
