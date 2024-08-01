# main.py

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"

    def farewell(self):
        return f"Goodbye, {self.name}!"


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def fibonacci(n):
    if n <= 0:
        raise ValueError("Fibonacci sequence is not defined for non-positive integers")
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        for i in range(2, n):
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


if __name__ == "__main__":
    # Calculator
    calc = Calculator()
    print(calc.add(2, 3))
    print(calc.subtract(10, 5))
    print(calc.multiply(4, 5))
    print(calc.divide(20, 4))

    # Greeter
    greeter = Greeter("Alice")
    print(greeter.greet())
    print(greeter.farewell())

    # Factorial
    print(factorial(5))

    # Prime check
    print(is_prime(7))
    print(is_prime(4))

    # Fibonacci
    print(fibonacci(10))
