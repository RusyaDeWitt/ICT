a = str(input())

a = a.replace(" ", "")
b = a

if(b == a[::-1]):
    print("Palindrome")
else:
    print("Not Palindrome")


