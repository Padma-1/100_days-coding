#special_prime
import math
n = int(input())
c = 1
def is_prime(n):
    x = int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    else:
        return True

def near_prime(n):
    n1=n-1
    while True:
        if is_prime(n1):
            return n1
        else:
            n1 = n1-1
            
if is_prime(n):
    a = near_prime(n)
    b = near_prime(a)
    while True:
        if a+b+c==n:
            print(" given number is special prime")
            break
        else:
           a = b
           b = near_prime(a)
        if a==2 or b==2:
            break
else:
    print("given number is not a special prime")
        
            
