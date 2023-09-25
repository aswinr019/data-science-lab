# Calculate the Euclidean distance using NumPy

import numpy as np

point1 = np.array([1, 2])
point2 = np.array([4, 6])

distance = np.linalg.norm(point2 - point1)

print("Euclidean distance:", distance)