# Find the index of a value in a tuple (handle value not present)

my_tuple = (10, 20, 30, 40, 50)

def find_index(tup, value):
    try:
        index = tup.index(value)
        print(f"Value {value} found at index: {index}")
    except ValueError:
        print(f"Value {value} not found in the tuple.")

print("Tuple:", my_tuple)

# Case 1: Value exists
find_index(my_tuple, 30)

# Case 2: Value does not exist
find_index(my_tuple, 60)
