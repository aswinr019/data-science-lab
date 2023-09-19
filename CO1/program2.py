# Write a python program to find the number off uppercase and lowercase letters in a given text.

text = input("Enter a text: ")

upper_case_count = lower_case_count = 0

for char in text: 
    if(char.isupper()):
        upper_case_count+= 1
    else:
        lower_case_count+=1
        
print("Given text: ",text)
print("Number of uppercase characters in given text: ",upper_case_count)
print("Number of lowercase characters in given text: ",lower_case_count)
