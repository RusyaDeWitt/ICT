n = int(input())

sum = 0

for i in range(n):
    s = input()
    if s == "Tetrahedron":
        sum += 4
    if s == "Cube":
        sum += 6
    if s == "Octahedron":
        sum += 8
    if s == "Dodecahedron":
        sum += 12
    if s == "Icosahedron":
        sum += 20

print(sum)