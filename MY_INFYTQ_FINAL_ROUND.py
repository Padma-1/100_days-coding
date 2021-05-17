##CONSIDER A NON-ZERO POSITIVE NUMBER, INNUM , AN INTEGER INBASE GREATER THAN 1 AND PRINT OUTNUM.
#THE MAXIMUM NUMBER OF CONSECUTIVE SET OF ZEROES AFTER CONVERTING INNUM TO ITS INBASE NOTATION
# PRINT -1 IF THERE EXISTS NO ZERO AFTER CONVERSION OF INNUM
"""in_num=int(input())
in_base=int(input())
temp=[]
while in_num>0:
    temp.append(in_num%2)
    in_num=in_num//2#in temp we get reversed base converted result
if temp.count(0)==0:
    print(-1)
else:
    c=0
    out_num=0
    for i in temp:
        if i!=0:
            c=0
        else:
            c+=1
            out_num=max(c,out_num)
    print(out_num)"""


#=====================================================================================================================================================================

##CONSIDER TWO NON EMPTY INPUT LISTS INLIST1 AND INLIST 2 EACH CONTAINING UNIQuE INTEGERS
##IDENTIFY AND PRINT OUTLIST BASED ON THE LOGIC BELOW
##CHECK THE SUM OF ELEMENTS OF EACH OF THE INPUT LISTS INLIST1 AND INLIST2.
#if THERE SUMS ARE NOT EQUAL
##IDENTIFY PAIRS OF NUMS,(NUM1,NUM2) WHERE NUM1 FROM INLIST1 AND NUM2 FROM INLIST2 SUCH THAT SWAPPED BETWEEN INLIST1 AND INLIST2,
##THE SUM OF ELEMENTS IN EACH OF THE LISTS, INLIST1 AND INLIST2 ARE EQUAL
##FIND THE PRODUCT OF NUM1 AND NUM2 FOR EACH OF THE IDENTIFIED PAIRS
##ADD THE NUMBERS, NUM1 FOLLOWED BY NUM2 , IN THE PAIRS (NUM1,NUM2) TO OUTLIST IN THEIR ASCENDING ORDER OF EVEN PRODUCT(if any)
##FOLLOWED BY THE NUMBERS IN THE PAIRS WITH ODD PRODUCTS(if any) IN DESCENDING ORDER
##PRINT -1 IF NO SUCH PAIR OF NUMBER EXISTS OR THE GIVEN INPUT LISTS HAVING THE SAME SUM# CONSIDER 0 AS AN EVEN NUMBER
"""in_list1=sorted(list(map(int,input().split())))#[1,2,3,4,5,9,14]
in_list2=sorted(list(map(int,input().split())))#[1,2,3,7,9,12]
r1=[]
r2=[]
if sum(in_list1)==sum(in_list2):
    print(in_list1)
else:
    for i in range(len(in_list1)):
        for j in range(len(in_list2)):
            a=in_list1.copy()#hence changes in a and b not reflect in inlists
            b=in_list2.copy()
            a[i],b[j]=b[j],a[i]#swapping nums between inlist1 and inlist2
            if sum(a)==sum(b):
                if ((a[i]*b[j])%2)==0:#checking for even product
                    #print(a[i],b[j])#2 4, 12 14-->products in ascending order not num1 and num2
                    r1.append(b[j])
                    r1.append(a[i])
                else:#checking for odd product
                    #print(a[i],b[j])#1 2,3 5,7 9
                    r2.append(b[j])
                    r2.append(a[i])
                   
res=r1+r2[::-1]
if len(res)!=0:
    for i in range(len(res)-1):
        print(res[i],end=",")
    print(res[-1])
else:
    print(-1)"""
