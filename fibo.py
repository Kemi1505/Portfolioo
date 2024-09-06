# Function to generate Fibonacci sequence
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

# Input: Number of terms in the sequence
num_terms = int(input("Enter the number of terms: "))

# Generate and display the Fibonacci sequence
if num_terms <= 0:
    print("Please enter a positive integer.")
elif num_terms == 1:
    print("Fibonacci sequence: [0]")
else:
    fib_sequence = fibonacci(num_terms)
    print(f"Fibonacci sequence (first {num_terms} terms): {fib_sequence}")
