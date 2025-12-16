# Finally Block in Python

print("=" * 50)
print("BASIC FINALLY BLOCK")
print("=" * 50)

try:
    print("Trying to execute code...")
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error occurred!")
finally:
    print("Finally block always executes!")

print("\n" + "=" * 50)
print("FINALLY WITH EXCEPTION")
print("=" * 50)

try:
    print("Trying division by zero...")
    result = 10 / 0
except ZeroDivisionError:
    print("✗ Caught division by zero")
finally:
    print("✓ Finally block runs even after exception")

print("\n" + "=" * 50)
print("FINALLY WITHOUT EXCEPTION")
print("=" * 50)

try:
    print("Normal execution...")
    x = 5 + 5
    print(f"Result: {x}")
finally:
    print("✓ Finally runs in successful execution too")

print("\n" + "=" * 50)
print("FILE HANDLING WITH FINALLY")
print("=" * 50)

# Create test file
with open("test.txt", "w") as f:
    f.write("Test content")

# Traditional way (before 'with' statement)
file = None
try:
    print("Opening file...")
    file = open("test.txt", "r")
    content = file.read()
    print(f"Content: {content}")
except FileNotFoundError:
    print("✗ File not found")
finally:
    if file:
        file.close()
        print("✓ File closed in finally block")

print("\n" + "=" * 50)
print("TRY-EXCEPT-ELSE-FINALLY")
print("=" * 50)

def full_structure(number):
    try:
        print(f"Trying to divide 100 by {number}")
        result = 100 / number
    except ZeroDivisionError:
        print("✗ Division by zero in except block")
    else:
        print(f"✓ Success! Result: {result} (else block)")
    finally:
        print("→ Finally block always runs\n")

full_structure(5)   # try → else → finally
full_structure(0)   # try → except → finally

print("=" * 50)
print("FINALLY WITH RETURN STATEMENT")
print("=" * 50)

def test_finally_return():
    try:
        print("In try block")
        return "Returning from try"
    finally:
        print("Finally block runs before return!")

result = test_finally_return()
print(f"Function returned: {result}")

print("\n" + "=" * 50)
print("FINALLY WITH BREAK/CONTINUE")
print("=" * 50)

print("Finally with break:")
for i in range(3):
    try:
        print(f"  Loop iteration: {i}")
        if i == 1:
            break
    finally:
        print(f"  Finally for iteration {i}")

print("\n" + "=" * 50)
print("MULTIPLE CLEANUP OPERATIONS")
print("=" * 50)

def complex_operation():
    file1 = None
    file2 = None
    
    try:
        print("Opening files...")
        file1 = open("file1.txt", "w")
        file2 = open("file2.txt", "w")
        
        file1.write("File 1 content")
        file2.write("File 2 content")
        
        print("✓ Files written successfully")
        
    except Exception as e:
        print(f"✗ Error: {e}")
    finally:
        # Cleanup all resources
        if file1:
            file1.close()
            print("→ File1 closed")
        if file2:
            file2.close()
            print("→ File2 closed")

complex_operation()

print("\n" + "=" * 50)
print("FINALLY VS WITH STATEMENT")
print("=" * 50)

print("Using finally:")
f = None
try:
    f = open("example.txt", "w")
    f.write("Content")
finally:
    if f:
        f.close()
        print("  Closed in finally")

print("\nUsing 'with' (better):")
with open("example2.txt", "w") as f:
    f.write("Content")
print("  Automatically closed (no finally needed)")

print("\n" + "=" * 50)
print("PRACTICAL: DATABASE-LIKE CONNECTION")
print("=" * 50)

class DatabaseConnection:
    def __init__(self, name):
        self.name = name
        self.connected = False
    
    def connect(self):
        print(f"  → Connecting to {self.name}")
        self.connected = True
    
    def close(self):
        if self.connected:
            print(f"  → Closing connection to {self.name}")
            self.connected = False

def perform_database_operation(should_fail=False):
    db = DatabaseConnection("PostgreSQL")
    
    try:
        db.connect()
        print("  → Performing operations...")
        
        if should_fail:
            raise Exception("Simulated database error!")
        
        print("  ✓ Operations completed")
        
    except Exception as e:
        print(f"  ✗ Error: {e}")
    finally:
        db.close()
        print("  ✓ Cleanup done in finally\n")

print("Successful operation:")
perform_database_operation(should_fail=False)

print("Failed operation:")
perform_database_operation(should_fail=True)

# Clean up files
import os
for filename in ["test.txt", "file1.txt", "file2.txt", "example.txt", "example2.txt"]:
    if os.path.exists(filename):
        os.remove(filename)

print("(All test files cleaned up)")
