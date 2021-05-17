arr=list(map(int,input().split()))#[2,5,3,6,4,8,7]-->alternate up's and down's
up_state=0
down_state=0
if arr[0]>arr[1]:
    down_state=1
if arr[0]<arr[1]:
    up_state=1
for i in range(1,len(arr)-1):
    if up_state==1:
        if arr[i]>arr[i+1]:
            down_state=1#
            up_state=0
        else:
            print("not bouncy")
            break
    else:
        if down_state==1:
            if arr[i]<arr[i+1]:
                up_state=1
                down_state=0
            else:
                print("not bouncy")
                break
else:
    print("bouncy array")
            
    
