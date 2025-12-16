import matplotlib.pyplot as plt
import numpy as np

# 6. Multiple Lines on One Plot
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='Sin(x)', color='blue', linestyle='--')
plt.plot(x, y2, label='Cos(x)', color='red', linestyle='-.')
plt.title("Sine and Cosine Waves")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.legend()
plt.grid(True)
plt.show()
