n = int(input())
m = int(input())
a = int(input())

x = m//a
y = n//a

if m % a != 0:
    x = x + 1
if n % a != 0:
    y = y + 1

print(x*y)