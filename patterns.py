#pattern 1
"""A A A A 
   B B B B 
   C C C C 
   D D D D"""
n=int(input())
x=64
for i in range(1,n+1):
        for j in range(1,n+1):
                print(chr(i+x),end=" ")#print(chr(j+x),end=" ")
        print()

        
#pattern 2
"""5 5 5 5 5 
   4 4 4 4 4 
   3 3 3 3 3 
   2 2 2 2 2 
   1 1 1 1 1 """
n=int(input())
for i in range(n,0,-1):
        for j in range(1,n+1):
                print(i,end=" ")
        print()


#pattern 3
"""5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 
   5 4 3 2 1 """
n=int(input())
for i in range(1,n+1):
        for j in range(n,0,-1):
                print(j,end=" ")
        print()

