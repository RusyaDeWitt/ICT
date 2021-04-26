n = int(input())

even = "I love "
odd = "I hate "

if n == 1:
    print("I hate it")
if n == 2:
    print("I hate that I love it")
if n > 2:
    temp = ""
    for i in range(1, n):
        if i%2 == 0:
            temp += even
        if i%2 != 0:
            temp += odd
        if i+1 == n:
            temp += "it"
        if i+1 != n:
            temp += "that "
print(temp)