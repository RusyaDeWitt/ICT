x1 = int(input("Input coordinate x: "))
y1 = int(input("Input coordinate y: "))

xi = x1
yi = y1

perimeter = 0
blank = "1"

while blank != "":
    x2 = input("Input coordinate x (blank to quit): ")
    if (x2 != ""):
        y2 = input("Input coordinate y : ")

        x2 = int(x2)
        y2 = int(y2)
    else:
        break

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    perimeter += distance
    x1 = x2
    y1 = y2

distance = ((xi - x1)**2 + (yi - y1)**2) ** 0.5
perimeter += distance
print("P =", perimeter)