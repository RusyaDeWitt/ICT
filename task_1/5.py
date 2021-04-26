less_one = 0.10
more_one = 0.25

print("Input less than 1:")
less = int(input())
print("Input more than 1:")
more = int(input())

ans = round((more * more_one) + (less * less_one),2)

print("Your refund is:",ans,"$")