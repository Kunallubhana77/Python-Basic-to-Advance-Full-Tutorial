# Dictionary Comprehension in Python

print("=" * 50)
print("BASIC DICTIONARY COMPREHENSION")
print("=" * 50)

# Create dictionary from range
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# Create dictionary from list
fruits = ["apple", "banana", "cherry"]
fruit_lengths = {fruit: len(fruit) for fruit in fruits}
print(f"Fruit lengths: {fruit_lengths}")

print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION WITH CONDITION")
print("=" * 50)

# Only even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# Filter by value
numbers = {x: x**2 for x in range(1, 11)}
filtered = {k: v for k, v in numbers.items() if v > 25}
print(f"Values > 25: {filtered}")

print("\n" + "=" * 50)
print("DICTIONARY COMPREHENSION FROM TWO LISTS")
print("=" * 50)

keys = ["name", "age", "city"]
values = ["Kunal", 22, "Mumbai"]
person = {k: v for k, v in zip(keys, values)}
print(f"Person: {person}")

print("\n" + "=" * 50)
print("NESTED DICTIONARY COMPREHENSION")
print("=" * 50)

# Multiplication table
multiplication = {
    i: {j: i*j for j in range(1, 6)} 
    for i in range(1, 6)
}
print("Multiplication table:")
for key, value in multiplication.items():
    print(f"  {key}: {value}")

print("\n" + "=" * 50)
print("SWAP KEYS AND VALUES")
print("=" * 50)

original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Swapped: {swapped}")

print("\n" + "=" * 50)
print("CONVERT STRING TO DICT")
print("=" * 50)

text = "hello"
char_count = {char: text.count(char) for char in text}
print(f"Character count in 'hello': {char_count}")

print("\n" + "=" * 50)
print("IF-ELSE IN DICT COMPREHENSION")
print("=" * 50)

# Label numbers as even or odd
number_labels = {
    x: "even" if x % 2 == 0 else "odd" 
    for x in range(1, 11)
}
print(f"Number labels: {number_labels}")

print("\n" + "=" * 50)
print("DICTIONARY FROM LIST OF TUPLES")
print("=" * 50)

students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
grades = {name: marks for name, marks in students}
print(f"Student grades: {grades}")

print("\n" + "=" * 50)
print("FILTER DICTIONARY BY KEY/VALUE")
print("=" * 50)

data = {
    "apple": 10,
    "banana": 15,
    "cherry": 8,
    "date": 20,
    "elderberry": 5
}

# Filter by key length
long_names = {k: v for k, v in data.items() if len(k) > 6}
print(f"Fruits with name length > 6: {long_names}")

# Filter by value
expensive = {k: v for k, v in data.items() if v >= 10}
print(f"Fruits with value >= 10: {expensive}")
