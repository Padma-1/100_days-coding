#kth setbit
#using logic
"""def kth_setbit(n,k):
    n=n>>(k-1)
    if n&1==1:
        return True
    else:
        return False
n=int(input())
k=int(input())
print(kth_setbit(n,k))"""

#using bin
n=int(input())
k=int(input())
n=bin(n)
n=n[2: ]
n=n[ ::-1]
for i in range(len(n)):
    if i==k-1:
        if n[i]=='1':
            print("true")
            break
else:
    print("false")
        


