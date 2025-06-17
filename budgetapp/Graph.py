import numpy as np
import matplotlib.pyplot as plt

years = [2006 + x for x in range(16)]
weights = [80, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97]

plt.plot(years, weights, c="g", lw=3, linestyle="--", marker="o", markersize=10, label="Weight")
plt.show()