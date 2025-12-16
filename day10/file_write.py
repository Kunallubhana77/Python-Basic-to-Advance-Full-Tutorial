# File Writing in Python

import os

print("=" * 50)
print("METHOD 1: write() - Write text to file")
print("=" * 50)

# Write mode ('w') - Creates new or overwrites existing
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.")
    print("✓ File written successfully")

# Read and display
with open("output.txt", "r") as file:
    print("File content:")
    print(file.read())

print("\n" + "=" * 50)
print("METHOD 2: writelines() - Write multiple lines")
print("=" * 50)

lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("output2.txt", "w") as file:
    file.writelines(lines)
    print("✓ Multiple lines written")

with open("output2.txt", "r") as file:
    print("File content:")
    print(file.read())

print("\n" + "=" * 50)
print("METHOD 3: Writing numbers and lists")
print("=" * 50)

with open("numbers.txt", "w") as file:
    # Write numbers
    for i in range(1, 6):
        file.write(f"Number: {i}\n")
    
    # Write list items
    fruits = ["Apple", "Banana", "Cherry"]
    for fruit in fruits:
        file.write(f"Fruit: {fruit}\n")

with open("numbers.txt", "r") as file:
    print("File content:")
    print(file.read())

print("\n" + "=" * 50)
print("OVERWRITING vs CREATING NEW FILE")
print("=" * 50)

# First write
with open("test.txt", "w") as file:
    file.write("Original content")

print("Original content written")
with open("test.txt", "r") as file:
    print(f"Content: {file.read()}")

# Overwrite
with open("test.txt", "w") as file:
    file.write("New content - old one is gone!")

print("\nAfter overwriting:")
with open("test.txt", "r") as file:
    print(f"Content: {file.read()}")

print("\n" + "=" * 50)
print("WRITING WITHOUT 'with' STATEMENT")
print("=" * 50)

file = open("manual.txt", "w")
file.write("Written without 'with' statement\n")
file.write("Must close manually!")
file.close()
print("✓ File written and closed manually")

with open("manual.txt", "r") as file:
    print("Content:")
    print(file.read())

print("\n" + "=" * 50)
print("WRITING WITH ERROR HANDLING")
print("=" * 50)

try:
    with open("safe_write.txt", "w") as file:
        file.write("Writing with error handling\n")
        file.write("This is safer!\n")
    print("✓ File written successfully")
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("WRITING FORMATTED DATA")
print("=" * 50)

students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 92},
    {"name": "Charlie", "marks": 78}
]

with open("students.txt", "w") as file:
    file.write("STUDENT MARKS REPORT\n")
    file.write("=" * 30 + "\n")
    for student in students:
        file.write(f"Name: {student['name']:10} | Marks: {student['marks']}\n")

with open("students.txt", "r") as file:
    print("Formatted file content:")
    print(file.read())

# Clean up
for filename in ["output.txt", "output2.txt", "numbers.txt", "test.txt", "manual.txt", "safe_write.txt", "students.txt"]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n(All sample files cleaned up)")
