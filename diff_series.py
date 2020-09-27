"""#input:9
#output:1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1 
def series(n):
    i=1
    while n:
       if(i<n):
         print(i,end=" ")
         i+=1
       else:
          print(n,end=" ")
          n-=1

n=int(input())
series(n)"""




#input:10
#output:1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1
#using recursion
def series(n,i=1):
    if n==0:
        return
    if i<n:
        print(i,end=" ")
        return series(n,i+1)
    else:
        print(n,end=" ")
        return series(n-1,i)
n=int(input())
series(n)
        
