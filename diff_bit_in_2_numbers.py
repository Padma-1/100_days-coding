def diff_bit(n,m):
    n=n^m# xor gives '1' when both i/ps are different
    c=1
    while n:
        if n&1==1:#when the given input's LSB position has 1 then only n&1 results 1
            return c
            break
        else:
            n=n>>1#to take 1 to LSB
            c+=1
x=int(input())
y=int(input())
print(diff_bit(x,y))
