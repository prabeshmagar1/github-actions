from app.calculator import add, subtract, multiply, divide

def test_add():
    assert add(1,2) == 3


def test_subtract():
    assert subtract(5,3) == 2


def test_multiply():
    assert multiply(4,3) == 12


def test_divide():
    assert divide(100,2) == 50