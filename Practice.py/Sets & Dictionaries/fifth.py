# Convert two lists (keys, values) into a dictionary

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

# Using zip and dict
my_dict = dict(zip(keys, values))

print("Keys:", keys)
print("Values:", values)
print("Converted Dictionary:", my_dict)
