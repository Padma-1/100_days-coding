from math import sqrt
def is_sqrt(a):
    x1=sqrt(a)
    if x1==int(x1):
        return True
    return False

def is_fibo(n):
    x=5*(n**2)-4
    y=5*(n**2)+4
    if is_sqrt(x) or is_sqrt(y):
        return n

##def near_fibo(n):
##    i=1
##    while 1:
##        if is_fibo(n-i):
##            return n-i
##        i+=1

#near_fibo by recursion    
def near_fibo(n,i=1):
        if is_fibo(n-i):
            return n-i
        i+=1
        return near_fibo(n,i)
        
"""main program here"""    
n=int(input())#30
while 1:
    if is_fibo(n):#30-->9-->1
        print(n)#1 Here 1 is printed
        break
    else:
        r=near_fibo(n)#21-->8
        n=n-r#30-21=9-->9-8=1
        print(r)#21-->8 Here 21 and 8 are printed
