n = int(input())
l = 1
ways = 0

for i in range(n-1):
    e = n - l
    if(e%l == 0):
        ways +=1
        l += 1
    else:
        l += 1

print(ways)