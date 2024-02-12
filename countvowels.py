"""
Write a program that counts the number of vowels in a sentence.
eg " Hello World " => returns 2
"""

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1

    return vowel_count

# Example usage:
input_sentence = "Hello World"
result = count_vowels(input_sentence)
print(f"The number of vowels in the sentence '{input_sentence}' is: {result}")
