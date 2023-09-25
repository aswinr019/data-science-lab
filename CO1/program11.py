# Find the number of occurrences of a sequence in a NumPy array
# Eg: Arr = [[2,8,9,4],
# [9,4,9,4],
# [4,5,9,7],
# [2,9,4,3]]
# and the seq = [9,4] then output is 4.

import numpy as np

array = np.array([[2,8,9,4],[9,4,9,4],[4,5,9,7],[2,9,4,3],[9,4,9,3]])

sequence = np.array([9,3])

matching_indices = np.where(np.in1d(array, sequence))[0]

count = (len(matching_indices) / len(sequence)) 

print("Array elements: ",array)
print("Sequence to find: ",sequence)
print("Number of occurrences:", count)
