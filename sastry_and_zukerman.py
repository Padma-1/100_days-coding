###Sastry number:A number N is a Sastry Number if N concatenated with N + 1 gives a perfect square.eg:183 
##from math import sqrt
##def is_sastry(n):
##    m=n+1
##    result=str(n)+str(m)
##    result=int(result)
##    if sqrt(result)==int(sqrt(result)):
##        return True
##    return False
##n=int(input())
##print(is_sastry(n))

#Zukarman numbers:Zuckerman Number is a number which is divisible by the product of its digits eg:115
def is_Zukerman(n):
    mul=1
    while n:
        r=n%10
        n=n//10
        mul*=r
    #print(mul)
    if temp%mul==0:
        return True
    return False

n=int(input())
temp=n
print(is_Zukerman(n))
