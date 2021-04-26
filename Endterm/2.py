s = input().split()
n = int(s[0])
a = int(s[1])

cnt = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        if(i*j == a):
            cnt += 1
print(cnt)