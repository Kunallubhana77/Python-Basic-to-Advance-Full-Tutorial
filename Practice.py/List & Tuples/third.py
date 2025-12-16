# Count how many times each item appears in a list

my_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = {}

for item in my_list:
    if item in counts:
        counts[item] += 1
    else:
        counts[item] = 1

print("List:", my_list)
print("Item counts:")
for item, count in counts.items():
    print(f"{item}: {count}")
