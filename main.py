# incident-test-app/main.py
# INTENTIONAL BUG: Removed to prevent import error

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 0)
    print(f"Result: {result}")