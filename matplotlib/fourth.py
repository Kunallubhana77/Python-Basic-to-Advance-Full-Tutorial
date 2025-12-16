import matplotlib.pyplot as plt
import numpy as np

# 4. Histogram
data = np.random.normal(170, 10, 250) # Mean 170, SD 10, 250 data points

plt.figure(figsize=(8, 5))
plt.hist(data, bins=15, color='skyblue', edgecolor='black')
plt.title("Histogram of Height Data")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.show()
