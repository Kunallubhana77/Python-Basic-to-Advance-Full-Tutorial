# Break and Continue Statements

print("=" * 50)
print("Example 1: Break Statement")
print("=" * 50)

print("Breaking out of a loop when value is 5:")
for i in range(1, 10):
    if i == 5:
        print(f"Found {i}! Breaking...")
        break
    print(i)

print("\n" + "=" * 50)
print("Example 2: Continue Statement")
print("=" * 50)

print("Skip printing even numbers:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

print("\n" + "=" * 50)
print("Example 3: Break in While Loop")
print("=" * 50)

count = 0
while count < 10:
    count += 1
    if count == 6:
        print("Reached 6, breaking!")
        break
    print(f"Count: {count}")

print("\n" + "=" * 50)
print("Example 4: Continue in While Loop")
print("=" * 50)

num = 0
while num < 10:
    num += 1
    if num % 3 == 0:
        continue  # Skip multiples of 3
    print(num)

print("\n" + "=" * 50)
print("Example 5: Break in Nested Loop")
print("=" * 50)

print("Breaking out of nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            print(f"Breaking inner loop at i={i}, j={j}")
            break
        print(f"i={i}, j={j}")

print("\n" + "=" * 50)
print("Example 6: Search and Break")
print("=" * 50)

numbers = [10, 25, 30, 45, 50, 60]
search_num = 45

print(f"Searching for {search_num} in the list:")
for index, num in enumerate(numbers):
    print(f"Checking index {index}: {num}")
    if num == search_num:
        print(f"✓ Found {search_num} at index {index}!")
        break
else:
    print(f"✗ {search_num} not found in the list")

print("\n" + "=" * 50)
print("Example 7: Continue with String")
print("=" * 50)

text = "Python Programming"
print("Printing only consonants:")
vowels = "aeiouAEIOU"

for char in text:
    if char in vowels or char == " ":
        continue
    print(char, end="")
print()  # New line
