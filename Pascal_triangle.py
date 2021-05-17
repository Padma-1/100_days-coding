n=int(input())
arr=[[0 for i in range(n)]for j in range(n)]
#for i in arr:
#   print(i)
for i in range(len(arr)):
    for j in range(len(arr)):
        if j==0 or i==j:
            arr[i][j]=1
        else:
            arr[i][j]=arr[i-1][j-1]+arr[i-1][j]
#for i in arr:
#   print(i)
for i in arr[0:-1]:#excluding last row..bcoz it doesn't have 0's in it. 
    x=i.index(0)#find the index where 0 is..
    print(i[:x])#printing upto zeroes
print(arr[-1])#finally printing last row
    
 

              
