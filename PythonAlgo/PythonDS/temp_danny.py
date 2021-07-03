import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3, 3, 100)
y = 9 - x**2
plt.xlim(-3, 3)
plt.xticks(list(range(-3, 4)))
plt.ylim(0.0, 9.0)
plt.plot(x, y)
ax = plt.gca()
ax.set_aspect('equal')
ax.grid(True)
plt.show()