#A number is abundant if sum of the proper factors of the number is greater than the given number eg:12-->1+2+3+4+6=16-->16>12 i.e., 12 is Abundant number
n=int(input())
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        sum+=i
if sum>n:
     print("Abundant number")
else:
     print("not Abundant number")
        
