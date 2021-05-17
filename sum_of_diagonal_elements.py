##Sum of Primary and Secondary diagonal elements that are not part in primary diagonal
n=int(input())
mat=[[int(input()) for i in range(n)]for j in range(n)]
diagonal_sum=0
for i in range(n):
    for j in range(n):
            if i==j:
                diagonal_sum+=mat[i][j]
for i in range(n):
    j=n-1
    if i==j:
        n-=1
        continue
    else:
        diagonal_sum+=mat[i][j]
    n-=1
print(diagonal_sum)
       
