n=int(input())
arr=list(map(int,input().split()))
t=int(input())
prefix=[0 for i in range(n)]
prefix[0]=arr[0]
for i in range(1,n):
       prefix[i]=prefix[i-1]+arr[i]
for i in range(0,t):
    l,r=map(int,input().split())
    sum1=prefix[r]
    if (l>0):
        sum1=prefix[r]-prefix[l-1]
    print(sum1)

