n = input().split()
n = set(n)
c = input()

for i in n:
    if(i == c):
        n.remove(c)
print(i)