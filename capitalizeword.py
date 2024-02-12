"""
Write a program that accepts a string as input, capitalizes the first letter of each word in the 
string, and then returns the result string.
Examples: 
"hi" => returns "Hi"
"i love programming" => returns "I Love Programming"
"""

def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    result = " ".join(capitalized_words)
    return result

# Example usage:
input_string = "i love programming"
result_string = capitalize_first_letter(input_string)
print(result_string)
