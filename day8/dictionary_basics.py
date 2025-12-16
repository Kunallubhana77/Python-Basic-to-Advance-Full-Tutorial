# Dictionary Basics in Python

print("=" * 50)
print("DICTIONARY CREATION")
print("=" * 50)

# Creating a dictionary
student = {
    "name": "Kunal",
    "age": 22,
    "course": "Python Programming",
    "grade": "A"
}
print(f"Student dictionary: {student}")

# Empty dictionary
empty_dict = {}
print(f"Empty dictionary: {empty_dict}")

# Using dict() constructor
person = dict(name="John", city="Mumbai", profession="Developer")
print(f"Person dictionary: {person}")

print("\n" + "=" * 50)
print("ACCESSING DICTIONARY VALUES")
print("=" * 50)

# Access using keys
print(f"Student name: {student['name']}")
print(f"Student age: {student['age']}")

# Access using get() method
print(f"Student grade: {student.get('grade')}")
print(f"Non-existent key: {student.get('address', 'Not Available')}")

print("\n" + "=" * 50)
print("MODIFYING DICTIONARY")
print("=" * 50)

# Update existing value
student["age"] = 23
print(f"Updated age: {student['age']}")

# Add new key-value pair
student["email"] = "kunal@example.com"
print(f"After adding email: {student}")

# Update multiple values
student.update({"grade": "A+", "semester": 5})
print(f"After update: {student}")

print("\n" + "=" * 50)
print("DICTIONARY OPERATIONS")
print("=" * 50)

# Get all keys
print(f"All keys: {list(student.keys())}")

# Get all values
print(f"All values: {list(student.values())}")

# Get all key-value pairs
print(f"All items: {list(student.items())}")

# Check if key exists
print(f"'name' in dictionary: {'name' in student}")
print(f"'address' in dictionary: {'address' in student}")

# Dictionary length
print(f"Dictionary length: {len(student)}")

print("\n" + "=" * 50)
print("REMOVING ITEMS FROM DICTIONARY")
print("=" * 50)

# Remove using pop()
removed_email = student.pop("email")
print(f"Removed email: {removed_email}")
print(f"After removing email: {student}")

# Remove using del
del student["semester"]
print(f"After deleting semester: {student}")

# Clear all items
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()
print(f"After clear: {temp_dict}")

print("\n" + "=" * 50)
print("ITERATING THROUGH DICTIONARY")
print("=" * 50)

# Iterate through keys
print("Keys:")
for key in student:
    print(f"  {key}")

# Iterate through values
print("\nValues:")
for value in student.values():
    print(f"  {value}")

# Iterate through key-value pairs
print("\nKey-Value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("NESTED DICTIONARY")
print("=" * 50)

students = {
    "student1": {"name": "Raj", "marks": 85},
    "student2": {"name": "Priya", "marks": 92},
    "student3": {"name": "Amit", "marks": 78}
}

print("Nested dictionary:")
for student_id, info in students.items():
    print(f"{student_id}: {info['name']} - Marks: {info['marks']}")
