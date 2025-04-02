def calculator(a, b, operation):
    """Performs basic arithmetic operations."""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else 'Cannot divide by zero'
    else:
        return 'Invalid operation'
