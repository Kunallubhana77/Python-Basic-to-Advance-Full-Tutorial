# Create a dictionary of 5 students marks and print topper

marks = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 78,
    'David': 95,
    'Eve': 88
}

print("Student Marks:", marks)

# Find topper
topper = max(marks, key=marks.get)
print(f"Topper is {topper} with {marks[topper]} marks.")
