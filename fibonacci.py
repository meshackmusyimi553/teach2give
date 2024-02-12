"""
Write a program to generate the Fibonacci sequence up to 100.
"""

def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]
    
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    return fibonacci_sequence

# Set the limit for the Fibonacci sequence
limit = 100

# Generate and print the Fibonacci sequence up to the specified limit
fibonacci_sequence = generate_fibonacci(limit)
print(f"Fibonacci sequence up to {limit}: {fibonacci_sequence}")
