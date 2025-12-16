# Range Function in Python

print("=" * 50)
print("Example 1: Basic Range")
print("=" * 50)

print("range(5) generates: 0, 1, 2, 3, 4")
for i in range(5):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("Example 2: Range with Start and Stop")
print("=" * 50)

print("range(2, 8) generates: 2, 3, 4, 5, 6, 7")
for i in range(2, 8):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("Example 3: Range with Start, Stop, and Step")
print("=" * 50)

print("range(1, 10, 2) generates odd numbers: 1, 3, 5, 7, 9")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("Example 4: Range with Negative Step (Reverse)")
print("=" * 50)

print("range(10, 0, -1) generates: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("Example 5: Converting Range to List")
print("=" * 50)

numbers = list(range(1, 6))
print(f"list(range(1, 6)) = {numbers}")

print("\n" + "=" * 50)
print("Example 6: Using Range for Indexing")
print("=" * 50)

fruits = ["apple", "banana", "cherry", "mango"]
print("Accessing list elements using range:")
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")

print("\n" + "=" * 50)
print("Example 7: Sum Using Range")
print("=" * 50)

total = sum(range(1, 11))
print(f"Sum of numbers from 1 to 10: {total}")

print("\n" + "=" * 50)
print("Example 8: Range with Large Step")
print("=" * 50)

print("range(0, 100, 20) generates: 0, 20, 40, 60, 80")
for i in range(0, 100, 20):
    print(i, end=" ")
print()

print("\n" + "=" * 50)
print("Example 9: Negative Numbers with Range")
print("=" * 50)

print("range(-5, 5) generates: -5, -4, -3, -2, -1, 0, 1, 2, 3, 4")
for i in range(-5, 5):
    print(i, end=" ")
print()
