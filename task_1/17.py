print("Input Mass:")
m = int(input())

print("Input inital T:")
Ti = int(input())

print("Input final T:")
Tf = int(input())

deltaT = Tf-Ti

C = 4.186

print("Heat Capacity:", m*C*deltaT)