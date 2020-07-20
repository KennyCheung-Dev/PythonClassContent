import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Warmup Question
# The sniper shoots a bullet vertically upward.
# Assuming that the initial velocity of the bullet is v0 = 800m/w
# the accelration of gravity is 9.8 m/s/s
# Draw the curve of the velocity within 150s after the bull4t is fired
# regardless of the velocity direction

# v0 = 800
# gravity = -9.8
#
# # x = np.linspace(0, 150) #but if we don't need as careful handling
# of start and end point as inspace, we can use arange
# t = np.arange(150)
# dy = v0 + gravity * t
# v = abs(dy)
# plt.plot(t, v)
#
# plt.show()

# ----------------------------------------------------------------------------------
# Fable of the tortoise and the hare
# A turtle is racing with the hare,
# Hare is so confident that it will win, he slept in the middle of the race
# At the end, turtle won the race

# t = np.arange(0, 120, 0.5)
# # Rabbit runs at 15 to 20 m/s
# rabbit = np.piecewise(t,
#                       [t < 10, t > 110],
#                       [lambda x : 15 * x, lambda x : 20 * (x - 110) + 150, lambda x : 150])
# tortoise = 3 * t  # tortoise speed is slow, 3 m/s
# plt.plot(t, tortoise, label='tortoise')
# plt.plot(t, rabbit, label='rabbit')
# plt.title('Race')
# plt.xlabel('time')
# plt.ylabel('meters')
# plt.legend()
# plt.show()

# ----------------------------------------------------------------------------------

# In-Class: Practice the piecewise function
# Try a different range, t < 50, t > 70
# speed = 0 at t < 50,
# speed = 7 at 50 < t < 70,
# speed = 11 at t > 70

# t = np.arange(0, 120, 0.5)
# # Rabbit runs at 15 to 20 m/s
# rabbit = np.piecewise(t,
#                       [t < 50, t > 70],
#                       [lambda x : 0, lambda x : 11 * (x - 70) + 140, lambda x : 7 * (x - 50)])
# tortoise = 3 * t  # tortoise speed is slow, 3 m/s
# plt.plot(t, tortoise, label='tortoise')
# plt.plot(t, rabbit, label='rabbit')
# plt.title('Race')
# plt.xlabel('time')
# plt.ylabel('meters')
# plt.legend()
# plt.show()

# ----------------------------------------------------------------------------------

# Let's change the font!

# t = np.arange(0, 120, 0.5)
# # Rabbit runs at 15 to 20 m/s
# rabbit = np.piecewise(t,
#                       [t < 50, t > 70],
#                       [lambda x : 0, lambda x : 11 * (x - 70) + 140, lambda x : 7 * (x - 50)])
# tortoise = 3 * t  # tortoise speed is slow, 3 m/s
# plt.plot(t, tortoise, label='tortoise')
# plt.plot(t, rabbit, label='rabbit')
# plt.title('Race', fontproperties = 'Press Start 2P', fontsize = 15)
# plt.xlabel('time', fontproperties = 'Press Start 2P', fontsize = 11)
# plt.ylabel('meters', fontproperties = 'Press Start 2P', fontsize = 11)
# # gameFont = fm.FontProperties(fname = r'/Users/kenny/Library/Fonts/PressStart2P-Regular.ttf')
# gameFont = fm.FontProperties(fname = r'PressStart2P-Regular.ttf')
# plt.legend(prop = gameFont)
# plt.show()

# ----------------------------------------------------------------------------------

gameFont = fm.FontProperties(fname = r'PressStart2P-Regular.ttf')

plt.bar([1, 3, 5, 7, 9], [5, 4, 8, 12, 7], label='Graph 1')
plt.bar([2, 4, 6, 8, 10], [4, 6, 8, 13, 15], label='Graph 2')

# params

# x: x-axis
# y: height
# width: default-0.8
# bottom: default-0
# align: center/edge

plt.legend()
plt.xlabel('number')
plt.ylabel('value')

plt.title(u'example', FontProperties= gameFont)

plt.show()
# ----------------------------------------------------------------------------------

