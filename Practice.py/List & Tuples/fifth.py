# Convert a list to tuple and tuple back to list

my_list = [1, 2, 3, 4, 5]
print(f"Original List: {my_list}, Type: {type(my_list)}")

# Convert list to tuple
my_tuple = tuple(my_list)
print(f"Converted to Tuple: {my_tuple}, Type: {type(my_tuple)}")

# Convert tuple back to list
my_list_back = list(my_tuple)
print(f"Converted back to List: {my_list_back}, Type: {type(my_list_back)}")
