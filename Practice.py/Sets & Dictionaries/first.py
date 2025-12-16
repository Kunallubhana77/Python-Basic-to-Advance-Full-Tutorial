# Input two sets and print union, intersection, and difference

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("Set 1:", set1)
print("Set 2:", set2)

# Union
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference (set1 - set2)
difference_set = set1.difference(set2)
print("Difference (Set 1 - Set 2):", difference_set)
