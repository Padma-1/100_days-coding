def fun(n,a = 1):#fun(10,1)
    if n==0:
        return#we dont return anything so it stops 
    print(a,end=" ")#1
    return fun(n-1,a+1)#fun(9,2) it agains calls the function
#a+1 used to print from 1 to 10
#n-1 used to end the loop when n becomes 0
fun(10)
