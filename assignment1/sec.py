# Question 9

# Assign an integer
value = 42
print(value, "->", type(value))

# Reassign a string
value = "Hello, world!"
print(value, "->", type(value))

# Reassign a list
value = [1, 2, 3]
print(value, "->", type(value))

# Reassign a dictionary
value = {"key": "value"}
print(value, "->", type(value))

# Reassign a function
def greet():
    return "Hi!"

value = greet
print(value, "->", type(value))
print("Function call result:", value())