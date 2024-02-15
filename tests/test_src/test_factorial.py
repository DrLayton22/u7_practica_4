import pytest

from src.factorial import FactorialCalculator


def test_factorial_of_1_is_1():
    calculator = FactorialCalculator()
    assert calculator.factorial(1) == 1


def test_factorial_raises_type_error_for_non_integer_input():
    calculator = FactorialCalculator()
    with pytest.raises(TypeError):
        calculator.factorial("abc")


def test_factorial_raises_value_error_for_negative_input():
    calculator = FactorialCalculator()
    with pytest.raises(ValueError):
        calculator.factorial(-5)


def test_factorial_of_5_is_120():
    calculator = FactorialCalculator()
    assert calculator.factorial(5) == 120
