value = float(input("Input Magnitude: "))

if value < 2:
    print("Micro")
elif value >= 2 and value < 3:
    print("Very Minor")
elif value >= 3 and value < 4:
    print("Minor")
elif value >= 4 and value < 5:
    print("Light")
elif value >= 5 and value < 6:
    print("Moderate")
elif value >= 6 and value < 7:
    print("Strong")
elif value >= 7 and value < 8:
    print("Major")
elif value >= 8 and value < 10:
    print("Great")
elif value >= 10:
    print("Meteoric")