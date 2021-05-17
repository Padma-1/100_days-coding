#BINARY EXPONENT
"""base=int(input())#2
exp=int(input())#10
res=1
while (exp):#10!=0-->
    if (exp%2==0):#even10-->
        base=base*base#4-->16-->256
        exp=exp/2#-->5-->2-->1
    else:
        res*=base#4-->256*4=1024
        exp=exp-1#4-->0
print(res)"""
#MODULAR ARITHMETIC-->large inputs and ouputs can't able to store in database so to
#reduce those numbers we use modulo-->mod=10^9+7-->for not to override the values in it
base=int(input())
exp=int(input())
res=1
mod=(10**9)+7
while (exp):
    if (exp%2==0):
        base=(base*base)%mod
        exp=exp/2
    else:
        res=(res*base)%mod
        exp=exp-1
print(res)

