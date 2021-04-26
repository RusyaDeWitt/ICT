num = int(input())
a = ""

while num >= 1:
    if(num%2 == 0):
        a += '0'
        num =  num // 2
    if(num%2 != 0):
        a += '1'
        num = num // 2
print(a[::-1])
