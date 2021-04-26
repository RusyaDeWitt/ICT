def shippingCalculator(n):
    a = 10.95
    for i in range(n-1):
        a += 2.95

    return a

n = int(input("Input n: "))

print(shippingCalculator(n))