import math

# incident-test-app/main.py
def compute(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b 

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")