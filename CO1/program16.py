# Create two NumPy arrays of the same shape and perform element-wise
# addition, subtraction, multiplication, and division operations on them.

import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

addition_result = array1 + array2

subtraction_result = array1 - array2

multiplication_result = array1 * array2

division_result = array1 / array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Element-wise addition:", addition_result)
print("Element-wise subtraction:", subtraction_result)
print("Element-wise multiplication:", multiplication_result)
print("Element-wise division:", division_result)