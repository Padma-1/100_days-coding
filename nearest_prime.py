n= int(input())
h=l =0

x = n+1
y = n-1
while True:
    fc = 0
    for i in range(1,x+1):
        if (x%i == 0):
            fc+=1
    if fc==2:
            h = i
            break
    else:
            x+=1
while True:
            
    fc1 = 0
    for j in range(1,y+1):
        if (y%j == 0):
            fc1+=1
    if fc1==2:
            l =j
            break
    else:
            y-=1
if abs(n-h)>abs(n-l):
    print(l)
elif abs(n-h)<abs(n-l):
    print(h)
else:
    print(l)
    
   
        
       
        
   