#####
###input:
##9 2 4 14 5 1 3
##1 12 7 9 2 3
###output:
##4,2,14,12,7,9,3,5,1,3

                
#=====================================================================================================================================================    
    
    
##GIVEN AN INTEGER IN_NUM GREATER THAN 1 AND PRINT OUT_NUM SUCH THAT :
#THE SUM OF NUM1 AND NUM2 IS A PALINDROME,
#WHERE NUM1 IS THE LARGEST PALINDROME SMALLER THAN IN_NUM, NUM2 IS THE SMALLEST PALINDROME GREATER THAN IN_NUM
#IF SUM IS NOT A PALINDROME, REPEAT THE ABOVE STEP BY DECREMENTING INNUM BY 1 UNTIL INNUM IS NOT ZERO #for input:4-->a=3 and b=4 ==>sum=7 is a palindrome
"""def is_palindrome(n):
    if str(n)==str(n)[::-1]:
        return True
    else:
        return False
in_num=int(input())
while True:
    temp=in_num
    while temp>0:
        temp-=1
        if is_palindrome(temp)==True:
            a=temp
            break
    print(a)
    j=0
    while True:
        in_num+=1
        if is_palindrome(in_num)==True:
            b=in_num
            break
        j+=1
    print(b)
    if is_palindrome(a+b)==True:
        print(a+b)
        break
    else:
        in_num-=1"""

##CONSIDER TWO NON EMPTY INPUT LISTS INLIST1 AND INLIST 2 EACH CONTAINING UNIQuE INTEGERS
##IDENTIFY AND PRINT OUTLIST BASED ON THE LOGIC BELOW
##CHECK THE SUM OF ELEMENTS OF EACH OF THE INPUT LISTS INLIST1 AND INLIST2.
#if THERE SUMS ARE NOT EQUAL
##IDENTIFY PAIRS OF NUMS,(NUM1,NUM2) WHERE NUM1 FROM INLIST1 AND NUM2 FROM INLIST2 SUCH THAT SWAPPED BETWEEN INLIST1 AND INLIST2,
##THE SUM OF ELEMENTS IN EACH OF THE LISTS, INLIST1 AND INLIST2 ARE EQUAL
##FIND THE PRODUCT OF NUM1 AND NUM2 FOR EACH OF THE IDENTIFIED PAIRS
##ADD THE NUMBERS, NUM1 FOLLOWED BY NUM2 , IN THE PAIRS (NUM1,NUM2) TO OUTLIST IN THEIR ASCENDING ORDER OF EVEN PRODUCT(if any)
##FOLLOWED BY THE NUMBERS IN THE PAIRS WITH ODD PRODUCTS(if any) IN DESCENDING ORDER
##PRINT -1 IF NO SUCH PAIR OF NUMBER EXISTS OR THE GIVEN INPUT LISTS HAVING THE SAME SUM# CONSIDER 0 AS AN EVEN NUMBER
"""in_list1=sorted(list(map(int,input().split())))#[1,2,3,4,5,9,14]
in_list2=sorted(list(map(int,input().split())))#[1,2,3,7,9,12]
r1=[]
r2=[]
if sum(in_list1)==sum(in_list2):
    print(in_list1)
else:
    for i in range(len(in_list1)):
        for j in range(len(in_list2)):
            a=in_list1.copy()#hence changes in a and b not reflect in inlists
            b=in_list2.copy()
            a[i],b[j]=b[j],a[i]#swapping nums between inlist1 and inlist2
            if sum(a)==sum(b):
                if ((a[i]*b[j])%2)==0:#checking for even product
                    #print(a[i],b[j])#2 4, 12 14-->products in ascending order not num1 and num2
                    r1.append(b[j])
                    r1.append(a[i])
                else:#checking for odd product
                    #print(a[i],b[j])#1 2,3 5,7 9
                    r2.append(b[j])
                    r2.append(a[i])
                   
res=r1+r2[::-1]
if len(res)!=0:
    for i in range(len(res)-1):
        print(res[i],end=",")
    print(res[-1])
else:
    print(-1)"""
#####
###input:
##9 2 4 14 5 1 3
##1 12 7 9 2 3
###output:
##4,2,14,12,7,9,3,5,1,3

            
    
    
    
    
    
    
    

        




































