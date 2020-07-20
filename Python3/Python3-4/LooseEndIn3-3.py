import matplotlib.pyplot as plt
from matplotlib import font_manager

labels = ("red", "green", "blue", "yellow", "gray")
colors = ("red", "green", "blue", "yellow", "gray")
fracs = [10, 20, 30 ,20, 20]
plt.pie(fracs, labels=labels, colors=colors, autopct='%1.0f%%')
plt.show()

