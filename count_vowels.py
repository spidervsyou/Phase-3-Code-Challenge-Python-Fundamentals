def count_vowels(text):
    vowels = 'aeiou'
    count = 0
    # Count vowels in the text (ignore case)
    for char in text.lower():
        if char in vowels:
            count += 1
    return count

# Example 
if __name__ == "__main__":
    text = "Programming"
    print(f"The number of vowels in '{text}' is {count_vowels(text)}")
