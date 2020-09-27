n = int(input())
t = n
while n:
    r = n%10
    n = n//10
    if (t%r==0):
        continue
    print("unlucky")
    break
else:
    print("lucky")

"""n = int(input())
temp  = n
n_count = 0
count = 0

while n:
    r = n%10
    n = n//10
    n_count+=1

    #print(r)
    if(temp%r == 0):
        count+=1
if(n_count == count):
    print("lucky number")
else:
    print("not a lucky number")"""
        

