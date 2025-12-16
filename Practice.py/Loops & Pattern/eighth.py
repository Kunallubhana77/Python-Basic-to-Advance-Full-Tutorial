# Count how many digits are in a number (no string conversion)

number = 987654
count = 0
temp = number

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print(f"Number: {number}")
print(f"Number of digits: {count}")
