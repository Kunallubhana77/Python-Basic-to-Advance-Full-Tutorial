# With Statement in Python

import os

print("=" * 50)
print("WHY USE 'with' STATEMENT?")
print("=" * 50)

print("Traditional way (without 'with'):")
print("- Must manually open file")
print("- Must remember to close file")
print("- Risk: File stays open if error occurs")
print()
print("With 'with' statement:")
print("- Automatically closes file")
print("- Works even if error occurs")
print("- Cleaner and safer code")

print("\n" + "=" * 50)
print("WITHOUT 'with' STATEMENT")
print("=" * 50)

# Manual file handling
file = open("test1.txt", "w")
file.write("This requires manual closing")
file.close()
print("✓ File written and closed manually")

print("\n" + "=" * 50)
print("WITH 'with' STATEMENT")
print("=" * 50)

# Automatic file handling
with open("test2.txt", "w") as file:
    file.write("This closes automatically")
# File is automatically closed here
print("✓ File automatically closed after 'with' block")

print("\n" + "=" * 50)
print("MULTIPLE FILES WITH 'with'")
print("=" * 50)

# Open multiple files at once
with open("source.txt", "w") as source, open("destination.txt", "w") as dest:
    source.write("Source content")
    dest.write("Destination content")

print("✓ Both files handled together")

print("\n" + "=" * 50)
print("ERROR HANDLING COMPARISON")
print("=" * 50)

print("Without 'with' - risky:")
print("```")
print("file = open('test.txt', 'w')")
print("file.write('data')  # If error here...")
print("file.close()        # ...this never runs!")
print("```")

print("\nWith 'with' - safe:")
print("```")
print("with open('test.txt', 'w') as file:")
print("    file.write('data')  # Even if error...")
print("# ...file still closes automatically!")
print("```")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: Reading and Writing")
print("=" * 50)

# Create source file
with open("input.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

# Read and process
with open("input.txt", "r") as infile:
    content = infile.read()
    print("Input content:")
    print(content)

# Read from one, write to another
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())

print("Output content (uppercased):")
with open("output.txt", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("NESTED 'with' STATEMENTS")
print("=" * 50)

with open("file1.txt", "w") as f1:
    f1.write("First file")
    with open("file2.txt", "w") as f2:
        f2.write("Second file (nested)")

print("✓ Nested 'with' statements work fine")

print("\n" + "=" * 50)
print("'with' STATEMENT WITH TRY-EXCEPT")
print("=" * 50)

try:
    with open("safe_file.txt", "w") as file:
        file.write("Safe writing with error handling\n")
        # Some operation that might fail
        file.write("More content\n")
    print("✓ File operations completed successfully")
except IOError as e:
    print(f"✗ IOError: {e}")
except Exception as e:
    print(f"✗ Error: {e}")

print("\n" + "=" * 50)
print("CUSTOM CONTEXT MANAGER (Advanced)")
print("=" * 50)

class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"  → Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            print(f"  → Closing {self.filename}")
            self.file.close()

# Use custom context manager
with FileManager("custom.txt", "w") as file:
    file.write("Using custom context manager!")

print("\n✓ Custom context manager demonstrated")

print("\n" + "=" * 50)
print("CHECKING IF FILE IS CLOSED")
print("=" * 50)

# Without 'with'
f = open("check1.txt", "w")
print(f"File closed? {f.closed}")  # False
f.close()
print(f"File closed? {f.closed}")  # True

# With 'with'
with open("check2.txt", "w") as f:
    print(f"Inside 'with', closed? {f.closed}")  # False
print(f"Outside 'with', closed? {f.closed}")  # True

# Clean up
files_to_remove = [
    "test1.txt", "test2.txt", "source.txt", "destination.txt",
    "input.txt", "output.txt", "file1.txt", "file2.txt",
    "safe_file.txt", "custom.txt", "check1.txt", "check2.txt"
]

for filename in files_to_remove:
    if os.path.exists(filename):
        os.remove(filename)

print("\n(All sample files cleaned up)")
