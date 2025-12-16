# Set Methods in Python

print("=" * 50)
print("SET METHODS")
print("=" * 50)

# Sample sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"set1: {set1}")
print(f"set2: {set2}")

print("\n" + "=" * 50)
print("1. add() - Add single element")
print("=" * 50)

fruits = {"apple", "banana"}
fruits.add("cherry")
print(f"After add('cherry'): {fruits}")

print("\n" + "=" * 50)
print("2. update() - Add multiple elements")
print("=" * 50)

fruits.update(["mango", "orange", "grape"])
print(f"After update: {fruits}")

print("\n" + "=" * 50)
print("3. remove() - Remove element (error if not found)")
print("=" * 50)

fruits.remove("banana")
print(f"After remove('banana'): {fruits}")

print("\n" + "=" * 50)
print("4. discard() - Remove element (no error)")
print("=" * 50)

fruits.discard("kiwi")  # Doesn't exist, no error
print(f"After discard('kiwi'): {fruits}")

print("\n" + "=" * 50)
print("5. pop() - Remove random element")
print("=" * 50)

popped = fruits.pop()
print(f"Popped: {popped}")
print(f"After pop: {fruits}")

print("\n" + "=" * 50)
print("6. clear() - Remove all elements")
print("=" * 50)

temp = {1, 2, 3}
temp.clear()
print(f"After clear: {temp}")

print("\n" + "=" * 50)
print("7. union() - Combine sets")
print("=" * 50)

union_set = set1.union(set2)
print(f"set1.union(set2): {union_set}")

print("\n" + "=" * 50)
print("8. intersection() - Common elements")
print("=" * 50)

inter_set = set1.intersection(set2)
print(f"set1.intersection(set2): {inter_set}")

print("\n" + "=" * 50)
print("9. difference() - Elements in first but not second")
print("=" * 50)

diff_set = set1.difference(set2)
print(f"set1.difference(set2): {diff_set}")

print("\n" + "=" * 50)
print("10. symmetric_difference() - Elements in either, not both")
print("=" * 50)

sym_diff = set1.symmetric_difference(set2)
print(f"set1.symmetric_difference(set2): {sym_diff}")

print("\n" + "=" * 50)
print("11. issubset() - Check if subset")
print("=" * 50)

small_set = {1, 2}
print(f"small_set: {small_set}")
print(f"{small_set}.issubset({set1}): {small_set.issubset(set1)}")

print("\n" + "=" * 50)
print("12. issuperset() - Check if superset")
print("=" * 50)

print(f"{set1}.issuperset({small_set}): {set1.issuperset(small_set)}")

print("\n" + "=" * 50)
print("13. isdisjoint() - Check if no common elements")
print("=" * 50)

set_a = {1, 2, 3}
set_b = {7, 8, 9}
print(f"set_a: {set_a}")
print(f"set_b: {set_b}")
print(f"set_a.isdisjoint(set_b): {set_a.isdisjoint(set_b)}")

print("\n" + "=" * 50)
print("14. copy() - Create shallow copy")
print("=" * 50)

original = {1, 2, 3}
copied = original.copy()
print(f"Original: {original}")
print(f"Copy: {copied}")
