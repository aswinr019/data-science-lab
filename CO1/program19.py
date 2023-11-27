# Simulate rolling a fair six-sided die 1000 times and count the
# occurrences of each number.

import random


def roll_die(number):
    occurrences = [0] * 6
    for i in range(0, number):
        roll = random.randint(1, 6)
        occurrences[roll - 1] = occurrences[roll - 1] + 1
    return occurrences


number = int(input("Enter the number of times to roll dice: "))
count = roll_die(number)

print("The number of occurrences of each side of die")

for i in range(6):
    print(f"Side { i + 1} : { count[i] } ")
