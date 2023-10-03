# Find the k smallest values of a NumPy array

import numpy as np


numbers = []

n = int(input("How many numbers ? "))

print("Enter the numbers: ")

for i in range(n):
    number = int(input())
    numbers.append(number)

k = int(input("Enter the number of smallest elements: "))

array = np.array(numbers)

sorted = np.sort(array)
smallest = sorted[:k]
print(f"Array elements are: {array} ")
print(f"The k smallest elements are : {smallest}")
