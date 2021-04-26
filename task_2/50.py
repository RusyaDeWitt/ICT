a = int("Input a: ")
b = int("Input b: ")
c = int("Input c: ")

dis = b**2 - 4*a*c

if dis < 0:
    print("Does not have any real roots")

elif dis == 0:
    root = -b / 2*a
    print("One real root:",root)

elif dis > 0:
    root_one = (-b + dis)/2*a
    root_two = (-b - dis)/2*a

    print("Have two real roots:",root_one,root_two)