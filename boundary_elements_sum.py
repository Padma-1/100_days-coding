##sum of all boundary elements in a given matrix
m=int(input())#no.of rows
n=int(input())#no.of columns
mat=[[int(input())for i in range(n)]for j in range(m)]
#print(mat)
boundary_sum=0
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            #print(mat[i][j])
            boundary_sum+=mat[i][j]
print(boundary_sum)
