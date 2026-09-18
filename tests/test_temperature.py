

from app.temperature import fahrenheit_to_celsius, celsius_to_fahrenheit


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32

def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0

def test_celsius_to_fahrenheit_positive():
    assert celsius_to_fahrenheit(100) == 212

def test_fahreinheit_to_celsius_positive():
    assert fahrenheit_to_celsius(212) == 100
