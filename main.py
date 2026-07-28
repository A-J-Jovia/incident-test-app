# incident-test-app/main.py
# Removed INTENTIONAL BUG: missing_module import

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")