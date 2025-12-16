numbers = []
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

numbers.sort()
print(f"Second largest number: {numbers[-2]}")


# i means index eg i = 0,1,2,3,4,5,6,7,8,9  

