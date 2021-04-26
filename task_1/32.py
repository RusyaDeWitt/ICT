num = []

for i in range(3):
    y = int(input())
    num.append(y)

num.sort()

print("Max:", num[2],"Min:",num[0],"Mid:",num[1])