# test_main.py

import pytest
from main import Calculator, Greeter, factorial, is_prime, fibonacci

# def test_calculator_add():
#     calc = Calculator()
#     assert calc.add(2, 3) == 5
#     assert calc.add(-1, 1) == 0
#     assert calc.add(0, 0) == 0

# def test_calculator_subtract():
#     calc = Calculator()
#     assert calc.subtract(10, 5) == 5
#     assert calc.subtract(0, 0) == 0
#     assert calc.subtract(-1, -1) == 0

# def test_calculator_multiply():
#     calc = Calculator()
#     assert calc.multiply(4, 5) == 20
#     assert calc.multiply(0, 1) == 0
#     assert calc.multiply(-1, -1) == 1

# def test_calculator_divide():
#     calc = Calculator()
#     assert calc.divide(20, 4) == 5
#     assert calc.divide(1, 2) == 0.5
#     with pytest.raises(ValueError):
#         calc.divide(10, 0)

# def test_greeter():
#     greeter = Greeter("Alice")
#     assert greeter.greet() == "Hello, Alice!"
#     assert greeter.farewell() == "Goodbye, Alice!"

# def test_greeter_empty_name():
#     greeter = Greeter("")
#     assert greeter.greet() == "Hello, !"
#     assert greeter.farewell() == "Goodbye, !"

# def test_factorial():
#     assert factorial(5) == 120
#     assert factorial(0) == 1
#     assert factorial(1) == 1
#     assert factorial(3) == 6
#     with pytest.raises(ValueError):
#         factorial(-1)

def test_is_prime():
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(9) # 3*3

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_main():
    import main
    # Calculator
    calc = main.Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(10, 5) == 5
    assert calc.multiply(4, 5) == 20
    assert calc.divide(20, 4) == 5

    # Greeter
    greeter = main.Greeter("Alice")
    assert greeter.greet() == "Hello, Alice!"
    assert greeter.farewell() == "Goodbye, Alice!"

    # Factorial
    assert main.factorial(5) == 120

    # Prime check
    assert main.is_prime(7)
    assert not main.is_prime(4)

    # Fibonacci
    assert main.fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

if __name__ == "__main__":
    pytest.main()
