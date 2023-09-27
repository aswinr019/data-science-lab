# Given a file “mark.csv” of student data with the fields rollno, name,
# branch, m1, m2, m3, write python code to
# •Print total marks of all students
# •Find the average mark of each subject
# •Find the student with highest and second highest mark.

import csv

with open("./mark.csv",mode='r',newline='') as file:
    csvreader = csv.reader(file)
    print("Student data: ")
    next(csvreader)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    total = 0
    prevtotal = 0
    highest=''

    for row in csvreader:
        total = int(row[3])+int(row[4])+int(row[5])
        print(f" { row } , Total mark : { total }")
        if( total > prevtotal ):
            highest = row[1]
        prevtotal = total
        sum1 = sum1 + int(row[3])
        sum2 = sum2 + int(row[4])
        sum3 = sum3 + int(row[5])
    print(f"Averagae mark of m1 , m2 and m3 are: { sum1 / 3} { sum2 / 3 } { sum3 / 3}")
    print(f"Student with the highest mark is : { highest }")
