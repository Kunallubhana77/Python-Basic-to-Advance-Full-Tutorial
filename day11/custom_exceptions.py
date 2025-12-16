# Custom Exceptions in Python

print("=" * 50)
print("CREATING CUSTOM EXCEPTION")
print("=" * 50)

# Define custom exception
class InvalidAgeError(Exception):
    """Custom exception for invalid age"""
    pass

def set_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative!")
    elif age > 150:
        raise InvalidAgeError("Age seems unrealistic!")
    else:
        print(f"✓ Age set to {age}")

# Test custom exception
try:
    set_age(25)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    set_age(-5)
except InvalidAgeError as e:
    print(f"✗ {e}")

try:
    set_age(200)
except InvalidAgeError as e:
    print(f"✗ {e}")

print("\n" + "=" * 50)
print("CUSTOM EXCEPTION WITH ATTRIBUTES")
print("=" * 50)

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.message = f"Insufficient funds! Balance: ₹{balance}, Required: ₹{amount}"
        super().__init__(self.message)

def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw_money(1000, 500)
    print(f"✓ Withdrawal successful. New balance: ₹{new_balance}")
except InsufficientFundsError as e:
    print(f"✗ Error: {e.message}")
    print(f"  Details: Balance={e.balance}, Requested={e.amount}")

try:
    new_balance = withdraw_money(1000, 1500)
except InsufficientFundsError as e:
    print(f"✗ Error: {e.message}")
    print(f"  Details: Balance={e.balance}, Requested={e.amount}")

print("\n" + "=" * 50)
print("EXCEPTION HIERARCHY")
print("=" * 50)

# Base exception for all validation errors
class ValidationError(Exception):
    """Base class for validation exceptions"""
    pass

# Specific validation exceptions
class EmailValidationError(ValidationError):
    """Error for email validation"""
    pass

class PasswordValidationError(ValidationError):
    """Error for password validation"""
    pass

class UsernameValidationError(ValidationError):
    """Error for username validation"""
    pass

def validate_user_data(username, email, password):
    if len(username) < 3:
        raise UsernameValidationError("Username must be at least 3 characters")
    
    if "@" not in email:
        raise EmailValidationError("Email must contain @")
    
    if len(password) < 8:
        raise PasswordValidationError("Password must be at least 8 characters")
    
    print("✓ All validations passed!")

# Test with specific catching
try:
    validate_user_data("ab", "user@example.com", "pass12345")
except  UsernameValidationError as e:
    print(f"✗ Username Error: {e}")
except EmailValidationError as e:
    print(f"✗ Email Error: {e}")
except PasswordValidationError as e:
    print(f"✗ Password Error: {e}")

# Test with generic catching
try:
    validate_user_data("john", "invalid-email", "pass")
except ValidationError as e:  # Catches all validation errors
    print(f"✗ Validation Error ({type(e).__name__}): {e}")

print("\n" + "=" * 50)
print("CUSTOM EXCEPTION WITH __str__ METHOD")
print("=" * 50)

class DatabaseError(Exception):
    def __init__(self, table, operation, reason):
        self.table = table
        self.operation = operation
        self.reason = reason
    
    def __str__(self):
        return f"Database Error on table '{self.table}' during {self.operation}: {self.reason}"

try:
    raise DatabaseError("users", "INSERT", "Duplicate primary key")
except DatabaseError as e:
    print(f"✗ {e}")

print("\n" + "=" * 50)
print("PRACTICAL: BANKING SYSTEM")
print("=" * 50)

class BankingError(Exception):
    """Base exception for banking errors"""
    pass

class InsufficientBalanceError(BankingError):
    def __init__(self, balance, requested):
        super().__init__(f"Balance ₹{balance} is less than requested ₹{requested}")
        self.balance = balance
        self.requested = requested

class NegativeAmountError(BankingError):
    def __init__(self, amount):
        super().__init__(f"Amount cannot be negative: ₹{amount}")
        self.amount = amount

class AccountFrozenError(BankingError):
    def __init__(self, account_id):
        super().__init__(f"Account {account_id} is frozen")
        self.account_id = account_id

class BankAccount:
    def __init__(self, account_id, balance=0, is_frozen=False):
        self.account_id = account_id
        self.balance = balance
        self.is_frozen = is_frozen
    
    def withdraw(self, amount):
        if self.is_frozen:
            raise AccountFrozenError(self.account_id)
        
        if amount < 0:
            raise NegativeAmountError(amount)
        
        if amount > self.balance:
            raise InsufficientBalanceError(self.balance, amount)
        
        self.balance -= amount
        print(f"✓ Withdrawn ₹{amount}. New balance: ₹{self.balance}")
    
    def deposit(self, amount):
        if amount < 0:
            raise NegativeAmountError(amount)
        
        self.balance += amount
        print(f"✓ Deposited ₹{amount}. New balance: ₹{self.balance}")

# Test banking system
account = BankAccount("ACC001", balance=5000)

try:
    account.deposit(1000)  # ✓ Works
except BankingError as e:
    print(f"✗ {e}")

try:
    account.withdraw(2000)  # ✓ Works
except BankingError as e:
    print(f"✗ {e}")

try:
    account.withdraw(10000)  # InsufficientBalanceError
except BankingError as e:
    print(f"✗ {e}")

try:
    account.deposit(-500)  # NegativeAmountError
except BankingError as e:
    print(f"✗ {e}")

frozen_account = BankAccount("ACC002", balance=1000, is_frozen=True)
try:
    frozen_account.withdraw(100)  # AccountFrozenError
except BankingError as e:
    print(f"✗ {e}")

print("\n" + "=" * 50)
print("CUSTOM EXCEPTION BEST PRACTICES")
print("=" * 50)

print("✓ Do:")
print("  - Inherit from Exception or specific exception types")
print("  - Give meaningful names (ending with 'Error')")
print("  - Add helpful error messages")
print("  - Create exception hierarchy for related errors")
print("  - Document your exceptions")
print()
print("✗ Don't:")
print("  - Inherit from BaseException (too broad)")
print("  - Create exceptions for everything (use built-in when possible)")
print("  - Leave exceptions empty (add context)")
print("  - Catch Exception without re-raising (unless intentional)")
