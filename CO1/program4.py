# Write a python program to find the value for sin(x) upto n terms using the series

# sin(x) = x / 1! - x ^ 3 / 3! + x ^ 5 / 5! - x ^ 7 / 7! + ...
# where x is in degrees
import math

n = int(input("Enter an upper limit: "))
x = int(input("Enter the variable x: "))

degree = 1
result = 0
turn = True

for i in range(1,n + 1):
    first = math.pow(x,degree)
    second = math.factorial(degree)
    
    if(turn):
        result = result - (first/second)
    else: 
        result = result + (first/second)
    
    degree += 2
    
print("sin(x): ",result)