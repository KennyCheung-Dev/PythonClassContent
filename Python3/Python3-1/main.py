import numpy as np
import matplotlib.pyplot as plt
# Using as makes our code easier
# You wouldn't have to type "numpy" or "matplotlib.pyplot" everytime

# x = np.linspace(-3, 3, 100)  # Create Data in X , range and sample rate
# y = 9 - x**2  # Create function in Y
#
# plt.xlim(-3, 3)  # Set x-axis range
# plt.xticks(list(range(-3, 4))) # Set x-axis scale
# plt.ylim(0.0, 9.0)# Set y-axis range
# plt.plot(x,y)  # Draw the image
#
# ax = plt.gca() # Get Current Axes, used to set style
# ax.set_aspect("equal")   # Set Aspect ratio equal
# ax.grid(True)  # Show grid
#
# plt.show()  # Show the result

# --------------------------------------------------------

# Let's try a more complex function!
# y = log2 x

# x = np.linspace(1, 10, 100)
# y = np.log2(x)
#
# plt.xlim(1, 10)
# plt.xticks(list(range(1, 11)))
# print(list(range(1,11)))
# plt.ylim(0, 5)
# plt.plot(x, y)
#
# ax = plt.gca()  #Get Current Axes
# ax.set_aspect("equal")
# ax.grid(True)
#
# plt.show()
#
# print(2**1.6) # = 3

# --------------------------------------------------------

# Fun In-Class Exercise!
# Draw:
# y = np.sqrt(x+3) + 1/(x+2) in [-1.9, 5]
# Tips: np.sqrt(x+3) + 1/(x+2)

# x = np.linspace(-1.9, 5, 50)
# y = np.sqrt(x+3) + 1/(x+2)
#
# plt.xlim(-1.9, 5)
# plt.xticks(list(range(-2, 6)))
# plt.ylim(0, 12)
# plt.plot(x, y)
#
# ax = plt.gca()  #Get Current Axes
# ax.set_aspect("equal")
# ax.grid(True)
#
# plt.show()


# --------------------------------------------------------
# Homework:
# 1. What are the two Python Modules used in today's lesson and
# what did we use them for?

# 2. What code do you write to generate a function
# in the range [-5, 5] with 100 data points?

# 3. What code do you write to plot a function
# (assuming y and x have both been initialized)
# on a graph where x is in the range[-5. 5] and y is in the range [0, 20]?

# 4. What code do you write to set the graph aspect ratio to equal and
# display grid lines?

# 5. What code do you write to show the plot after done setting up?

#In-Class Exercise

# x**2 - y**2 / 9  = 1  in x = [-10, 10]     y limit: [-1, 32]

# x**2 / 4 + y**2/25 = 1 in x = [-3, 3]      y limit: [1, 6]

# --------------------------------------------------------
# Q:
# x**2 - y**2/9  = 1
# x**2 = 1 + y**2/9
# x**2 - 1 = y**2/9
# 9 * x**2 - 9 = y**2
# y = sqrt(9 * x**2 - 9)

# x = np.linspace(-10, 10, 50)
# y = np.sqrt(9 * x**2 - 9)
#
# plt.xlim(-10, 10)
# plt.xticks(list(range(-10, 11)))
# plt.ylim(-1, 32)
# plt.plot(x, y)
#
# ax = plt.gca()  #Get Current Axes
# ax.set_aspect("equal")
# ax.grid(True)
#
# plt.show()

# --------------------------------------------------------
# Q:
# (x**2 / 4) + (y**2/25) = 1
# y**2 / 25 = 1 - (x**2 / 4)
# y**2 = 25 - (25 * x**2 / 4)
# y**2 = 25 - (6.25 * x**2)
# y = sqrt(25 - (6.25 * x**2))

x = np.linspace(-3, 3, 50)
y = np.sqrt(25 - 6.25 * x**2)

plt.xlim(-3, 3)
plt.xticks(list(range(-3, 4)))
plt.ylim(1, 6)
plt.plot(x, y)

ax = plt.gca()  #Get Current Axes
ax.set_aspect("equal")
ax.grid(True)

plt.show()

# --------------------------------------------------------