# Given a tuple of numbers, print all numbers greater than 50

my_tuple = (10, 55, 30, 75, 45, 60, 90, 20)

print("Original Tuple:", my_tuple)
print("Numbers greater than 50:")

for num in my_tuple:
    if num > 50:
        print(num)
