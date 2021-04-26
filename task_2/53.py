print("Input value:")
value = float(input())

if value == 0.0:
    print("Unacceptable performance")
elif value == 0.4:
    print("Acceptable performance")
elif value >= 0.6:
    print("Meritorious performance")
else:
    print("Invalid value")