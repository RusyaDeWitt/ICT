print("Input Temperature and Speed:")
t = float(input())
s = float(input())

if(t <= 10 and s >= 4.8):
    ans = 13.12+0.6215*t-11.37*s**0.16+0.3965*t*s**0.16
    print(round(ans))