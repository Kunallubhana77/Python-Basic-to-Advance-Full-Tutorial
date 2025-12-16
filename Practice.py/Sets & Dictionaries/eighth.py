# Count how many unique values exist across dictionary items

my_dict = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}
print("Dictionary:", my_dict)

# Using set to find unique values
unique_values = set(my_dict.values())
count = len(unique_values)

print("Unique Values:", unique_values)
print("Count of Unique Values:", count)
