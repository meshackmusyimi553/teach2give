"""
Write a program that takes an integer as input and returns true if the input is a power of two.
Examples:
8 => returns true
6 => returns false
"""

def is_power_of_two(n):
    # Check if the number is positive and has only one '1' bit in its binary representation
    return n > 0 and (n & (n - 1)) == 0

# Test cases
print(is_power_of_two(8))  # Should return True
print(is_power_of_two(6))  # Should return False
