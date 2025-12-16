# Nested Loops in Python

print("=" * 50)
print("Example 1: Basic Nested Loop")
print("=" * 50)

for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
    print()  # New line after each inner loop

print("=" * 50)
print("Example 2: Multiplication Table (Nested Loop)")
print("=" * 50)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} × {j} = {i*j:2d}", end="  ")
    print()  # New line after each row

print("\n" + "=" * 50)
print("Example 3: Nested Loop with Lists")
print("=" * 50)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix elements:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

print("\n" + "=" * 50)
print("Example 4: Pattern - Right Triangle")
print("=" * 50)

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "=" * 50)
print("Example 5: Pattern - Number Triangle")
print("=" * 50)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "=" * 50)
print("Example 6: Nested Loop - Finding Pairs")
print("=" * 50)

print("All pairs from two lists:")
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

for num in list1:
    for letter in list2:
        print(f"({num}, {letter})", end=" ")
    print()

print("\n" + "=" * 50)
print("Example 7: Breaking Nested Loop")
print("=" * 50)

found = False
for i in range(1, 6):
    for j in range(1, 6):
        if i * j > 10:
            print(f"Product {i} × {j} = {i*j} exceeded 10!")
            found = True
            break
    if found:
        break
