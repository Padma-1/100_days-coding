##Suppose you have a long flowerbed in which some of the plots are planted and some are not.
##However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
##
##Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty),
##and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
##Test1                          
##8
##0 0 0 0 0 1 0 0
##0
##True
##----
##7
##1 0 0 0 0 0 1
##2
##True
##---
##4
##0 0 0 0
##1
##True
##---
##2
##0 1
##1
##False
##-----
##5
##0 0 1 0 0
##2
##True
##------
##
##8
##1 0 1 0 1 0 0 1
##2
##False

n=int(input())
arr=list(map(int,input().split()))
new=int(input())
count=0
for i in range(len(arr)):
       if (arr[i]!=1) and (i==0 or arr[i-1]!=1) and (i==n-1 or arr[i+1]!=1):
              arr[i]=1
              count+=1
if new<=count:
       print(True)
else:
       print(False)
       
