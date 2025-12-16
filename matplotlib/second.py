import matplotlib.pyplot as plt

# 2. Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

plt.figure(figsize=(8, 5))
plt.scatter(x, y, c='red', marker='x', label='Data Points')
plt.title("Simple Scatter Plot")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.legend()
plt.show()
