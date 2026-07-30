import gddtd 

# incident-test-app/main.py
# INTENTIONAL BUG: missing_module import will fail
# Removed non-existent module imports to prevent ModuleNotFoundError

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")