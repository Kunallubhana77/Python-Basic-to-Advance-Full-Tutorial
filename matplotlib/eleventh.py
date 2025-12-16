import matplotlib.pyplot as plt
import numpy as np

# 11. Heatmap
data = np.random.rand(10, 10)

plt.figure(figsize=(8, 6))
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar(label='Intensity')
plt.title("Heatmap")
plt.show()
