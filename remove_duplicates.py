#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
a=[0,0,1,1,1,2,2,3,3,4]
#a=[1,1,2]
i=0
j=1
while(i<j):
    if(j==len(a)):
            print(a)
            break
    if a[i]==a[j]:
        a.pop(i)
    else:
        i+=1
        j+=1
