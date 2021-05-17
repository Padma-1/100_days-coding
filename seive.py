# to find a number is prime or not using seive array-->here once seive is generated and then checking whether that is prime or not based on 0 and 1 on seive array
"""def seivegen():
    seive=[1 for i in range(m+1)]
    i=2
    while(i*i<=m):
        if seive[i]==1:
            for j in range(i*i,m+1,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
t=int(input())
while t:
    n,m=map(int,input().split())
    seivegen()
    sum1=0
    for i in range(n,m+1):
        if seive[i]==1:
            sum1+=i
    print(sum1)
t-=1"""

def seivegen():
    seive=[1 for i in range(r+1)]
    i=2
    while (i*i<=r):
        if seive[i]==1:
            for j in range(i*i,r+1,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0
    sum1=0
    for i in range(l,r+1):
        if seive[i]==1:
            sum1+=i
    return sum1

N=int(input())
for i in range(N):
    l,r=map(int,input().split())
    print(seivegen())


