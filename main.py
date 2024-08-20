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

def generate_password(length=12):
#     """
#     Generate a random password of given length
#     """
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

class Greeter:
    def __init__(self, name):
        if name is None:
            raise ValueError("Name cannot be None")
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

# # New functions added without test cases

def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index)
    weight: in kilograms
    height: in meters
    """
    if height <= 0:
        raise ValueError("Height must be greater than zero")
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def generate_password(length=12):
#     """
#     Generate a random password of given length
#     """
    import random
    import string
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# New functions added without test cases(2)

# def celsius_to_fahrenheit(celsius):
#     """
#     Convert Celsius to Fahrenheit
#     """
#     return (celsius * 9/5) + 32

# def count_vowels(string):
#     """
#     Count the number of vowels in a string
#     """
#     vowels = 'aeiouAEIOU'
#     return sum(1 for char in string if char in vowels)

# def is_palindrome(s):
#     """
#     Check if a string is a palindrome
#     """
#     s = ''.join(char.lower() for char in s if char.isalnum())
#     return s == s[::-1]