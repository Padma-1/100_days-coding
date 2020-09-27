###n fibonacci numbers using function
##def fibo(n):
##    a = 0
##    b = 1
##    if(n==1):
##        print(a)
##    elif(n==2):
##        print(a,b)
##    else:
##        print(a,b,end=" ")
##        n=n-2#already 2 values printed so '8'
##        while n:#8 6 5 4 3 2 1-->True 0-->False
##            c = a+b
##            #if(c>x):#upto n fibonacci remove comments from these 2 steps
##             #   break
##            print(c,end = " ")
##        
##            a,b = b,c
##            n = n-1
##       
##n = int(input())
##x=n
##fibo(n)#10



#if given number is fibonacci or not
##def is_fibo(n):
##    a=0
##    b=1
##    if n==0 or n==1 :
##        return True
##    else:
##        while True:
##            c=a+b
##            a,b = b,c
##            if (c>=n):
##                 break
##        if(c==n):
##             return True
##        else:
##            return False
##            
##n=int(input())
##print(is_fibo(n))

#if given number is fibonacci or not
"""n=int(input())
a=0
b=1
if n==0 or n==1:
    print("fibonacci")
while n>1:
    c=a+b
    a,b=b,c
    if c==n:
        print("fibonacci")
        break
    else:
        if c>n:
            print("not a fibonacci")
            break"""


import math
def is_sqrt(n):
    x=math.sqrt(n)
    if x==int(x):
       return True#returns and stop execution
    return False
#print(is_sqrt(26))



#easiest method to find if a given number is fibonacci or not
def is_fibo(n):
    x=5*(n**2)-4
    y=5*(n**2)+4
    if is_sqrt(x) or is_sqrt(y):
        return True
    else:
        return False
#n=int(input())
#print(is_fibo(n))



    


#to get Nth fibonacci
##def nth_fibo(n):
##    a = 0
##    b = 1
##    if(n==1):
##        print(a)
##    elif(n==2):
##        print(b)
##    else:
##        n=n-2
##        while n:
##            c = a+b
##            a,b = b,c
##            n = n-1
##        return c
##                
##n = int(input())
##print(nth_fibo(n))




#easiest method to find nth fibonacci using formula
##from math import sqrt as s
##def nth_fibo(n):
##    n=n-1
##    x=(1+s(5))**n
##    y=(1-s(5))**n
##    z=(2**n)*s(5)
##    result = (x-y)//z
##    print(result)
##n=int(input())
##nth_fibo(n)






#near fibonacci number
##def near_fibo(n):
##    a=0
##    b=1
##    x=n#8
##    n=n-2
##    while True:
##        c=a+b#1-->2-->3-->5-->8-->13
##        a,b = b,c#a=1,b=1-->a=1,b=2-->2,3-->3,5-->5,8-->8,13
##        if(c>x):#8>8F-->13>8T
##            break
##    return a,b
##n=int(input())
##n1,n2 = near_fibo(n)
##if (abs(n-n1)>abs(n-n2)):
##    print(n2)
##elif (abs(n-n1)<abs(n-n2)):
##    print(n1)
##else:
##    print(n1,n2)






#n fibonacci numbers using recursion
##def fun(n,a=0,b=1):
##    if n==0:
##        return
##    if a==0 and n==2:
##        print(a,b)
##        return
##    if a==0:# print at beginning only
##        print(a,b,a+b,end=" ")#0 1 1-->3 values primted
##        return fun(n-3,b,a+b)#fun(7,1,1) n-3--> because already 3 values printed
##    else:
##        print(a+b,end=" ")#2-->1 value printed
##        return fun(n-1,b,a+b)#fun(7,1,2) n-1-->1 value printed above
##fun(5)





###upto n fibonacci using recursion
##def fibo_series(n,a=0,b=1):
##    if n==0:
##        return
##    if a==0 and n==2:
##        print(a,b)
##        return
##    if a==0:# print at beginning only
##        print(a,b,a+b,end=" ")#0 1 1-->3 values primted
##        return fibo_series(n-3,b,a+b)#fun(7,1,1) n-3--> because already 3 values printed
##    else:
##        if(a+b >x):
##            return
##        print(a+b,end=" ")#2-->1 value printed
##        
##        return fibo_series(n-1,b,a+b)#fun(7,1,2) n-1-->1 value printed above
##n=int(input())
##x=n
##fibo_series(n)


#to get left and right fibonacci of given fibonacci nuber
##from math import sqrt as s
##n1=int(input())#8
##x=(1+s(5))/2
##n0=round(n1/x)
##n2=round(n1*x)
##print(n0,n1,n2)#5,8,13

    
    
