###collatz_sequence
##def collatz_series(n):
##    print(n,end=" ")
##    while n>1:
##        if(n%2==0):
##            n=n//2
##            print(n,end=" ")
##        else:
##            n=3*n+1
##            print(n,end=" ")
##n=int(input())
###collatz_series(n)

#using recursion
def collatz_sequence(n,i=1):
    if i==1:#to print input
        print(n,end=" ")
        i+=1
    if n==1:
        return
    if n%2==0:
        n=n//2
        print(n,end=" ")
        return collatz_sequence(n,2)
    else:
        n=3*n+1
        print(n,end=" ")
        return collatz_sequence(n,2)
n=int(input())
collatz_sequence(n)
        
        
