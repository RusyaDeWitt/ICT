n = input()
s = input()

sf = 0
fs = 0

for i in range(len(s)):
    if(i+1 < len(s)):
        if(s[i] == 'S' and s[i+1] == 'F'):
            sf += 1
        if(s[i] == 'F' and s[i+1] == 'S'):
            fs += 1

if(sf > fs):
    print("YES")
else:
    print("NO")