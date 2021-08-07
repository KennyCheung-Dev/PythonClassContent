import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

myFont = fm.FontProperties(fname =r'PressStart2P-Regular.ttf')


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
# plt.title('Race', FontProperties=myFont)
# plt.xlabel('time', FontProperties=myFont)
# plt.ylabel('meters', FontProperties=myFont)
# plt.legend(prop=myFont)
# plt.show()

#-------------------------------------------------------------------------


# give data
x = list(range(1978, 2018))
y_recruit = list(reversed(
[80.6103, 66.7064, 64.5055, 62.1323, 61.1381, 58.9673, 56.0168, 53.8177, 51.0953, 44.6422, 41.8612, 39.7925, 36.4831, 32.6286, 26.8925, 20.2611, 16.5197, 12.8484, 9.2225, 7.2508, 6.3749, 5.9398, 5.1053, 5.0864, 4.2145, 3.3439, 2.9679, 2.9649, 2.8569, 3.5645, 3.9017, 4.131, 4.6871, 2.3181, 1.5642, 1.108, 0.9363, 0.3616, 0.811, 1.0708]))
y_graduate = list(reversed(
[57.8045, 56.3938, 55.1522, 53.5863, 51.3626, 48.6455, 42.9994, 38.36, 37.1273, 34.4825, 31.1839, 25.5902, 18.9728,
15.0777, 11.1091, 8.0841, 6.7809, 5.8767, 5.467, 4.7077, 4.6539, 3.9652, 3.1877, 2.8047, 2.8214, 2.5692, 3.2537, 3.544, 3.7232, 4.0838, 2.7603, 1.695, 1.7004, 0.2756, 0.4497, 0.4058, 1.1669, 0.0476, 0.014, 0.0009]))

# set size, dpi, dots per inch, or pixel per inch
plt.figure(figsize=(10, 6.16), dpi=100)

plt.xticks(x[::2], rotation=45)

#draw first line:
plt.plot(x, y_recruit, label="enrolled")

#Draw second line:
plt.plot(x, y_graduate,
         color = "orange",
         linewidth=3,
         linestyle="-",
         label="graduated")

plt.grid(alpha=0.5)

plt.xlabel("year", fontproperties=myFont, fontsize=12)
plt.ylabel("number", fontproperties=myFont, fontsize=12)

plt.title("Title", fontproperties=myFont, fontsize=18)

ax = plt.gca()
ax.grid(True)

#Legend
plt.legend(prop=myFont, fontsize=12)

plt.show()