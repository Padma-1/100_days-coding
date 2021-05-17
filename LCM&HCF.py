#LCM OF two NUMBERs
"""
n,m=map(int,input().split())
temp=max(n,m)
t=temp
while True:
    if t%n==0 and t%m==0:
        print(t)
        break
    else:
        t=t+temp
"""

#LCM ##C++
"""#include<iostream>;
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int temp=max(n,m);
    int t=temp;
    while (true)
    {
        if ((t%n==0) && (t%m==0))
        {
            cout<<t;
            break;
        }
        else
        {
            t+=temp;
        }
    }
    return 0;
}
"""

#HCF OF TWO NUMBERS
"""n,m=map(int,input().split())
temp=min(n,m)
for i in range(temp,0,-1):
    if n%i==0 and m%i==0:
        print(i)
        break
"""

#HCF#C++
"""#include<iostream>;
using namespace std;
int main()
{
    int n,m;
    cin>>n>>m;
    int temp=min(n,m);
    for(int i=temp;i>0;i--)
    {
        if ((n%i==0) && (m%i==0))
        {
            cout<<i;
            break;
        }
    }
    return 0;
}
"""

