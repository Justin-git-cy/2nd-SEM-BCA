def factorial(n):
    """Computes factorial using recursion."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
