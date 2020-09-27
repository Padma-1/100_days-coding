from demo import is_prime # importing function is_prime from pgm named demo
##super prime program
n=int(input())
def pos_prime(n):#position of that prime
    pos = 0
    for i in range(1,n+1):
        if is_prime(i):
            pos+=1
    return pos
if is_prime(n):#if given no. is prime then only we  need to find position 
   #print(pos_prime(11))#calling function
    if is_prime(pos_prime(n)):
        print("super prime")
    else:
        print(" not a super prime")
else:
    print("not a prime")
