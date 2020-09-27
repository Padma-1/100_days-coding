#canada number or not-->sum of squares of each individual digits is equal to sum of non trivial divisors/factors
from math import sqrt
def sum_sq_digits(n):
    sum1=0
    while n:
        r=n%10
        n=n//10
        sum1+=r**2
    return sum1

def non_trivial_sum(n):
    result=0
    for i in range(2,n//2):
        if n%i==0:
            result+=i
    return result

def is_canada(n):
    if sum_sq_digits(n)==non_trivial_sum(n):
        return True
    return False
n=int(input())#125,581,1699
print(is_canada(n))





"""#to find divisors
def non_trivial_sum(n):
    result=0

    for i in range(1,int(sqrt(n))+1):#25
        if n%i==0:#25%1==0-->25%5==0
            if i==n//i:#1==25//1-->5==25//5 here divisor and quouient are same
                result+=i#26+5=31
            else:
                result+=i+(n//i)#26
    return result-1-n#for use in place of non_trivial_sum code after result=0

"""

            
    
    
        
    
    
