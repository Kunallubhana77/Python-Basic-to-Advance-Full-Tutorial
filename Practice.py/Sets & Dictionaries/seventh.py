# Find common values between two dictionaries

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'x': 3, 'y': 4, 'z': 5}

print("Dictionary 1:", dict1)
print("Dictionary 2:", dict2)

# Finding common values
common_values = set(dict1.values()) & set(dict2.values())

print("Common Values:", common_values)
