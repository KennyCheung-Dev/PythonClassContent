import numpy as np
import matplotlib.pyplot as plt

# plot y = x**2  in the interval of [-3, 3]

# Data
x = np.linspace(-3, 3, 100)
# y = (2 * x**2) + (6 * x) + (3)
y = x**2

# Attributes for the plot
plt.xlim(-5, 10)
plt.xticks(list(range(-3, 4)))
plt.ylim(0.0, 9.0)

ax = plt.gca()
ax.set_aspect("equal")
ax.grid(True)

plt.plot(x, y)   #Drawing the plot

plt.show() #Showing the plot

# -----------------------------------------------------------------
#Plot this equation
# y = 2x**2 + 6x + 3 in the interval of [-3, 3]

# -----------------------------------------------------------------

# Homework:
#Q1
# x**2 - y**2 / 9 = 1   in the interval of [-10, 10]
#Q2
# x**2 / 4 + y**2 / 25 = 1     in the interval of [-3, 3]

#Sqrt is done with np.sqrt()








