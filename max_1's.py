##Given a binary array, find the maximum number of consecutive 1s in this array.
##Example 1:
##Input:
##6
##1 1 0 1 1 1
##Output:
##3
n=int(input())
l=list(map(int,input().split()))
count=0
c=0
for i in range(len(l)):
       if l[i]==1:
              count+=1
       if l[i]==0:
          if count>c:
              c=count
              count=0
          else:
              c=count
              count=0
       
if count>c:
       c=count
       print (c)
else:
   print(c)


