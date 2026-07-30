import non_existent_webhook_test_module
import absolutely_broken_module_test
import missing_module_for_ci_test
import final_check_module_v2

# incident-test-app/main.py
# INTENTIONAL BUG: missing_module import will fail
import missing_module  # This module does not exist -> ImportError

def compute(a, b):
    return a / b  # Also: ZeroDivisionError if b=0

if __name__ == '__main__':
    result = compute(10, 2)
    print(f"Result: {result}")
