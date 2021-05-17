#for each function  you need to find the summation of all primes between the integers l and r inclusive.
"""constraints are 1<=N<=5*10^5 AND 1<=l<=r<=10^6
IF INPUT            OUTPUT
2                  
1 6                  10
4 16                 36

For the query,the primes between 1 and 6 are 2, 3 and 5. Thus the answer 2+3+5=10.
Similarily,for the second query, Answer 5+7+11+13=36."""
#using seive and prefix_sum algorithms
x=1000001#if x=10
seive=[1]*x
seive[0]=0
seive[1]=0
i=2
while (i*i<=x):#to generate seive-->[0, 0, 1, 1, 0, 1, 0, 1, 0, 0]
    if seive[i]==1:
        for j in range(i*i,x,i):
            seive[j]=0
    i+=1
print(seive)
for i in range(1,x):#to generate prefix array-->[0, 0, 2, 5, 5, 10, 10, 17, 17, 17]
    if seive[i]==1:
        seive[i]=i+seive[i-1]
    else:
        seive[i]=seive[i-1]
print(seive)
N=int(input())
for i in range(N):
    l,r=map(int,input().split())
    print(seive[r]-seive[l-1])
   
