print("kg or pounds?")
print("k - kg , p - pounds")

ans = input()
if(ans == "k"):
    print("Input weight and height")
    w = int(input())
    h = float(input())
    bmi = w/h**2
    print("BMI:",bmi)
if(ans == "p"):
    print("Input weight and height")
    w = int(input())
    h = float(input())
    bmi = (w/h**2)*703
    print("BMI:",bmi)