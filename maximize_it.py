from itertools import product
k,m = map(int,input().split())
z = []
for i in range(k):
    l = list(map(int,input().split()))
    z.append(l[1: ])
p = list(product(*z))

sum1 = 0
z1  =[]
for i in p:
    for j in i:
        sum1 +=j**2
    z1.append(sum1%m)
    sum1 = 0
        
print(max(z1))
             
    
    
    
