# incident-test-app/main.py

def compute(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b 

if __name__ == '__main__':
    result = compute(10, 0)
    print(f"Result: {result}")