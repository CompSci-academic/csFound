# This function calculates the nth Fibonacci number using recursion.
# It has an exponential time complexity of O(2^n) because it makes
# multiple recursive calls with exponential growth.
def fibonacci(n):
    # Base case: If n is 0 or 1, return n.
    if n <= 1:
        return n
    # Recursive case: Calculate the (n-1)th and (n-2)th Fibonacci numbers,
    # and then sum them. This leads to multiple recursive calls with
    # exponential growth, resulting in O(2^n) time complexity.
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 5

# Calling the function to calculate the 5th Fibonacci number
result = fibonacci(n)

# Printing the result
print(f"The {n}th Fibonacci number is:", result)
