def factorial(n):
    if n == 0:
        return 1  # Base case: 0! is defined as 1
    else:
        return n * factorial(n - 1)  # Recursive case: n! = n * (n-1)!

# Example usage
n = 5
result = factorial(n)
print(f"The factorial of {n} is {result}")
