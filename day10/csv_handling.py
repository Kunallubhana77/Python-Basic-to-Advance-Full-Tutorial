# CSV File Handling in Python

import csv
import os

print("=" * 50)
print("WRITING CSV FILES")
print("=" * 50)

# Method 1: Using csv.writer
with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)
    
    # Write header
    writer.writerow(["Name", "Age", "Grade", "Marks"])
    
    # Write data rows
    writer.writerow(["Alice", 20, "A", 85])
    writer.writerow(["Bob", 21, "B", 78])
    writer.writerow(["Charlie", 19, "A", 92])

print("✓ CSV file created with writer")

print("\n" + "=" * 50)
print("READING CSV FILES")
print("=" * 50)

# Method 1: Using csv.reader
print("Using csv.reader:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n" + "=" * 50)
print("WRITING CSV WITH DICTWRITER")
print("=" * 50)

students = [
    {"name": "Alice", "age": 20, "grade": "A", "marks": 85},
    {"name": "Bob", "age": 21, "grade": "B", "marks": 78},
    {"name": "Charlie", "age": 19, "grade": "A", "marks": 92}
]

with open("students_dict.csv", "w", newline='') as file:
    fieldnames = ["name", "age", "grade", "marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()  # Write column headers
    writer.writerows(students)  # Write all rows

print("✓ CSV file created with DictWriter")

print("\n" + "=" * 50)
print("READING CSV WITH DICTREADER")
print("=" * 50)

print("Using csv.DictReader:")
with open("students_dict.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']}, Age: {row['age']}, Grade: {row['grade']}, Marks: {row['marks']}")

print("\n" + "=" * 50)
print("APPENDING TO CSV FILE")
print("=" * 50)

# Append new student
with open("students.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["David", 22, "B", 80])

print("✓ New row appended")
print("\nUpdated CSV:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n" + "=" * 50)
print("READING SPECIFIC COLUMNS")
print("=" * 50)

print("Names and Marks only:")
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    for row in reader:
        print(f"Name: {row[0]}, Marks: {row[3]}")

print("\n" + "=" * 50)
print("FILTERING CSV DATA")
print("=" * 50)

print("Students with grade 'A':")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["Grade"] == "A":
            print(f"  {row['Name']} - Marks: {row['Marks']}")

print("\n" + "=" * 50)
print("CSV WITH CUSTOM DELIMITER")
print("=" * 50)

# Using semicolon as delimiter
with open("custom.csv", "w", newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["Product", "Price", "Quantity"])
    writer.writerow(["Apple", 50, 10])
    writer.writerow(["Banana", 30, 15])

print("CSV with semicolon delimiter:")
with open("custom.csv", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("COUNTING ROWS IN CSV")
print("=" * 50)

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    row_count = sum(1 for row in reader)
    print(f"Total rows (including header): {row_count}")

print("\n" + "=" * 50)
print("CALCULATING FROM CSV DATA")
print("=" * 50)

total_marks = 0
count = 0

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_marks += int(row["Marks"])
        count += 1

average = total_marks / count if count > 0 else 0
print(f"Average marks: {average:.2f}")

# Clean up
for filename in ["students.csv", "students_dict.csv", "custom.csv"]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n(All CSV files cleaned up)")
