# Write a Python program that creates a NumPy array from a list of
# numbers and calculates the mean, median, and standard deviation of
# the elements.


import numpy as np

numbers = []

n = int(input("How many numbers ? "))

print("Enter the numbers: ")

for i in range(0,n):
    number = int(input())
    numbers.append(number)

array = np.array(numbers)

print("Array elements : ",array)
print("Mean of elements : ",np.mean(array))
print("Meadian of elements : ",np.median(array))
print("Standard deviation of elements : ",np.std(array))

