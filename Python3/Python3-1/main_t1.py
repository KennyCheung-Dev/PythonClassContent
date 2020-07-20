import numpy as np
import matplotlib.pyplot as plt

#Declare the x data range
x = np.linspace(-3, 3, 50)
# Declare the equation for our graph, value of y
y = x**2

plt.xlim(0, 3) # Set x-axis range
plt.xticks([0, 1, 2, 3]) # Set x-axis scale
plt.ylim(0, 9.0) # Set y-axis range
plt.plot(x,y) # Draw the image

ax = plt.gca() #Get Current Axes
ax.set_aspect(0.3)  # Set aspect ratio to equal between x and y
ax.grid(True)

plt.show()

#In-Class
#Draw This Graph:
# y = 9 - x**2  on the interval of [-3, 3]

#Homework
#1. x**2 - (y**2 / 9) = 1  in x = [-10, 10]

#2. x**2 / 4 + (y**2/25) = 1  in x = [-3, 3]
