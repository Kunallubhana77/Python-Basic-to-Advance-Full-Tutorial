import matplotlib.pyplot as plt
import numpy as np

# 10. Box Plot
np.random.seed(10)
data_1 = np.random.normal(100, 10, 200)
data_2 = np.random.normal(90, 20, 200)
data_3 = np.random.normal(80, 30, 200)
data_4 = np.random.normal(70, 40, 200)
data = [data_1, data_2, data_3, data_4]

plt.figure(figsize=(10, 6))
plt.boxplot(data, patch_artist=True, labels=['Data 1', 'Data 2', 'Data 3', 'Data 4'])
plt.title("Box Plot Comparison")
plt.ylabel("Values")
plt.grid(axis='y')
plt.show()
