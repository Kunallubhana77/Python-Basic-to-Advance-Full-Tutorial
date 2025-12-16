# Raise Exception in Python

print("=" * 50)
print("BASIC RAISE STATEMENT")
print("=" * 50)

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    elif age < 18:
        raise ValueError("Must be 18 or older!")
    else:
        print(f"✓ Age {age} is valid")

try:
    check_age(25)   # Valid
except ValueError as e:
    print(f"Error: {e}")

try:
    check_age(-5)   # Invalid
except ValueError as e:
    print(f"✗ Error: {e}")

try:
    check_age(15)   # Invalid
except ValueError as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 50)
print("RAISING DIFFERENT EXCEPTION TYPES")
print("=" * 50)

def validate_email(email):
    if not email:
        raise ValueError("Email cannot be empty")
    if "@" not in email:
        raise ValueError("Email must contain @")
    if not email.endswith(".com"):
        raise TypeError("Email must end with .com")
    print(f"✓ Email '{email}' is valid")

test_emails = ["user@example.com", "", "invalid.com", "user@example.org"]

for email in test_emails:
    try:
        print(f"\nValidating: '{email}'")
        validate_email(email)
    except (ValueError, TypeError) as e:
        print(f"✗ {type(e).__name__}: {e}")

print("\n" + "=" * 50)
print("RE-RAISING EXCEPTIONS")
print("=" * 50)

def risky_operation():
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Caught exception, logging it...")
        raise  # Re-raise the same exception

try:
    risky_operation()
except ZeroDivisionError:
    print("✗ Exception bubbled up and caught here")

print("\n" + "=" * 50)
print("RAISING WITH CUSTOM MESSAGE")
print("=" * 50)

def withdraw(balance, amount):
    if amount > balance:
        raise RuntimeError(f"Insufficient funds! Balance: {balance}, Requested: {amount}")
    return balance - amount

try:
    new_balance = withdraw(1000, 500)
    print(f"✓ Withdrawal successful. New balance: {new_balance}")
except RuntimeError as e:
    print(f"✗ {e}")

try:
    new_balance = withdraw(1000, 1500)
except RuntimeError as e:
    print(f"✗ {e}")

print("\n" + "=" * 50)
print("RAISE FROM (Exception Chaining)")
print("=" * 50)

def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError("Cannot perform division") from e

try:
    result = divide_numbers(10, 0)
except ValueError as e:
    print(f"✗ {type(e).__name__}: {e}")
    print(f"  Original cause: {type(e.__cause__).__name__}")

print("\n" + "=" * 50)
print("RAISE WITHOUT ARGUMENT (Re-raise)")
print("=" * 50)

def process():
    try:
        items = [1, 2, 3]
        print(items[10])  # Will raise IndexError
    except IndexError:
        print("Logging error before re-raising...")
        raise  # Re-raise without argument

try:
    process()
except IndexError as e:
    print(f"✗ Caught re-raised exception: {type(e).__name__}")

print("\n" + "=" * 50)
print("PRACTICAL: INPUT VALIDATION")
print("=" * 50)

def create_user(username, password):
    # Validate username
    if not username:
        raise ValueError("Username cannot be empty")
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters")
    
    # Validate password
    if not password:
        raise ValueError("Password cannot be empty")
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters")
    if not any(c.isdigit() for c in password):
        raise ValueError("Password must contain at least one number")
    
    print(f"✓ User '{username}' created successfully!")

test_users = [
    ("john", "password123"),  # Valid
    ("", "password123"),       # Empty username
    ("ab", "password123"),     # Short username
    ("john", ""),              # Empty password
    ("john", "pass"),          # Short password
    ("john", "password"),      # No number in password
]

for username, password in test_users:
    try:
        print(f"\nCreating user: '{username}'")
        create_user(username, password)
    except ValueError as e:
        print(f"✗ Validation Error: {e}")

print("\n" + "=" * 50)
print("PRACTICAL: DIVISION WITH VALIDATION")
print("=" * 50)

def safe_divide(a, b):
    if not isinstance(a, (int, float)):
        raise TypeError(f"First argument must be a number, not {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"Second argument must be a number, not {type(b).__name__}")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    
    result = a / b
    print(f"✓ {a} / {b} = {result}")
    return result

test_cases = [
    (10, 2),      # Valid
    (10, 0),      # Zero division
    ("10", 2),    # Invalid type
    (10, "2"),    # Invalid type
]

for a, b in test_cases:
    try:
        print(f"\nDividing {a} by {b}")
        safe_divide(a, b)
    except (TypeError, ZeroDivisionError) as e:
        print(f"✗ {type(e).__name__}: {e}")

print("\n" + "=" * 50)
print("RAISE VS ASSERT")
print("=" * 50)

print("Using raise:")
def check_positive_raise(num):
    if num <= 0:
        raise ValueError("Number must be positive")
    print(f"✓ {num} is positive")

print("Using assert:")
def check_positive_assert(num):
    assert num > 0, "Number must be positive"
    print(f"✓ {num} is positive")

try:
    check_positive_raise(-5)
except ValueError as e:
    print(f"  Raise caught: {e}")

try:
    check_positive_assert(-5)
except AssertionError as e:
    print(f"  Assert caught: {e}")
