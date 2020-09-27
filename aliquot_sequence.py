"""Aliquot_sequence
input:16
output:16 15 9 4 3 1 0
Input:  n = 10
Output: 10 8 7 1 0
Sum of proper divisors of 10 is  5 + 2 + 1 = 8.
Sum of proper divisors of 8 is 4 + 2 + 1 = 7.
Sum of proper divisors of 7 is 1
Sum of proper divisors of 1 is 0
Note that there is no proper divisor of 1."""


##def Aliquot_seq(n,j=0):
##    if j==0:#to print given input
##        print(n,end=" ")
##        j+=1
##    i=1
##    sum1=0
##    for i in range(1,n):
##       if(n%i==0):
##           sum1=sum1+i
##    print(sum1,end=" ")
##    if(sum1==0):
##        return
##    return Aliquot_seq(sum1,j)
##n=int(input())
##Aliquot_seq(n)

##Aliquot_sequence
from math import sqrt
def proper_div_sum(n):
    if n==1:
        print(0,end=" ")
        return
    sum1=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if i==n//i:
                sum1+=i
            else:
                sum1+=i+(n//i)
    n=sum1-n#n is not added to sum
    print(n,end=" ")
    return proper_div_sum(n)
n=int(input())
print(n,end=" ")
proper_div_sum(n)
