# Calculate the determinant and inverse of a square matrix using numpy functions.


import numpy as np

dimension = int(input("Enter the dimension of the square matrix: "))

sm = []

for i in range(dimension):
    row = []
    for j in range(dimension):
        number = int(input(f"Enter element { i +1 } - { j + 1 } : "))
        row.append(number)
    sm.append(row)

print(f"Matrix elements: {sm}")
print(f"Inverse of the matrix: {sm.linalg.inv(sm)}")
print(f"Determinant of the matrix: {sm.linalg.det(sm)}")
