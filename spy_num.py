n = int(input())
add = 0
mul = 1
while n:
    r=n%10
    n=n//10
    add = add+r
    mul = mul*r
#print(add)
#rint(mul)
if(add == mul):
    print("spy number")
else:
    print("not a spy number")
    
