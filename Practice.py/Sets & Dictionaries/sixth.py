# Reverse a dictionary (swap keys & values)

original_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", original_dict)

# Swapping keys and values
reversed_dict = {v: k for k, v in original_dict.items()}

print("Reversed Dictionary:", reversed_dict)
