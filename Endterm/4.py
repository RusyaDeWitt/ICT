year = input()
a = int(year)
b = True
c = False

while b == True:
        a += 1
        s = set(str(a))
        if(str(a) != a):
            if(len(s) == 4):
                print(a)
                b = False
        else:
            a += 1
