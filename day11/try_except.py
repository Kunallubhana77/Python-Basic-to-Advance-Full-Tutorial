# Try-Except in Python

print("=" * 50)
print("BASIC TRY-EXCEPT")
print("=" * 50)

# Without exception handling - would crash
print("Example 1: Division by zero")
try:
    result = 10 / 0
    print(f"Result: {result}")
except:
    print("✗ Error: Cannot divide by zero!")

print("\n" + "=" * 50)
print("SPECIFIC EXCEPTION TYPE")
print("=" * 50)

try:
    number = int("abc")  # This will fail
except ValueError:
    print("✗ ValueError: Invalid conversion to integer")

print("\n" + "=" * 50)
print("MULTIPLE EXCEPT BLOCKS")
print("="* 50)

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"{a} / {b} = {result}")
    except ZeroDivisionError:
        print("✗ Error: Division by zero")
    except TypeError:
        print("✗ Error: Invalid data type")

divide_numbers(10, 2)   # Works fine
divide_numbers(10, 0)   # ZeroDivisionError
divide_numbers(10, "a") # TypeError

print("\n" + "=" * 50)
print("CATCHING EXCEPTION OBJECT")
print("=" * 50)

try:
    file = open("nonexistent.txt", "r")
except FileNotFoundError as e:
    print(f"✗ File Error: {e}")

print("\n" + "=" * 50)
print("GENERIC EXCEPTION HANDLING")
print("=" * 50)

try:
    # Some operation that might fail
    x = [1, 2, 3]
    print(x[10])  # Index out of range
except Exception as e:
    print(f"✗ An error occurred: {type(e).__name__}")
    print(f"  Details: {e}")

print("\n" + "=" * 50)
print("TRY-EXCEPT WITH ELSE")
print("=" * 50)

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("✗ Cannot divide by zero")
    else:
        # Executes only if no exception occurred
        print(f"✓ Success: {a} / {b} = {result}")

safe_divide(10, 2)  # else block runs
safe_divide(10, 0)  # else block doesn't run

print("\n" + "=" * 50)
print("NESTED TRY-EXCEPT")
print("=" * 50)

try:
    try:
        number = int("123")
        result = number / 0
    except ValueError:
        print("Inner: Value Error")
    except ZeroDivisionError:
        print("Inner: Division by zero")
        raise  # Re-raise the exception
except ZeroDivisionError:
    print("Outer: Caught re-raised exception")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: User Input")
print("=" * 50)

def get_number():
    # Demo version without actual input
    test_inputs = ["abc", "10", "0"]
    
    for test_input in test_inputs:
        print(f"\nTrying to convert: '{test_input}'")
        try:
            number = int(test_input)
            print(f"✓ Successfully converted to: {number}")
        except ValueError:
            print(f"✗ '{test_input}' is not a valid number")

get_number()

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: List Access")
print("=" * 50)

def safe_list_access(lst, index):
    try:
        value = lst[index]
        print(f"✓ Value at index {index}: {value}")
    except IndexError:
        print(f"✗ Index {index} is out of range")
    except TypeError:
        print(f"✗ Invalid index type")

my_list = [10, 20, 30, 40, 50]
safe_list_access(my_list, 2)   # ✓ Works
safe_list_access(my_list, 10)  # ✗ Out of range
safe_list_access(my_list, "a") # ✗ Wrong type

print("\n" + "=" * 50)
print("COMMON EXCEPTION TYPES")
print("=" * 50)

exceptions = {
    "ZeroDivisionError": "10 / 0",
    "ValueError": "int('abc')",
    "TypeError": "10 + 'hello'",
    "IndexError": "[1,2,3][10]",
    "KeyError": "{'a':1}['b']",
    "FileNotFoundError": "open('nonexistent.txt')",
    "AttributeError": "'hello'.nonexistent()"
}

print("Common Exceptions:")
for exc, example in exceptions.items():
    print(f"  {exc:25} → {example}")
