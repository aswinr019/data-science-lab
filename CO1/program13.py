# Calculate the sum of the diagonal elements of a NumPy array

import numpy as np

mat = []

n = int(input("Enter the number of row/coluns ( square matrix) ? "))

for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    mat.append(row)

matrix = np.array(mat)

print("Array elements : ", matrix)
print("Sum of diagonal elements : ", np.trace(matrix))
