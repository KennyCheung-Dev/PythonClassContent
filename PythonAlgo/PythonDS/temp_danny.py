import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


# Fable of the tortoise and the hare
# A turtle is racing with the hare,
# Hare is so confident that it will win, he slept in the middle of the race
# At the end, turtle won the race!

# t = np.arange(0, 120, 0.5)
# # Rabbit runs at 15 to 20 m/s
# # Tortoise is running 3 m/s
# tortoise = 3 * t
#
# rabbit = np.piecewise(t,
#                       [t < 10, t > 110],
#                       [lambda x : 15 * x, lambda x : 20 * (x - 110) + 150, lambda x : 150]
#                       )
#
# plt.plot(t, tortoise, label='tortoise')
# plt.plot(t, rabbit, label='rabbit')
# plt.title('Race')
# plt.xlabel('time')
# plt.ylabel('meters')
# plt.legend()
# plt.show()

#-------------------------------------------------------------------------

t = np.arange(0, 120, 0.5)
# Rabbit runs at 15 to 20 m/s
# Tortoise is running 3 m/s
tortoise = 3 * t

rabbit = np.piecewise(t,
                      [t < 10, t > 110],
                      [lambda x : 15 * x, lambda x : 20 * (x - 110) + 150, lambda x : 150]
                      )

plt.plot(t, tortoise, label='tortoise')
plt.plot(t, rabbit, label='rabbit')
plt.title('Race', )
plt.xlabel('time')
plt.ylabel('meters')
plt.legend()
plt.show()
