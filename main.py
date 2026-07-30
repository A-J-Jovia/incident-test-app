import wrng 

# incident-test-app/main.py
# INTENTIONAL BUG: missing_module import will fail
import missing_module  # This module does not exist -> ImportError

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")