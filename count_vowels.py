def count_vowels(text):
    """Returns the number of vowels in the input string, case insensitive."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
