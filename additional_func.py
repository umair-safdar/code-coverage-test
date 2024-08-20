def reverse_string(s):
    """
    Reverse a given string
    """
    return s[::-1]

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    # Compare the cleaned string with its reverse
    return cleaned == cleaned[::-1]

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit
    """
    return (celsius * 9/5) + 32
##
def count_vowels(string):
    """
    Count the number of vowels in a string
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in string if char in vowels)