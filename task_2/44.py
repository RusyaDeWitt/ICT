month = int(input("Input month:"))
date = int(input("Inpur date: "))


if month == 1 or month == 4 or month == 12:
    if month == 1 and date == 1:
        print("New Year's Day")
    elif month == 4 and date == 1:
        print("Canada Day")
    elif month == 12 and date == 25:
        print("Christmas Day")

else:
    print("That is not a holiday that falls on the same date each year.")
