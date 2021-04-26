numbers = {
    "1":  "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

second_number = {
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifthy",
    "6": "sixty",
    "7": "seventy",
    "8": "eigthy",
    "9": "ninety"
}

third_number = {
    "0": "ten",
    "1": "eleven",
    "2": "twelve",
    "3": "thirteen",
    "4": "fourtheen",
    "5": "fiftheen",
    "6": "sixteen",
    "7": "seventeen",
    "8": "eighteen",
    "9": "nineteen"
}



str = input()

res = ""

if(len(str) == 3):
    res += numbers[str[0]]
    res += " hundered "
    if(str[1] == '1'):
        res += third_number[str[2]]
    else:
        res += second_number[str[1]]
        res += " "
        res += numbers[str[2]]

if(len(str) == 2):
    res += second_number[str[0]]
    res += " "
    res += numbers[str[1]]
if(len(str) == 1):
    res += numbers[str[0]]

print(res)