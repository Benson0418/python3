from math import gcd
N,M,Q=map(int,input().split())
g=gcd(N,M)
l=N*M//g
L=[int(x) for x in input().split()]
dp=[False]*(l+1)
dp[0]=True
for i in range(1,l+1):
    if i-N<0 and i-M<0:
        continue
    elif i-N>=0:
        if dp[i-N]:
            dp[i]=True
    if i-M>=0:
        if dp[i-M]:
            dp[i]=True
for i in L:
    if i>=l:
        print('YES' if i%g==0 else 'NO')
        continue
    print('YES' if dp[i] else 'NO')
    


            

    


