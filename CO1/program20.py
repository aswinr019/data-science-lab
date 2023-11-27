# Write a program that uses matplotlib to create a simple line plot
# of a set of data points.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = x * 2

plt.plot(x, y)
plt.show()
