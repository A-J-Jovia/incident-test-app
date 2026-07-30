# incident-test-app/main.py
import missing_module  # This module does not exist -> ImportError

def compute(a, b):
    return a / b

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")
