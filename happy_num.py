n= int(input())
sum1 = 0
while True:
    r= n%10#7
    n = n//10#0
    sum1 = sum1+r**2#49
    if(n == 0):
        n = sum1#n = 49 now
        sum1 = 0
        if(1<=n<+9):
            break;
if n==1:
    print("happy")
else:
    print("not a happy number")
        
    
    
