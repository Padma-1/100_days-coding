#is_prime
import math
def is_prime(n):#given number is prime or not
    if n==1:
        return False
    else:
         x = int(math.sqrt(n))
         for i in range(2,x+1):
             if (n%i==0):
                return False
         else:
             return True
#print(is_prime(1))
  


