import non_existent_webhook_test_module

import missing_module_for_ci_test

# incident-test-app/main.py
def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")