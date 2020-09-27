##import math
##n=int(input())
##pc = 0
##dc=0
##x = int(math.sqrt(n))
##for i in range(2,x+1):
##    if(n%i==0):
##        print("not prime")
##        break
##else:
##    while n:
##        r = n%10
##        n=n//10
##        dc+=1
##        y = int(math.sqrt(r))
##        for i in range(2,y+1):
##            if(r%i==0):
##                break
##        else:
##            pc+=1
##    if(pc==dc):
##        print('mega prime')
##    else:
##        print("prime but not mega prime")
            
        
        
import math
n=int(input())
pc = 0
dc=0
def is_prime(n):
    x = int(math.sqrt(n))
    for i in range(2,x+1):
        if(n%i==0):
            print("not  a prime")
            return False
          
    else:
        return True
if is_prime(n):
    while n:
        r = n%10
        n=n//10
        dc+=1
        if is_prime(r):
            pc+=1
            
      
    if(pc==dc):
        print('mega prime')
    else:
        print("prime but not mega prime")
            
        
        
