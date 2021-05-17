## an array A of integers, return true if and only if it is a valid mountain array.
##Recall that A is a mountain array if and only if:
##•	A.length >= 3
##•	There exists some i with 0 < i < A.length - 1 such that:
##o	A[0] < A[1] < ... A[i-1] < A[i]
##o	A[i] > A[i+1] > ... > A[A.length - 1]
##Example 1:
##Input: [2,1]
##Output: false
##Example 2:
##Input: [3,5,5]
##Output: false
##Example 3:
##Input: [0,3,2,1]
##Output: true
##Example 4:
##Input: [1,2,3,4,5,6,7,8,9]
##Output: false
##Example 5:
##Input: [100 90 80 70 60 50 40 30 20 10]
##Output: false
arr=list(map(int,input().split()))
x=sorted(arr)
if arr==x or arr==x[::-1] or len(arr)<3:
       print('false')
else:
       arr.append(-1)
       for i in range(len(arr)-1):
              if arr[i]<arr[i+1]:
                     arr[i]=0
              elif arr[i]>arr[i+1]:
                     arr[i]=1
              else:#if 2 elements are same
                     print('false')
                     break
       del arr[-1]
       y=sorted(arr)
       if arr==y:
              print(True)
       else:
              print(False)
              
              
