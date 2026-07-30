import zzz_fresh_test_case

# incident-test-app/main.py
# INTENTIONAL BUG: missing_module import will fail
import missing_module_for_ci_test
import absolutely_broken_module_test

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")