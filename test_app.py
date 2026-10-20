from app import add
from calc_test_helpers import approx


def test_add():
    assert approx(add(2, 3), 5)
