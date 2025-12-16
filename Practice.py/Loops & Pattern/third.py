# Sum of digits of a number using a loop

number = 12345
temp = number
total_sum = 0

while temp > 0:
    digit = temp % 10
    total_sum += digit
    temp //= 10

print(f"Number: {number}")
print(f"Sum of digits: {total_sum}")
