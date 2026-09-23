import pytest
from lern_python import add, sub, mul, div
def test_add():
    assert add(4, 3) == 7

def test_sub():
    assert sub(10, 4) == 6
def test_mul():
    assert mul(2, 6) == 12
def test_div():
    assert div(10, 2) == 5.0
def test_div_zero():
    with pytest.raises(ValueError):
        div(10, 0)
