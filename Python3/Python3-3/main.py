from matplotlib import pyplot as plt
from matplotlib import font_manager

gameFont = font_manager.FontProperties(fname = r'PressStart2P-Regular.ttf')

# give data:
x = list(range(1978, 2018))
y_recruit = list(reversed(
    [
        80.6, 66.7, 64.5, 62.1, 61.1, 58.9, 56.1, 53.8, 51.1, 44.6, 44.1, 41.8, 39.8, 36.4, 32.6, 26.8, 20.2, 16.5, 12.8, 9.2, 7.3, 6.3, 5.9, 5.1, 5.1, 4.2, 3.3, 2.9, 2.9, 2.8, 3.5, 3.9, 4.1, 4.6, 2.3, 1.5, 1.1, 0.9, 0.8, 1.1
    ]
))
y_graduate = list(reversed(
    [
        57.8, 56.3, 55.1, 53.5, 51.3, 48.6, 42.9, 38.3, 37.1, 34.4, 31.1, 25.5, 18.9, 15.1, 11.1, 8.0, 6.7, 5.8, 5.4, 4.7, 4.6, 3.9, 3.1, 2.8, 2.8, 2.5, 3.2, 3.5, 3.7, 4.1, 2.7, 1.7, 1.7, 0.2, 0.4, 1.1, 0.1, 0.1, 0.0, 0.0
    ]
))

#set size, dpi, dots per inch, or pixel per inch
plt.figure(figsize=(10, 6.16), dpi=100)

plt.xticks(x[::2], rotation=45)

#draw first line
plt.plot(x, y_recruit, label="enrolled")

#Draw second line
plt.plot(x, y_graduate,
         color = "orange",
         linewidth=3,
         linestyle="-.",  # Can explore with '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
         label="graduated")

plt.grid(alpha=0.5)

plt.xlabel("year", fontproperties=gameFont, fontsize=12)
plt.ylabel("number", fontproperties=gameFont, fontsize=12)

plt.title("title", fontproperties=gameFont, fontsize=18)

#Another way
ax = plt.gca()
ax.grid(True)

#Legend
# plt.legend(prop=gameFont,fontsize=12)
plt.legend()

#show
plt.show()