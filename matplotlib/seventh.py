import matplotlib.pyplot as plt

# 7. Subplots (2x2 Grid)
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Top Left
axs[0, 0].plot(x, y, 'tab:blue')
axs[0, 0].set_title('Line Plot')

# Top Right
axs[0, 1].scatter(x, y, color='tab:orange')
axs[0, 1].set_title('Scatter Plot')

# Bottom Left
axs[1, 0].bar(x, y, color='tab:green')
axs[1, 0].set_title('Bar Chart')

# Bottom Right
axs[1, 1].hist(y, bins=5, color='tab:red')
axs[1, 1].set_title('Histogram')

plt.tight_layout()
plt.show()
