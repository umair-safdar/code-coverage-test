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