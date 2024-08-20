import pytest
from main import Calculator, Greeter, factorial, is_prime, fibonacci
from additional_func import celsius_to_fahrenheit, count_vowels

def test_calculator_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_calculator_subtract():
    calc = Calculator()
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(0, 0) == 0
    assert calc.subtract(-1, -1) == 0

def test_calculator_multiply():
    calc = Calculator()
    assert calc.multiply(4, 5) == 20
    assert calc.multiply(0, 1) == 0
    assert calc.multiply(-1, -1) == 1

def test_calculator_divide():
    calc = Calculator()
    assert calc.divide(20, 4) == 5
    assert calc.divide(1, 2) == 0.5
    with pytest.raises(ValueError):
        calc.divide(10, 0)

def test_greeter():
    greeter = Greeter("Alice")
    assert greeter.greet() == "Hello, Alice!"
    assert greeter.farewell() == "Goodbye, Alice!"

def test_greeter_empty_name():
    greeter = Greeter("")
    assert greeter.greet() == "Hello, !"
    assert greeter.farewell() == "Goodbye, !"

def test_greeter_edge_cases():
    greeter = Greeter(" ")
    assert greeter.greet() == "Hello,  !"
    assert greeter.farewell() == "Goodbye,  !"

    with pytest.raises(ValueError):
        Greeter(None)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    with pytest.raises(ValueError):
        factorial(-1)

def test_is_prime():
    assert is_prime(7)
    assert not is_prime(4)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(0)
    assert not is_prime(-1)
    assert not is_prime(9)  # 3*3

def test_fibonacci():
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-1)

def test_calculator_edge_cases():
    calc = Calculator()
    assert calc.add(1000000000, 2000000000) == 3000000000
    assert calc.subtract(-1000000000, 2000000000) == -3000000000
    assert calc.multiply(123456789, 987654321) == 123456789 * 987654321
    assert calc.divide(1, 3) == 1 / 3

def test_factorial_edge_cases():
    with pytest.raises(ValueError):
        factorial(-1000)
    assert factorial(10) == 3628800

def test_fibonacci_edge_cases():
    assert fibonacci(3) == [0, 1, 1]
    assert fibonacci(4) == [0, 1, 1, 2]

#from 2nd file
def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(-40) == -40
    assert round(celsius_to_fahrenheit(37), 2) == 98.60

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("The quick brown fox") == 5
    assert count_vowels("") == 0

if __name__ == "__main__":
    pytest.main()