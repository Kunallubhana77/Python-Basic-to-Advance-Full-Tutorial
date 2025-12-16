import matplotlib.pyplot as plt
import numpy as np

# 9. Area Plot (Fill Between)
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, color='black')
plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.title("Area Plot (Fill Between)")
plt.xlabel("X")
plt.ylabel("Sin(X)")
plt.show()
