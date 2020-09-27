#using logic
n=int(input())
for i in range(1,n//2+1):
    if (2**i)==n:
        print("true")
        break
else:
    print("false")


#using and-->if number of 1's is 1 we can represent that number in 2**
n=int(input())
res=0
while n:
    n=n&(n-1)
    res+=1
if res==1:
    print("true")
else:
    print("false")
    




#using and     
def two_power(n):
    if n&(n-1)==0:
        return True
    return False
n=int(input())
print(two_power(n))
