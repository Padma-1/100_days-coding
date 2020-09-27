from demo import is_prime
#the below is the pgm what i have written in demo
##import math
##def is_prime(n):#given number is prime or not
##    if n==1:
##        return False
##    else:
##         x = int(math.sqrt(n))
##         for i in range(2,x+1):
##             if (n%i==0):
##                return False
##         else:
##             return True
###print(is_prime(1))
  
n = int(input())#137
digit_count = len(str(n))#finding digit count
prime_count = 0
i = 0
x = 10**2(digit_count - 1)#100
if is_prime(n):
    while True:
         r  =n%10#137%10 = 7
         n = n//10#137//10 = 13
         i+=1
         res = r*x+n#713,371,137
         n = res
         if is_prime(n):
             prime_count +=1
         #print(n)
         if i==digit_count:
               break
   
   if prime_count==digit_count:
       print("circular prime")
   else:
       print("not a circular prime")
else:
    print("not a circular prime")
    
