str = input()
str2 = input()

str = str.replace(" ", "")
str2 = str2.replace(" ", "")

if(sorted(str.lower()) == sorted(str2.lower())):
    print("YES")
else:
    print("NO")