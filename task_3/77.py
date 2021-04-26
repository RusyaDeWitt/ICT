binary = input()
sum = 0

rbinary = binary[::-1]
for i in range(len(binary)):
    if(rbinary[i] == '1'):
        sum += 1 * 2**i
    else:
        sum += 0

print(sum)