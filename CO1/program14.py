# Find indices of elements equal to zero in a NumPy array


import numpy as np

numbers = []

n = int(input("How many numbers ? "))

print("Enter the numbers: ")

for i in range(0,n):
    number = int(input())
    numbers.append(number)

array = np.array(numbers)

zero_indicies = []

for i in range(len(array)): 
    if(array[i] == 0):
        zero_indicies.append(i)

print(f"Array elements: {array}")
print(f"Indecies of zero elements: {zero_indicies}")
