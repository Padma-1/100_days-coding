"""Input
5
5 5
2 7
8 10
10 20
4 5
Output
0
5
-1
8
0
Explanation

Test Case 1: [ 5 - 2 ] = 3

Test Case 2: [ 7 - 2 ] = 5

Test Case 3: No prime number in the given range. Output = -1
Test Case 4: [ 19 - 11 ] = 8
Test Case 5: The difference would be 0 since there is only one prime number in the given range."""

##T=int(input())
##for i in range(T):
##    l,r=map(int,input().split())
##    if l==1:
##        l+=1
##    if l==r:
##        print("0")
##    else:
##        temp=[]
##        for i in range(l,r+1):
##            for j in range(2,int(i**(1/2))+1):
##                           if i%j==0:
##                               break
##            else:
##                temp.append(i)
##        if temp==[]:
##            print("-1")
##        else:
##            res=temp[-1]-temp[0]
##            print(res)
##
x=1000001
seive=[1 for i in range(x+1)]
def seivegen():
    i=2
    while(i*i<=x):
        if seive[i]==1:
            for j in range(i*i,x+1,i):
                seive[j]=0
        i+=1
    seive[0]=0
    seive[1]=0

seivegen()
