grade = float(input("Input grade: "))

if grade == 4:
    print("A+")
elif grade > 3.7 and grade < 4:
    print("A")
elif grade > 3.3 and grade <= 3.7:
    print("A-")
elif grade > 3 and grade <= 3.3:
    print("B+")
elif grade > 2.7 and grade <= 3:
    print("B")
elif grade > 2.3 and grade <= 2.7:
    print("B-")
elif grade > 2 and grade <= 2.3:
    print("C+")
elif grade > 1.7 and grade <= 2:
    print("C")
elif grade > 1.3 and grade <= 1.7:
    print("C-")
elif grade > 1 and grade <= 1.3:
    print("D+")
elif grade == 1:
    print("D")
elif grade < 1:
    print("F")