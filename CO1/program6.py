# Given is a list of of words, wordlist, and a string, name. Write a Python
# function which takes wordlist and name as input and returns a tuple.
# The first element of the output tuple is the number of words in the
# wordlist which have name as a substring in it. The second element of
# the tuple is a list showing the index at which the name occurs in each of
# the words of the wordlist and a 0 if it doesn’t occur.

def find_words_with_substring(wordlist, name):
    
    count = 0
    indexes = []
    
    for word in wordlist:
        if name in word:
            count += 1
            indexes.append(word.index(name)+1)
        else:
            indexes.append(0) 
    output_tuple = (count, indexes)
    return output_tuple

wordlist=[]
num = int(input("Enter the number of words"))
for i in range(0,num):
    print("Enter the word ",i+1)
    wordlist.append(input())
name = input("Enter the string")
result = find_words_with_substring(wordlist, name)
print(result)