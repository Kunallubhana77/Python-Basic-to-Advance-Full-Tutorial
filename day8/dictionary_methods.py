# Dictionary Methods in Python

print("=" * 50)
print("DICTIONARY METHODS")
print("=" * 50)

# Sample dictionary
fruits = {"apple": 10, "banana": 15, "cherry": 8}
print(f"Original dictionary: {fruits}")

print("\n" + "=" * 50)
print("1. get() - Get value with default")
print("=" * 50)

print(f"Apple count: {fruits.get('apple')}")
print(f"Mango count: {fruits.get('mango', 0)}")  # Default value

print("\n" + "=" * 50)
print("2. keys() - Get all keys")
print("=" * 50)

keys = fruits.keys()
print(f"Keys: {list(keys)}")

print("\n" + "=" * 50)
print("3. values() - Get all values")
print("=" * 50)

values = fruits.values()
print(f"Values: {list(values)}")

print("\n" + "=" * 50)
print("4. items() - Get all key-value pairs")
print("=" * 50)

items = fruits.items()
print(f"Items: {list(items)}")

print("\n" + "=" * 50)
print("5. update() - Update dictionary")
print("=" * 50)

fruits.update({"mango": 20, "orange": 12})
print(f"After update: {fruits}")

print("\n" + "=" * 50)
print("6. pop() - Remove and return value")
print("=" * 50)

removed = fruits.pop("banana")
print(f"Removed: {removed}")
print(f"After pop: {fruits}")

print("\n" + "=" * 50)
print("7. popitem() - Remove last item")
print("=" * 50)

last_item = fruits.popitem()
print(f"Last item removed: {last_item}")
print(f"After popitem: {fruits}")

print("\n" + "=" * 50)
print("8. setdefault() - Get or set default")
print("=" * 50)

fruits = {"apple": 10, "banana": 15}
print(f"Get apple: {fruits.setdefault('apple', 0)}")
print(f"Get mango (sets default): {fruits.setdefault('mango', 5)}")
print(f"After setdefault: {fruits}")

print("\n" + "=" * 50)
print("9. copy() - Create shallow copy")
print("=" * 50)

fruits_copy = fruits.copy()
print(f"Original: {fruits}")
print(f"Copy: {fruits_copy}")

fruits_copy["grape"] = 25
print(f"After modifying copy:")
print(f"  Original: {fruits}")
print(f"  Copy: {fruits_copy}")

print("\n" + "=" * 50)
print("10. clear() - Remove all items")
print("=" * 50)

temp = {"a": 1, "b": 2, "c": 3}
print(f"Before clear: {temp}")
temp.clear()
print(f"After clear: {temp}")

print("\n" + "=" * 50)
print("11. fromkeys() - Create dict from sequence")
print("=" * 50)

keys = ["name", "age", "city"]
default_dict = dict.fromkeys(keys, "unknown")
print(f"Dict from keys: {default_dict}")

numbers_dict = dict.fromkeys(range(1, 6), 0)
print(f"Dict with number keys: {numbers_dict}")
