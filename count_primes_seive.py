"""Count the number of prime numbers less than a non-negative number, n.LEET CODE
Example 1:
----------
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example:2
----------
IF input:n=0 or 1
output:0"""
"""class Solution:
    def countPrimes(self, n: int) -> int:
        seive=[1 for i in range(n+1)]#as to start from 0 to n
        def seivegen():
            i=2
            while(i*i<=n):
                if seive[i]==1:
                    for j in range(i*i,n+1,i):
                        seive[j]=0
                i+=1
            seive[0]=0
            if n>0:
              seive[1]=0
        seivegen()
        count=0
        for i in range(1,n):
            if seive[i]==1:
                count+=1
        return count
        
"""
n=int(input())
seive=[1 for i in range(n+1)]#as to start from 0 to n
def seivegen():
    i=2
    while(i*i<=n):
        if seive[i]==1:
            for j in range(i*i,n+1,i):
                seive[j]=0
        i+=1
    seive[0]=0
    if n>0:
      seive[1]=0
seivegen()
count=0
for i in range(1,n):
    if seive[i]==1:
        count+=1
print (count)
print(seive)
        
