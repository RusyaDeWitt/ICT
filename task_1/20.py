print("Input Pressure:")
p = float(input())

print("Input Liters:")
v = float(input())

print("Input Temperature(Kelvin):")
t = float(input())

r = 8.314

n = float((p*v)/(r*t))

print("Answer:",n)