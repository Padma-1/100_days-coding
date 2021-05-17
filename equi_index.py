"""n=int(input())
arr=list(map(int,input().split()))
for i in range(1,n-1):
    ls=0
    rs=0
    for j in range(0,i):
        ls+=arr[j]
        #print(ls)
    for k in range(i+1,n):
        rs+=arr[k]
        #print(rs)
    if ls==rs:
        print(i)
        break
"""
##using prefix algorithm
arr=list(map(int,input().split()))
n=len(arr)
#prefix=[0 for i in range(len(arr))]
prefix=list([0]*len(arr))#above line also for same purpose
prefix[0]=arr[0]
for i in range(1,n):
    prefix[i]=prefix[i-1]+arr[i]
ls=0
rs=0
for i in range(1,n-1):
    ls=prefix[i-1]
    rs=prefix[n-1]-prefix[i]
    if ls==rs:
        print(i)
        break
