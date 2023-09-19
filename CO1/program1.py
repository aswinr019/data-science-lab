# Write a python program to reverse a number and alos find the sum of the digits.
# Prompt for user input


number = int(input("Enter a number: "))
copy = number
reverse = 0
sum = 0


while(number > 0):
    sum = sum + number % 10
    reverse = ( reverse * 10 )+ number % 10
    number =int( number / 10 )

print("Number: ",copy)
print("Reverse of number: ",reverse)
print("Sum of digits: ",sum)