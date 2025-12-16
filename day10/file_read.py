# File Reading in Python

print("=" * 50)
print("METHOD 1: read() - Read entire file")
print("=" * 50)

# Create a sample file first
with open("sample.txt", "w") as f:
    f.write("Hello Python!\nWelcome to file handling.\nThird line of text.")

# Read entire file
with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

print("\n" + "=" * 50)
print("METHOD 2: readline() - Read one line")
print("=" * 50)

with open("sample.txt", "r") as file:
    line1 = file.readline()
    line2 = file.readline()
    print(f"First line: {line1.strip()}")
    print(f"Second line: {line2.strip()}")

print("\n" + "=" * 50)
print("METHOD 3: readlines() - Read all lines as list")
print("=" * 50)

with open("sample.txt", "r") as file:
    lines = file.readlines()
    print("All lines:")
    for i, line in enumerate(lines, 1):
        print(f"  Line {i}: {line.strip()}")

print("\n" + "=" * 50)
print("METHOD 4: Loop through file object")
print("=" * 50)

with open("sample.txt", "r") as file:
    print("Iterating through file:")
    for line_num, line in enumerate(file, 1):
        print(f"  {line_num}. {line.strip()}")

print("\n" + "=" * 50)
print("METHOD 5: read(n) - Read n characters")
print("=" * 50)

with open("sample.txt", "r") as file:
    chunk1 = file.read(10)  # First 10 characters
    chunk2 = file.read(10)  # Next 10 characters
    print(f"First 10 chars: '{chunk1}'")
    print(f"Next 10 chars: '{chunk2}'")

print("\n" + "=" * 50)
print("READING FILE WITHOUT 'with' STATEMENT")
print("=" * 50)

file = open("sample.txt", "r")
content = file.read()
print("Content:")
print(content)
file.close()  # Must close manually
print("(File closed manually)")

print("\n" + "=" * 50)
print("CHECKING IF FILE EXISTS")
print("=" * 50)

import os

if os.path.exists("sample.txt"):
    print("✓ File exists!")
    file_size = os.path.getsize("sample.txt")
    print(f"  File size: {file_size} bytes")
else:
    print("✗ File does not exist")

print("\n" + "=" * 50)
print("READING WITH ERROR HANDLING")
print("=" * 50)

try:
    with open("sample.txt", "r") as file:
        content = file.read()
        print("File read successfully")
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("READING SPECIFIC LINES")
print("=" * 50)

with open("sample.txt", "r") as file:
    lines = file.readlines()
    # Read specific line (e.g., line 2)
    if len(lines) >= 2:
        print(f"Second line: {lines[1].strip()}")

# Clean up
os.remove("sample.txt")
print("\n(Sample file cleaned up)")
