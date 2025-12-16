import matplotlib.pyplot as plt

# 3. Bar Chart
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]

plt.figure(figsize=(8, 5))
plt.bar(categories, values, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.title("Categorical Data Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()
