#Triplet sum-1
##12 1 4 3 6 9
##25
##12 + 4 + 9  = 25
"""arr=list(map(int,input().split()))
key=int(input())
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            if arr[i]+arr[j]+arr[k]==key:
                print(arr[i],"+",arr[j],"+",arr[k]," = ",key)
                break"""

"""arr=list(map(int,input().split()))
key=int(input())
for i in range(len(arr)):
    s=key-arr[i]
    j=i+1
    k=len(arr)-1
    while j<k:
        if arr[j]+arr[k]==s:
            print(arr[i],arr[j],arr[k])
            break
        elif arr[j]+arr[k]<s:
            j+=1
        else:
            k-=1
"""#triplet sum
"""a=[12,3,6,9,4,1,5]
key=19
a=sorted(a)#[1,3,4,5,6,9,1]
i=0
count=0
for i in range(len(a)):
    j=i+1
    k=len(a)-1
    temp=0
    temp=key-a[i]
    while(j<k):
        if a[j]+a[k]==temp:
            count+=1
            print(a[i],a[j],a[k])
            break
        if a[j]+a[k]<temp:
            j+=1
        else:
            k-=1
if count==0:
    print("not found")
"""



#Given an array A of distinct integers and a sum value X.
##Find count of triplets with sum smaller than given sum value X.
##
##Input:
##First line consists of T test cases. 
##First line of every test case consists of N and X, denoting the number of elements in array and Sum Value respectively. 
##Second line consists of array elements.
##
##Output:
##For each testcase, output the count of Triplets.
"""t=int(input())
for i in range(t):
    n,x=map(int,input().split())#5 12
    a=list(map(int,input().split()))#[5,1,4,3,7]
    a=sorted(a)#[1,3,4,5,7]
    i=0
    count=0
    for i in range(len(a)):#i=0
        j=i+1#j=1-->6
        k=len(a)-1#k=5
        temp=0
        temp=x-a[i]
        while(j<k):
            if a[j]+a[k]<temp:#3+4<11
                count+=1
                #print(a[i],a[j],a[k])#1,3,4
                k-=1#
                if j==k:
                    k=len(a)-1
                    j+=1
            if a[j]+a[k]>=temp:
                k-=1
    print(count)"""

##Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
##
##Notice that the solution set must not contain duplicate triplets.
##Input: nums = [-1,0,1,2,-1,-4]
##Output: [[-1,-1,2],[-1,0,1]]
##Example 2:
##
##Input: nums = []
##Output: []
##Example 3:
##
##Input: nums = [0]
##Output: []
## 
"""a=[-1,0,1,2,-1,-4]
key=0
a=sorted(a)#[1,3,4,5,6,9,1]
i=0
count=0
l=[]
for i in range(len(a)):
    j=i+1
    k=len(a)-1
    temp=key-a[i]
    while(j<k):
        if a[j]+a[k]==temp:
            count+=1
            c=[a[i],a[j],a[k]]
            if c not in l:
                l.append(c)
        if a[j]+a[k]<temp:
            j+=1
        else:
            k-=1
if count==0:
    print("[]")
else:
    print(l)"""



        
