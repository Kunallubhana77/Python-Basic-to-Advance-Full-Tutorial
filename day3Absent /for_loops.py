# For Loop Examples in Python

print("=" * 50)
print("Example 1: Simple For Loop with Range")
print("=" * 50)

for i in range(1, 6):
    print(f"Iteration {i}")

print("\n" + "=" * 50)
print("Example 2: Iterating Through a List")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "mango", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

print("\n" + "=" * 50)
print("Example 3: Sum of Numbers Using For Loop")
print("=" * 50)

total = 0
for num in range(1, 11):
    total += num
print(f"Sum of numbers 1 to 10: {total}")

print("\n" + "=" * 50)
print("Example 4: Multiplication Table")
print("=" * 50)

number = 5
print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

print("\n" + "=" * 50)
print("Example 5: For Loop with String")
print("=" * 50)

word = "Python"
print("Characters in Python:")
for char in word:
    print(char)

print("\n" + "=" * 50)
print("Example 6: For Loop with Dictionary")
print("=" * 50)

student = {"name": "John", "age": 20, "grade": "A"}
print("Student Details:")
for key, value in student.items():
    print(f"{key}: {value}")

print("\n" + "=" * 50)
print("Example 7: For Loop with Enumerate")
print("=" * 50)

colors = ["red", "green", "blue", "yellow"]
print("Colors with index:")
for index, color in enumerate(colors, start=1):
    print(f"{index}. {color}")

print("\n" + "=" * 50)
print("Example 8: For Loop with Range and Step")
print("=" * 50)

print("Even numbers from 0 to 20:")
for num in range(0, 21, 2):
    print(num, end=" ")
print()  # New line
