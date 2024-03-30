import pytest


def test_sub1():
    assert 2 - 2 == 0


@pytest.mark.smoke
def test_sub2():
    assert 2 + 2 != 4


@pytest.mark.skip(reason="Not implemented yet")
def test_sub3():
    assert 2 + 5 != 7
