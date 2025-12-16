# File Append Mode in Python

import os

print("=" * 50)
print("APPEND MODE ('a') - Add to existing file")
print("=" * 50)

# Create initial file
with open("log.txt", "w") as file:
    file.write("Log Entry 1: System started\n")

print("Initial content:")
with open("log.txt", "r") as file:
    print(file.read())

# Append to file
with open("log.txt", "a") as file:
    file.write("Log Entry 2: User logged in\n")
    file.write("Log Entry 3: File uploaded\n")

print("\nAfter appending:")
with open("log.txt", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("APPEND vs WRITE MODE")
print("=" * 50)

# Write mode - overwrites
with open("demo.txt", "w") as file:
    file.write("First write\n")

with open("demo.txt", "w") as file:
    file.write("Second write (first is gone!)\n")

print("Using write mode (w):")
with open("demo.txt", "r") as file:
    print(file.read())

# Append mode - adds to end
with open("demo.txt", "a") as file:
    file.write("Third line (appended)\n")
    file.write("Fourth line (also appended)\n")

print("After appending:")
with open("demo.txt", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("CREATING FILE IF NOT EXISTS")
print("=" * 50)

# Append mode creates file if it doesn't exist
with open("newfile.txt", "a") as file:
    file.write("This file was created by append mode\n")

print("✓ File created (if didn't exist)")
with open("newfile.txt", "r") as file:
    print("Content:")
    print(file.read())

print("\n" + "=" * 50)
print("APPENDING WITH TIMESTAMPS")
print("=" * 50)

from datetime import datetime

with open("activity_log.txt", "a") as file:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] User action performed\n")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] Data saved successfully\n")

print("Activity log:")
with open("activity_log.txt", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("APPEND WITH ERROR HANDLING")
print("=" * 50)

try:
    with open("safe_append.txt", "a") as file:
        file.write("Safely appending line 1\n")
        file.write("Safely appending line 2\n")
    print("✓ Content appended successfully")
    
    with open("safe_append.txt", "r") as file:
        print("Content:")
        print(file.read())
except Exception as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLE: To-Do List")
print("=" * 50)

# Initialize to-do list
with open("todo.txt", "w") as file:
    file.write("MY TO-DO LIST\n")
    file.write("=" * 30 + "\n")

# Add tasks
tasks = [
    "1. Complete Python tutorial",
    "2. Practice file handling",
    "3. Build a project"
]

with open("todo.txt", "a") as file:
    for task in tasks:
        file.write(task + "\n")

print("To-Do List:")
with open("todo.txt", "r") as file:
    print(file.read())

# Add more tasks later
with open("todo.txt", "a") as file:
    file.write("4. Review code\n")
    file.write("5. Push to GitHub\n")

print("\nUpdated To-Do List:")
with open("todo.txt", "r") as file:
    print(file.read())

# Clean up
for filename in ["log.txt", "demo.txt", "newfile.txt", "activity_log.txt", "safe_append.txt", "todo.txt"]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n(All sample files cleaned up)")
