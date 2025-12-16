# Remove a key-value pair from a dictionary

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print("Original Dictionary:", my_dict)

# Remove key 'c'
key_to_remove = 'c'
if key_to_remove in my_dict:
    removed_value = my_dict.pop(key_to_remove)
    print(f"Removed key '{key_to_remove}' with value {removed_value}")
else:
    print(f"Key '{key_to_remove}' not found")

print("Dictionary after removal:", my_dict)
