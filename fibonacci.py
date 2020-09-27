#fibonacci upto n
n= 10
a = 0
b = 1
print(a,end = " ")
print(b,end = " ")
#i = 2#0,1 already printed
while True:
    c = a+b
    a,b = b,c#swapping
   # i+=1
    if c>n:
        break
    print(c,end=" ")#1 2 3 5 8


###fibonacci of n numbers
n= 10
a = 0
b = 1
print(a,end = " ")
print(b,end = " ")
i = 2#0,1 already printed
while True:
    c = a+b
    print(c,end=" ")#0 1 1 2 3 5 8 13 21 34
    a,b = b,c#swapping
    i+=1
    if i==n:
        break

    
#nearest fibonacci
n=10
a=0
b=1
while True:
    c=a+b
    a,b = b,c
    if c>n:
        break
print(a,b)
