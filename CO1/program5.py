# Write a Python program which takes a positive integer n as input and
# finds the sum of cubes all positive even numbers less than or equal to
# the number.

import math 


sum = 0

number = int(input("Enter a number: "))

for num in range(2,(number+1),2):
    cube = int(math.pow(num,3))
    sum = sum + cube

print(f"Sum of cubes of all positive even numbers upto n : {sum}");