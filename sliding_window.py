#sliding window
#eg:[1,2,4,5,6,8] find max.subarray with length 2
"""a=[1,2,4,5,6,8,2,3,4]
res=0
i=0
j=1
res=0
while(j!=len(a)):
    c=a[i]+a[j]
    if c>=res:
        res=c
    i+=1
    j+=1
print(res)"""


a=[1,2,4,5,6,8]
key=9
for i in range(len(a)-1):
    j=i
    if a[i]<key:
        j+=1
        res=a[i]+a[j]
        if res==key:
            print(a[i],a[j])
        elif res<key:
            j+=1
        else:
             res-=a[i]
             i+=1
    if a[i]==key:
        print(a[i])"""

