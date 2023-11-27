# Create two NumPy arrays of the same shape and perform element-wise
# addition, subtraction, multiplication, and division operations on them.

import numpy as np

number = int(input("Enter the number of elements : "))

list1 = []
list2 = []

for i in range(number):
    n = int(input(f"Enter the element { i + 1 } of first list: "))
    list1.append(n)

for j in range(number):
    n = int(input(f"Enter the element  { j + 1 } of second list: "))
    list2.append(n)

array1 = np.array(list1)
array2 = np.array(list2)

addition_result = np.add(array1, array2)

subtraction_result = np.subtract(array1, array2)

multiplication_result = np.multiply(array1, array2)

division_result = np.divide(array1, array2)

print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise addition:", addition_result)
print("Element-wise subtraction:", subtraction_result)
print("Element-wise multiplication:", multiplication_result)
print("Element-wise division:", division_result)
