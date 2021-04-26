def validTriangle(l):
    l.sort()
    if(l[2] >= l[0]+l[1]):
        return False
    else:
        return True

l = []
for i in range(3):
    n = int(input("Input length: "))
    l.append(n)

print(validTriangle(l))