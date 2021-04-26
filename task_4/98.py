hx = input("Input hex: ")
n =  int(input("Input num: "))

def hex2int(hx):
    return int(hx, 16)

def int2hex(n):
    return hex(n)

print(hex2int(hx))
print(int2hex(n))