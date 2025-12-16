# Python Assignment Operators

print("=" * 50)
print("ASSIGNMENT OPERATORS")
print("=" * 50)

# Simple Assignment
x = 10
print(f"x = 10 → x = {x}")

# Addition Assignment
x += 5  # x = x + 5
print(f"x += 5 → x = {x}")

# Subtraction Assignment
x -= 3  # x = x - 3
print(f"x -= 3 → x = {x}")

# Multiplication Assignment
x *= 2  # x = x * 2
print(f"x *= 2 → x = {x}")

# Division Assignment
x /= 4  # x = x / 4
print(f"x /= 4 → x = {x}")

# Floor Division Assignment
x = 20
x //= 3  # x = x // 3
print(f"x //= 3 → x = {x}")

# Modulus Assignment
x %= 4  # x = x % 4
print(f"x %= 4 → x = {x}")

# Exponentiation Assignment
x **= 3  # x = x ** 3
print(f"x **= 3 → x = {x}")

# Bitwise AND Assignment
x = 12  # Binary: 1100
x &= 10  # Binary: 1010, Result: 1000 = 8
print(f"x &= 10 → x = {x}")

# Bitwise OR Assignment
x |= 5  # Binary: 1000 | 0101 = 1101 = 13
print(f"x |= 5 → x = {x}")

# Bitwise XOR Assignment
x ^= 3  # Binary: 1101 ^ 0011 = 1110 = 14
print(f"x ^= 3 → x = {x}")

# Right Shift Assignment
x >>= 2  # Shift right by 2 positions
print(f"x >>= 2 → x = {x}")

# Left Shift Assignment
x <<= 1  # Shift left by 1 position
print(f"x <<= 1 → x = {x}")
