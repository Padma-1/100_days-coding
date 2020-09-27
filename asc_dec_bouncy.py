n = int(input())
x = list(str(n))

asc  =sorted(x)
des= sorted(x,reverse = True)

if(x==asc):
    print("given number is in ascending order")
elif(x==des):
    print("given number is in descending order")
else:
    print("given number is a bouncy number")















