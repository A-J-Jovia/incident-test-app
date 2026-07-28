# incident-test-app/main.py

def compute(a, b):
    # Check for division by zero to avoid ZeroDivisionError
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

if __name__ == '__main__':
    try:
        result = compute(10, 2)  # Example with valid division
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")