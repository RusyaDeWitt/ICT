n = int(input())
s = input().split()

a = [ ]
b = [ ]

for i in s:
    a.append(int(i))

a = sorted(a)

for i in range(a[0], a[-1]+1):
    b.append(i)

print(len(b)-len(a))
