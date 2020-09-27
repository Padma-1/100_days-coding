num = int(input())
rev = 0
while num:
    rem = num%10
    num = num//10
    rev = rev*10+rem
print(rev)
    
