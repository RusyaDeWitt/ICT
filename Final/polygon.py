n = int(input())

for i in range(n):
    s = input().split()
    a = int(s[0])
    b = int(s[1])

    if(a%b == 0):
        print("YES")
    else:
        print("NO")