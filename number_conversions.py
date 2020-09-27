###binary_to_decimal-->int('111',2)=7
##def bin_to_dec(n):
##    i=0
##    sum=0
##    while n:
##        r=n%10
##        sum+=r*2**i
##        i+=1
##        n=n//10
##    return sum
##n=int(input())
##print(bin_to_dec(n))
##
###method 2
##n=int(input())#111
##base=1#2^0
##dec=0
##while n:
##    r=n%10#1
##    n=n//10#11
##    dec+=r*base#1
##    base=base*2#2
##print(dec)
##
##decimal_to_binary-->bin(8)='0b1000'
##def dec_to_bin(n):
##    l=[ ]
##    while n:
##        x=n%2
##        n=n//2
##        l.append(x)
##    l = l[ :: -1]#-->to get binary representation [1, 0, 1, 0]
##    for i in l:
##       print(i,end="")#1010
##n=int(input())#10
##dec_to_bin(n)

#Octal_to_decimal-->int('123',8)=83
##def oct_to_decimal(n):
##    i=0
##    sum=0
##    while n:
##        r=n%10
##        sum+=r*8**i
##        i+=1
##        n=n//10
##    return sum
##n=int(input())
##print(oct_to_decimal(n))


#Decimal_to_octal-->oct(33)='0o41'
##def dec_to_oct(n):
##    l=[ ]
##    while n:
##        x=n%8
##        n=n//8
##        l.append(x)
##    l = l[ :: -1]
##    for i in l:
##       print(i,end="")
##n=int(input())
##dec_to_oct(n)

###decimal to hexadecimal
##n=int(input())#2545
##hex_val=""
##while n:
##    rem=n%16#2545%16=1-->159%16=15-->9%16=9
##    if rem<=9:#T
##        hex_val+=chr(48+rem)#'1'#1F9
##    else:
##        hex_val+=chr(55+rem)#55+15=70=F
##    n=n//16#159-->9-->0
##print(hex_val[ ::-1])

#hexadecimal to decimal
s=input()
dec_val=0
base = 1
l= s[ ::-1]
for i in l:
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        dec_val+=int(i)*base
    else:
        dec_val+=(ord(i)-55)*base
        
    base=base*16
print(dec_val)

        

