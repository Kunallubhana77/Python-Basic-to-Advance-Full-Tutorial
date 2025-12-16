# While Loop Examples

print("=" * 50)
print("Example 1: Simple Counter")
print("=" * 50)

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print("\n" + "=" * 50)
print("Example 2: Sum of Numbers")
print("=" * 50)

total = 0
num = 1
while num <= 10:
    total += num
    num += 1
print(f"Sum of numbers 1 to 10: {total}")

print("\n" + "=" * 50)
print("Example 3: Countdown Timer")
print("=" * 50)

countdown = 5
while countdown > 0:
    print(f"Time remaining: {countdown} seconds")
    countdown -= 1
print("Time's up!")

print("\n" + "=" * 50)
print("Example 4: While with Break")
print("=" * 50)

i = 1
while True:
    print(f"Iteration: {i}")
    if i == 5:
        print("Breaking the loop at 5")
        break
    i += 1

print("\n" + "=" * 50)
print("Example 5: While with Continue")
print("=" * 50)

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {number}")

print("\n" + "=" * 50)
print("Example 6: Factorial Calculator")
print("=" * 50)

n = 5
factorial = 1
temp = n

while temp > 0:
    factorial *= temp
    temp -= 1
    
print(f"Factorial of {n} is: {factorial}")

print("\n" + "=" * 50)
print("Example 7: Reverse a Number")
print("=" * 50)

original = 12345
reversed_num = 0

while original > 0:
    digit = original % 10
    reversed_num = reversed_num * 10 + digit
    original //= 10

print(f"Reversed number: {reversed_num}")

print("\n" + "=" * 50)
print("Example 8: Password Validator (Demo)")
print("=" * 50)

attempts = 0
max_attempts = 3
correct_password = "python123"

# In a real scenario, use input(). This is demo version
test_password = "wrong"

while attempts < max_attempts:
    attempts += 1
    print(f"Attempt {attempts}/{max_attempts}")
    
    if test_password == correct_password:
        print("✓ Login successful!")
        break
    else:
        if attempts < max_attempts:
            print("✗ Wrong password. Try again.")
        else:
            print("✗ Account locked. Too many failed attempts.")
