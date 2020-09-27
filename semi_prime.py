from demo import is_prime
import math
n = int(input())
for i in range(1,int(math.sqrt(n))+1):
    if is_prime(i):
        if n%i==0:
            y = n//i
            if is_prime(y):
                print("semi prime")
                break
else:
    print("not a semi prime")
            
