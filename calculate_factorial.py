def calculate_factorial(n):
    result = 1
    # Calculate factorial of n
    for i in range(1, n + 1):
        result *= i
    return result
# Example 
if __name__ == "__main__":
    n = 4
    print(f"The factorial of {n} is {calculate_factorial(n)}")
