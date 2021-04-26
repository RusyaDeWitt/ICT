a = 2
b = 3
c = 4
pi = 3

for i in range(1,16):
    if(i % 2 != 0):
        pi += 4/(a*b*c)
        print("Approximation:",i,":",pi)
    if(i % 2 == 0):
        pi -= 4/(a*b*c)
        print("Approximation:", i,":", pi)
    a += 2
    b += 2
    c += 2
