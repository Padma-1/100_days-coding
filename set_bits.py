#number of setbits(1's) in a given number
#using bin function
binary_num=list(bin(int(input())))#8-->['0', 'b', '1', '0', '0', '0']
set_bits = binary_num.count('1')
print(set_bits)#1


#using logic
def dec_to_bin(n):
    l=[ ]
    while n:
        x=n%2
        n=n//2
        l.append(x)
    #print(l[ :: -1])#-->to get binary representation
    print(l.count(1))#no.of set bits
n=int(input())#6
dec_to_bin(n)


#using bin
n=int(input())
s=bin(n)
res=0
for i in s[2:]:
    if i=='1':
        res+=1
print(res)

#using simple logic
n=int(input())#15
res=0
while n:#15-->7-->3-->1-->0
    if n%2!=0:#T-->T-->T-->T
        res+=1#1-->2-->3-->4
    n=n//2#15//2=7-->7//2=3-->3//2=1-->1//2=0
print(res)

#accurate method-->by using "and" we make all 1's to 0's-->in how many iterations all 1's coverts into 0's-->that given the number of setbits#iteration stops when n=0
n=int(input())#128
res=0
while n:#loop iterate for no.of 1's times#128-->0F
    n=n&(n-1)
    #1000 0000
    #0111 1111
    #---------
    #0000 0000
    #---------
    res+=1#1
print(res)

#"and" with "right shift"
n=int(input())
res=0
while n:
    if n&1==1:
        res+=1
    n=n>>1
print(res)



