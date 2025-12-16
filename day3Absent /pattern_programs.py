# Pattern Programs in Python

print("=" * 50)
print("Pattern 1: Right Triangle Star Pattern")
print("=" * 50)

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 2: Inverted Right Triangle")
print("=" * 50)

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 3: Pyramid Pattern")
print("=" * 50)

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 4: Number Pattern - Incrementing")
print("=" * 50)

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 5: Number Pattern - Same Number")
print("=" * 50)

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 6: Square Pattern")
print("=" * 50)

size = 5
for i in range(size):
    for j in range(size):
        print("*", end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 7: Hollow Square Pattern")
print("=" * 50)

for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 8: Diamond Pattern")
print("=" * 50)

n = 5
# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("* " * i)

print("\n" + "=" * 50)
print("Pattern 9: Alphabet Pattern")
print("=" * 50)

for i in range(5):
    ch = 65  # ASCII value of 'A'
    for j in range(i + 1):
        print(chr(ch + j), end=" ")
    print()

print("\n" + "=" * 50)
print("Pattern 10: Floyd's Triangle")
print("=" * 50)

num = 1
for i in range(1, 6):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
