# Python Data Types - Comprehensive Examples

# 1. Numeric Types
print("=" * 50)
print("NUMERIC TYPES")
print("=" * 50)

# Integer
age = 25
print(f"Integer: {age}, Type: {type(age)}")

# Float
price = 99.99
print(f"Float: {price}, Type: {type(price)}")

# Complex
complex_num = 3 + 4j
print(f"Complex: {complex_num}, Type: {type(complex_num)}")

# 2. Text Type
print("\n" + "=" * 50)
print("TEXT TYPE")
print("=" * 50)

name = "Python Tutorial"
print(f"String: {name}, Type: {type(name)}")

# 3. Sequence Types
print("\n" + "=" * 50)
print("SEQUENCE TYPES")
print("=" * 50)

# List (mutable)
fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}, Type: {type(fruits)}")

# Tuple (immutable)
coordinates = (10, 20, 30)
print(f"Tuple: {coordinates}, Type: {type(coordinates)}")

# Range
numbers = range(5)
print(f"Range: {list(numbers)}, Type: {type(numbers)}")

# 4. Set Types
print("\n" + "=" * 50)
print("SET TYPES")
print("=" * 50)

# Set (mutable, unique elements)
unique_numbers = {1, 2, 3, 4, 5}
print(f"Set: {unique_numbers}, Type: {type(unique_numbers)}")

# Frozenset (immutable)
frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}, Type: {type(frozen)}")

# 5. Mapping Type
print("\n" + "=" * 50)
print("MAPPING TYPE")
print("=" * 50)

# Dictionary
student = {"name": "John", "age": 20, "grade": "A"}
print(f"Dictionary: {student}, Type: {type(student)}")

# 6. Boolean Type
print("\n" + "=" * 50)
print("BOOLEAN TYPE")
print("=" * 50)

is_active = True
is_deleted = False
print(f"Boolean True: {is_active}, Type: {type(is_active)}")
print(f"Boolean False: {is_deleted}, Type: {type(is_deleted)}")

# 7. None Type
print("\n" + "=" * 50)
print("NONE TYPE")
print("=" * 50)

nothing = None
print(f"None: {nothing}, Type: {type(nothing)}")

# 8. Binary Types
print("\n" + "=" * 50)
print("BINARY TYPES")
print("=" * 50)

# Bytes (immutable)
byte_data = b"Hello"
print(f"Bytes: {byte_data}, Type: {type(byte_data)}")

# Bytearray (mutable)
byte_array = bytearray(b"World")
print(f"Bytearray: {byte_array}, Type: {type(byte_array)}")

# Memoryview
mem_view = memoryview(bytes(5))
print(f"Memoryview: {mem_view}, Type: {type(mem_view)}")


