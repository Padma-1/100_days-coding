n  = int(input())#145
temp = n
sum1 = 0
while n:
    r = n%10
    
    fact = 1
    for i in range(1,r+1):
          fact = fact*i
         
      
          
    sum1+=fact
    n = n//10
    
if temp == sum1:
    print("strong number")
else:
    print("not a strong number")
    
        
    



       
    
   


    




