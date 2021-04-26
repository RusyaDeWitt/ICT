m = int(input("Input m: "))
n = int(input("Input n: "))

d = 0

if(n < m):
    d = n
else:
    d = m

while m%d != 0 or  n%d != 0:
    d -= 1

print(d)