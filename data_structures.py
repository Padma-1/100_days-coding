"""s="[[[{]]]"
a=['(','[','{']
b=[']','}',')']
stack=[]
for i in range(len(s)):
    if s[i] in a:
        stack.append(s[i])
    print(stack)
    if stack!=[] and s[i] in b :
        if (stack[-1]=='[') and (s[i]==']'):
            stack.pop()
        elif (stack[-1]=='{') and (s[i]=='}'):
            stack.pop()
        elif (stack[-1]=='(') and (s[i]==')'):
            stack.pop()
print(stack)
if len(stack)==0:
    print (True)
else:
    print (False)
    """
#1 2 -2 -1 3 3 2 -2 -3 -3 -4 5 -5
#10
#longest subarray having balenced paranthesis
arr=list(map(int,input().split()))
arr.insert(0,0)
stack=[]
stack.append(0)
len1=0
for i in range(1,len(arr)):
    if arr[i]>0:
        stack.append(i)
    if (arr[stack[-1]]==-1*arr[i]):
        stack.pop()
        len1=max(len1,i-stack[-1])
    else:
        stack.append(i)
print(len1)      
        
        
            
    
    
    
