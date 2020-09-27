n = int(input())
rev = 0
temp = n
while n:
    r = n%10
    n = n//10
    rev = rev*10+r
if (rev ==temp):
    print("plaindrome")
