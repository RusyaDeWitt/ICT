n = int(input("Input integer 2 or greater: "))
f = 2

print("The prime factors of",n,"are: ")
while f <= n:
    if(n%f == 0):
        print(f)
        n /= f
    else:
        f += 1