from calculator import sum, subtract
import pytest

def test_sum():
    assert sum(2, 3) == 5
    assert sum(-1, -1) == -2
    assert sum(0, 0) == 0

def test_sum_invalid_input():
    with pytest.raises(ValueError):
        sum("a", 2)

@pytest.mark.parametrize("a, b, expected", [(2, 3, -1), (0, 0, 0), (-1, -1, 0)])
def test_subtract(a, b, expected):
    assert subtract(a,b) == expected


def test_subtract_invalid_input():
    with pytest.raises(ValueError):
        subtract("a", 2)

if __name__ == '__main__':
    pass
