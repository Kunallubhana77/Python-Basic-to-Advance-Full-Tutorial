# Sets in Python

print("=" * 50)
print("SET CREATION")
print("=" * 50)

# Creating a set
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Set from list (removes duplicates)
numbers = {1, 2, 3, 2, 1, 4, 5, 4}
print(f"Numbers set (duplicates removed): {numbers}")

# Empty set (must use set(), not {})
empty_set = set()
print(f"Empty set: {empty_set}")

# Set from string
letters = set("hello")
print(f"Letters from 'hello': {letters}")

print("\n" + "=" * 50)
print("SET OPERATIONS")
print("=" * 50)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (all elements from both sets)
union = set1 | set2  # or set1.union(set2)
print(f"Union (set1 | set2): {union}")

# Intersection (common elements)
intersection = set1 & set2  # or set1.intersection(set2)
print(f"Intersection (set1 & set2): {intersection}")

# Difference (elements in set1 but not in set2)
difference = set1 - set2  # or set1.difference(set2)
print(f"Difference (set1 - set2): {difference}")

# Symmetric Difference (elements in either set, but not both)
sym_diff = set1 ^ set2  # or set1.symmetric_difference(set2)
print(f"Symmetric Difference (set1 ^ set2): {sym_diff}")

print("\n" + "=" * 50)
print("ADDING ELEMENTS")
print("=" * 50)

colors = {"red", "green", "blue"}
print(f"Original: {colors}")

# Add single element
colors.add("yellow")
print(f"After add('yellow'): {colors}")

# Update with multiple elements
colors.update(["orange", "purple"])
print(f"After update: {colors}")

print("\n" + "=" * 50)
print("REMOVING ELEMENTS")
print("=" * 50)

numbers = {1, 2, 3, 4, 5}
print(f"Original: {numbers}")

# Remove (raises error if not found)
numbers.remove(3)
print(f"After remove(3): {numbers}")

# Discard (no error if not found)
numbers.discard(10)  # Element doesn't exist
print(f"After discard(10): {numbers}")

# Pop (removes random element)
popped = numbers.pop()
print(f"Popped element: {popped}")
print(f"After pop: {numbers}")

# Clear all elements
temp = {1, 2, 3}
temp.clear()
print(f"After clear: {temp}")

print("\n" + "=" * 50)
print("SET MEMBERSHIP")
print("=" * 50)

fruits = {"apple", "banana", "cherry"}
print(f"Fruits: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")
print(f"'orange' not in fruits: {'orange' not in fruits}")

print("\n" + "=" * 50)
print("SET LENGTH AND ITERATION")
print("=" * 50)

colors = {"red", "green", "blue", "yellow"}
print(f"Set length: {len(colors)}")
print("Iterating through set:")
for color in colors:
    print(f"  - {color}")

print("\n" + "=" * 50)
print("SUBSET AND SUPERSET")
print("=" * 50)

set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}

print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_a is subset of set_b: {set_a.issubset(set_b)}")
print(f"set_b is superset of set_a: {set_b.issuperset(set_a)}")
print(f"Are they disjoint: {set_a.isdisjoint(set_b)}")

print("\n" + "=" * 50)
print("FROZENSET (Immutable Set)")
print("=" * 50)

frozen = frozenset([1, 2, 3, 4, 5])
print(f"Frozenset: {frozen}")
print(f"Type: {type(frozen)}")
# frozen.add(6)  # This would raise an error
