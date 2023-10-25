def fibonacci(n):
    # Create a list to store Fibonacci numbers
    fib = [0] * (n + 1)

    # Base cases
    fib[0] = 0
    fib[1] = 1

    # Calculate Fibonacci numbers from 2 to n
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Example usage
n = 10
result = fibonacci(n)
print(f"The {n}-th Fibonacci number is: {result}")
