import random

n = random.randint(1, 100)
print(n)
max = n
times = 0

for i in range(100):
    a = random.randint(1, 100)

    if(a > max):
        max = a
        print(a, "<-- Updated")
        times += 1
    else:
        print(a)

print("The max value was:", max)
print("The max value was updated", times, "times")