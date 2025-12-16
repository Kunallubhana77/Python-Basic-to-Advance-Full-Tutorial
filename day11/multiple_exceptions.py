# Multiple Exception Handling in Python

print("=" * 50)
print("HANDLING MULTIPLE EXCEPTIONS SEPARATELY")
print("=" * 50)

def process_data(data, index):
    try:
        # Multiple potential errors
        value = int(data[index])
        result = 100 / value
        return result
    except IndexError:
        print("✗ IndexError: Index out of range")
    except ValueError:
        print("✗ ValueError: Cannot convert to integer")
    except ZeroDivisionError:
        print("✗ ZeroDivisionError: Cannot divide by zero")

print("Test 1: Valid data")
process_data(["10", "20", "30"], 1)

print("\nTest 2: Index error")
process_data(["10", "20"], 5)

print("\nTest 3: Value error")
process_data(["abc", "20"], 0)

print("\nTest 4: Zero division")
process_data(["0", "20"], 0)

print("\n" + "=" * 50)
print("HANDLING MULTIPLE EXCEPTIONS TOGETHER")
print("=" * 50)

def calculator(a, b, operation):
    try:
        if operation == "add":
            result = a + b
        elif operation == "divide":
            result = a / b
        elif operation == "index":
            result = [a, b][10]  # Will cause IndexError
        print(f"✓ Result: {result}")
    except (ZeroDivisionError, TypeError, IndexError) as e:
        print(f"✗ Error occurred: {type(e).__name__}")
        print(f"  Message: {e}")

calculator(10, 2, "add")
calculator(10, 0, "divide")
calculator(10, "abc", "add")
calculator(10, 5, "index")

print("\n" + "=" * 50)
print("SPECIFIC THEN GENERIC EXCEPTION")
print("=" * 50)

def robust_operation(value):
    try:
        # Try to perform operations
        num = int(value)
        result = 100 / num
        items = [1, 2, 3]
        print(items[num])
    except ValueError:
        print("✗ Specific: Cannot convert to integer")
    except ZeroDivisionError:
        print("✗ Specific: Division by zero")
    except IndexError:
        print("✗ Specific: Index out of range")
    except Exception as e:
        # Catch any other exception
        print(f"✗ Generic: {type(e).__name__} - {e}")

print("Test cases:")
robust_operation("10")    # Works
robust_operation("abc")   # ValueError
robust_operation("0")     # ZeroDivisionError
robust_operation("1")     # Works fine

print("\n" + "=" * 50)
print("MULTIPLE EXCEPTIONS WITH CUSTOM MESSAGES")
print("=" * 50)

def safe_file_operations(filename, line_num):
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            specific_line = lines[line_num]
            number = int(specific_line)
            print(f"✓ Number from file: {number}")
    except FileNotFoundError:
        print(f"✗ File '{filename}' not found")
    except IndexError:
        print(f"✗ Line {line_num} doesn't exist in file")
    except ValueError:
        print(f"✗ Line content is not a valid number")
    except PermissionError:
        print(f"✗ No permission to read '{filename}'")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

# Create test file
with open("test_numbers.txt", "w") as f:
    f.write("100\n200\nabc\n")

safe_file_operations("test_numbers.txt", 0)   # ✓ Works
safe_file_operations("test_numbers.txt", 2)   # ValueError
safe_file_operations("test_numbers.txt", 10)  # IndexError
safe_file_operations("nonexistent.txt", 0)    # FileNotFoundError

# Clean up
import os
os.remove("test_numbers.txt")

print("\n" + "=" * 50)
print("EXCEPTION HIERARCHY DEMO")
print("=" * 50)

def exception_order(test_case):
    try:
        if test_case == 1:
            result = 10 / 0
        elif test_case == 2:
            result = int("abc")
        elif test_case == 3:
            result = [1][10]
    except ArithmeticError as e:  # Parent of ZeroDivisionError
        print(f"✗ Arithmetic Error: {type(e).__name__}")
    except LookupError as e:      # Parent of IndexError, KeyError
        print(f"✗ Lookup Error: {type(e).__name__}")
    except ValueError as e:
        print(f"✗ Value Error: {e}")
    except Exception as e:        # Parent of all
        print(f"✗ General Exception: {type(e).__name__}")

exception_order(1)  # ZeroDivisionError → ArithmeticError
exception_order(2)  # ValueError
exception_order(3)  # IndexError → LookupError

print("\n" + "=" * 50)
print("PRACTICAL: CALCULATOR WITH ERROR HANDLING")
print("=" * 50)

def smart_calculator(num1, num2, operator):
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b
    }
    
    try:
        # Multiple potential errors
        n1 = float(num1)
        n2 = float(num2)
        
        if operator not in operations:
            raise ValueError(f"Invalid operator: {operator}")
        
        result = operations[operator](n1, n2)
        print(f"✓ {n1} {operator} {n2} = {result}")
        
    except ValueError as e:
        print(f"✗ Invalid input: {e}")
    except ZeroDivisionError:
        print(f"✗ Cannot divide by zero")
    except TypeError as e:
        print(f"✗ Type error: {e}")

print("Test cases:")
smart_calculator("10", "5", "+")    # ✓
smart_calculator("10", "5", "/")    # ✓
smart_calculator("10", "0", "/")    # ZeroDivisionError
smart_calculator("abc", "5", "+")   # ValueError
smart_calculator("10", "5", "%")    # ValueError - invalid operator
