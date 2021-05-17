#Two pointer algorithm
#finding 2 elements whose sum=key
#a=[1,6,12,17,5,3]
#key=17
#o/p: 5 and 12
a=[1,6,12,17,5,3]
key=17
a1=sorted(a)
i=0
j=len(a1)-1
while(i<j):
    if a1[i]+a1[j]==key:
        print(a1[i],a1[j])
        break
    if a1[i]+a1[j]<key:
        i+=1
    else:
        j-=1
else:
    print("not found")
        
        
