# While Loop Examples in Python

print("=" * 50)
print("Example 1: Basic While Loop")
print("=" * 50)

count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

print("\n" + "=" * 50)
print("Example 2: User Input Simulation (While Loop)")
print("=" * 50)

# Demo version without actual input
attempts = 0
max_attempts = 3
target = 7
guess = 5  # Simulated guess

while attempts < max_attempts and guess != target:
    attempts += 1
    print(f"Attempt {attempts}: Guessed {guess}")
    if guess != target:
        guess += 1

if guess == target:
    print(f"Correct! You guessed it in {attempts} attempt(s)")
else:
    print(f"Out of attempts! The number was {target}")

print("\n" + "=" * 50)
print("Example 3: Infinite Loop with Break")
print("=" * 50)

counter = 1
while True:
    print(f"Loop iteration: {counter}")
    if counter == 5:
        print("Breaking out of infinite loop")
        break
    counter += 1

print("\n" + "=" * 50)
print("Example 4: While Loop with Else")
print("=" * 50)

n = 1
while n <= 3:
    print(f"n = {n}")
    n += 1
else:
    print("While loop completed normally")

print("\n" + "=" * 50)
print("Example 5: Sum Until Condition")
print("=" * 50)

sum_total = 0
number = 1

while sum_total < 50:
    sum_total += number
    print(f"Adding {number}, Total: {sum_total}")
    number += 1

print(f"Final sum: {sum_total}")
