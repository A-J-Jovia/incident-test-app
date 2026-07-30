import importlib

# incident-test-app/main.py
# INTENTIONAL BUG: missing_module import will fail
try:
    importlib.import_module('missing_module')
except ImportError:
    pass

def compute(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b 

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")