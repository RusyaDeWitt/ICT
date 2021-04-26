letter = input("Input letter: ")
number = int(input("Input number: "))


if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    if number % 2 == 0:
        print("White")
    elif number % 2 != 0:
        print("Black")
if letter == "b" or letter == "d" or letter == "f" or letter == "h":
    if number % 2 == 0:
        print("Black")
    elif number % 2 != 0:
        print("White")