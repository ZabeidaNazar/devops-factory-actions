import pytest
from myapp.app import add, substruct, divide

def test_add():
    assert add(2, 3) == 5

def test_substruct():
    assert substruct(5, 3) == 2

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (9, 3, pytest.approx(3)),
        (9, 5, pytest.approx(1.8)),
        (9, 6, pytest.approx(1.5)),
        (9, 7, pytest.approx(1.285714286)),
        (0, 7, pytest.approx(0)),
    ]
)
def test_divide(a, b, expected):
    assert divide(a, b) == expected

def test_divide_0():
    with pytest.raises(ZeroDivisionError):
        divide(9, 0)
