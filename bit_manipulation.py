#reverse a list
"""a=list(map(int,input().split()))
def rev(l,r,a):
    if l>r:
        return a
    a[l],a[r]=a[r],a[l]
    return rev(l+1,r-1,a)
print(rev(0,len(a)-1,a))
"""
#string is palindrome or not
"""s="abbaba"
def palindrome(l,r,s):
    if l>r:
        return True
    if s[l]!=s[r]:
        return False
    return palindrome(l+1,r-1,s)
print(palindrome(0,len(s)-1,s))"""
#factorial of a number
"""def fact(i):
    if i==n:
        return n
    return i*fact(i+1)
n=int(input())#5
i=1
print(fact(i))
"""
#to get all combos of sum n
"""n=int(input())
stack_space=[]
def combos(n,stack_space):
    if n==0:
        print(stack_space)
        return
    for i in range(1,n+1):
        stack_space.append(i)
        combos(n-i,stack_space)
        stack_space.pop()
print(combos(n,stack_space))"""
"""def combos(n,a=[]):
    if n==0:
        print (a)
        #return
    for i in range(1,n+1):
        temp=a.copy()
        temp.append(i)
        combos(n-i,temp)
n=int(input())
combos(n)"""
#
##from itertools import permutations
##s="abc"
##a=[]
##a.append(permutations(s))
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
t=int(input())
for i in range(t):
    n=int(input())
    print(fact(n))

























        
