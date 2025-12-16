import matplotlib.pyplot as plt
import numpy as np

# 15. Polar Plot
r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

plt.figure(figsize=(8, 8))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_rmax(2)
ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Polar Plot", va='bottom')
plt.show()
