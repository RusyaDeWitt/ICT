def lowestTerms(a, b):
    m = 0
    for i in range(1,a+1):
       if(a % i == 0 and b % i == 0):
           m = i
       i += 1

    a = a // m
    b = b // m

    return (a,b)

a = int(input("Input a: "))
b = int(input("Input b: "))

print(lowestTerms(a, b))