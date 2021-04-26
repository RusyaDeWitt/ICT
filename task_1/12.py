import math

print("Input t1 and g1")
t1 = math.radians(int(input()))
g1 = math.radians(int(input()))

print("Input t2 and g2")
t2 = math.radians(int(input()))
g2 = math.radians(int(input()))

distance = 6371.01 * math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))

print(round(distance))
