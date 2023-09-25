# Given two matrices A and B, write a program to find the product of A and BT.

import numpy as np

matrix1 = []
matrix2 = []

n = int(input("Enter the number of row/coluns ( square matrix) ? "))

print(f"Enter {n*n} elements : ")

for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix1.append(row)

n = int(input("Enter the number of row/coluns ( square matrix) ? "))

print(f"Enter {n*n} elements : ")

for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
        row.append(element)
    matrix2.append(row)


print(f"Matrix one : {matrix1}")
print(f"Matrix two : {matrix2}")
mat1 = np.array(matrix1)
mat2 = np.array(matrix2)
print(f"Transpose of matrix two : {mat1.T}")

product = np.dot(matrix1,mat2.T)

print(f"Product of matrix one and transpose of matrix two : {product}")
