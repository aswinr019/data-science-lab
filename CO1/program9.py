# Given a file “mark.csv” of student data with the fields rollno, name,
# branch, m1, m2, m3, write python code to
# •Print total marks of all students
# •Find the average mark of each subject
# •Find the student with highest and second highest mark.

import csv

with open("./mark.csv") as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        print(row)
