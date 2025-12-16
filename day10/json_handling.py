# JSON File Handling in Python

import json
import os

print("=" * 50)
print("WRITING JSON TO FILE")
print("=" * 50)

# Python dictionary
student = {
    "name": "Kunal",
    "age": 22,
    "courses": ["Python", "JavaScript", "SQL"],
    "grades": {
        "Python": "A",
        "JavaScript": "B",
        "SQL": "A"
    }
}

# Write JSON to file
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

print("✓ JSON file created")
print("\nFile content:")
with open("student.json", "r") as file:
    print(file.read())

print("\n" + "=" * 50)
print("READING JSON FROM FILE")
print("=" * 50)

with open("student.json", "r") as file:
    data = json.load(file)
    print(f"Name: {data['name']}")
    print(f"Age: {data['age']}")
    print(f"Courses: {data['courses']}")
    print(f"Grades: {data['grades']}")

print("\n" + "=" * 50)
print("WRITING LIST OF OBJECTS")
print("=" * 50)

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Charlie", "age": 19, "grade": "A"}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("✓ List of students saved")

print("\n" + "=" * 50)
print("READING AND ITERATING JSON ARRAY")
print("=" * 50)

with open("students.json", "r") as file:
    students_data = json.load(file)
    print("All students:")
    for student in students_data:
        print(f"  - {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

print("\n" + "=" * 50)
print("UPDATING JSON FILE")
print("=" * 50)

# Read existing JSON
with open("student.json", "r") as file:
    data = json.load(file)

# Modify data
data["age"] = 23
data["courses"].append("React")
data["grades"]["React"] = "A+"

# Write back
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("✓ JSON updated")
print("\nUpdated content:")
with open("student.json", "r") as file:
    updated = json.load(file)
    print(f"Age: {updated['age']}")
    print(f"Courses: {updated['courses']}")

print("\n" + "=" * 50)
print("JSON to STRING and STRING to JSON")
print("=" * 50)

# Python object to JSON string
person = {"name": "John", "city": "Mumbai"}
json_string = json.dumps(person, indent=2)
print("JSON string:")
print(json_string)
print(f"Type: {type(json_string)}")

# JSON string to Python object
json_text = '{"product": "Laptop", "price": 50000}'
python_obj = json.loads(json_text)
print(f"\nPython object: {python_obj}")
print(f"Type: {type(python_obj)}")
print(f"Product: {python_obj['product']}, Price: {python_obj['price']}")

print("\n" + "=" * 50)
print("PRETTY PRINTING JSON")
print("=" * 50)

data = {"name": "Test", "items": [1, 2, 3], "nested": {"key": "value"}}

print("Without indentation:")
print(json.dumps(data))

print("\nWith indentation:")
print(json.dumps(data, indent=4))

print("\nWith sorting keys:")
print(json.dumps(data, indent=4, sort_keys=True))

print("\n" + "=" * 50)
print("APPENDING TO JSON ARRAY")
print("=" * 50)

# Read existing array
with open("students.json", "r") as file:
    students = json.load(file)

# Add new student
students.append({"name": "David", "age": 22, "grade": "B"})

# Write back
with open("students.json", "w") as file:
    json.dump(students, file, indent=2)

print("✓ New student added")
print("\nAll students:")
with open("students.json", "r") as file:
    all_students = json.load(file)
    for s in all_students:
        print(f"  - {s['name']}")

print("\n" + "=" * 50)
print("ERROR HANDLING WITH JSON")
print("=" * 50)

# Try to parse invalid JSON
invalid_json = '{"name": "Test", "invalid": }'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"✗ JSON Decode Error: {e}")

# Try to read non-existent file
try:
    with open("nonexistent.json", "r") as file:
        data = json.load(file)
except FileNotFoundError:
    print("✗ File not found!")

print("\n" + "=" * 50)
print("NESTED JSON STRUCTURE")
print("=" * 50)

company = {
    "name": "Tech Corp",
    "employees": [
        {
            "name": "Alice",
            "role": "Developer",
            "skills": ["Python", "JavaScript"],
            "projects": [
                {"name": "Project A", "status": "completed"},
                {"name": "Project B", "status": "ongoing"}
            ]
        },
        {
            "name": "Bob",
            "role": "Designer",
            "skills": ["Figma", "Photoshop"],
            "projects": [
                {"name": "Project C", "status": "completed"}
            ]
        }
    ]
}

with open("company.json", "w") as file:
    json.dump(company, file, indent=2)

print("✓ Complex nested JSON created")
print("\nAccessing nested data:")
with open("company.json", "r") as file:
    company_data = json.load(file)
    print(f"Company: {company_data['name']}")
    print(f"First employee: {company_data['employees'][0]['name']}")
    print(f"Their skills: {company_data['employees'][0]['skills']}")

# Clean up
for filename in ["student.json", "students.json", "company.json"]:
    if os.path.exists(filename):
        os.remove(filename)

print("\n(All JSON files cleaned up)")
