n = 157
summ = 0
temp = n
while n:
    r = n%10
    n = n//10
    summ+=r
if (temp%summ==0):
    print("harshed")
else:
    print("not a harshed number")
