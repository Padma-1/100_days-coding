#check whether the given number is the product of two consecutive integers or not-->i.e pronic number or not
#from math import sqrt
def is_pronic(n):
    for i in range(1,n//2):#12
        if n%i==0 and n%(i+1)==0 and (i*(i+1)==n):
            return True
    else:
        return False
n=int(input())
print(is_pronic(n))
