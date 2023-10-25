# This function calculates the factorial of a number using recursion.
# The time complexity of this algorithm is O(n!), which means it grows
# factorially with the input size, making it very inefficient for large inputs.

def factorial(n):
    # Base case: If n is 0 or 1, return 1 (0! and 1! are defined as 1).
    if n <= 1:
        return 1
    else:
        # Recursive call: Calculate n! by multiplying n with (n-1)!
        return n * factorial(n - 1)

# Example usage
number = 5  # Calculate 5!

# Calling the function to calculate the factorial
result = factorial(number)

# Printing the result
print(f"{number}! = {result}")
