s1 = input()
s2 = input()

s3 = s1+s2
print(s3)

m=len(s3) // 2

print(s3[:m]+s1+s3[m:])