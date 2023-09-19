# Write a python program to replace vowels with '*' in the given text.

text = input("Enter a text: ")

def replace_with_star(string):
    
    for char in string:
        if( char.lower() in ('a','e','i','o','u') ):
            string = string.replace(char,'*')
    return string

replaced = replace_with_star(text)

print("Before reversing: ",text)
print("After replasing: ",replaced)