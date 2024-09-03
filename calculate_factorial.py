def calculate_factorial(n):
    """Returns the factorial of a non-negative integer n."""
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
