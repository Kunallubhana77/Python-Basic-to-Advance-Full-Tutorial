# Print a pyramid pattern

rows = 5

for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("*" * (2 * i - 1))
