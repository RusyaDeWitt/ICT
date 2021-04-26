n = input().split()
n = set(n)

c = input().split()
c = set(c)

for i in n:
    if(i in c):
        print(i)