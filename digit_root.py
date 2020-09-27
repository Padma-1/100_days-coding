#99999-->9+9+9+9+9-->45-->4+5-->9__so ans is 9
def digitroot(n):
    sum=0
    while n:
        r=n%10
        sum+=r
        n=n//10
    if sum in[0,1,2,3,4,5,6,7,8,9]:
            return sum
    return digitroot(sum)
n=int(input())
print(digitroot(n))

#Method 2
def digitroot(n):
    sum=0
    while n>0 or sum>9:
        if n==0:
            n=sum
            sum=0
        r=n%10
        sum+=r
        n=n//10
    return sum
n=int(input())
print(digitroot(n))
        
    
    
