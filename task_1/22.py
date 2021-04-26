import math

print("Inpus s1 s2 s3")
s1 = int(input())
s2 = int(input())
s3 = int(input())


s = (s1+s2+s3)/2
total = s*(s-s1)*(s-s2)*(s-s3)
ans = math.sqrt(total)

print("Area:",ans)