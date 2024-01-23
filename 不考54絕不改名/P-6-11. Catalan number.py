#解1
P=1000000009
n=int(input())
dp=[1]+[0]*n
for i in range(1,n+1):
    dp[i]=0
    for j in range(i):
        dp[i]+=(dp[j]*dp[i-1-j])%P
    dp[i]%=P
print(dp[n])


#解2
P=1000000009
from functools import lru_cache

@lru_cache(maxsize=None)
def Catalan_number(n):
    global P
    if n==0:
        return 1
    res=0
    for i in range(n):
        res+=(Catalan_number(i)*Catalan_number(n-1-i))%P
    return res%P

print(Catalan_number(int(input())))
    


