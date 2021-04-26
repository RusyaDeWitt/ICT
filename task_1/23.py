import math

print("Input length and number of sides")

s = int(input())
n = int(input())

ans = n * ((s**2)/(4*math.tan(math.pi/n)))

print("Answer:",ans)