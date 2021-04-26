a = int(input())
sum = 0

for i in range(a):
    s = input().split()
    for k in s:
        sum += int(k)

if(sum == 0):
    print("YES")
else:
    print("NO")