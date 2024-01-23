P=1000000009
n=int(input())
dp=[1]+[0]*n
for i in range(1,n+1):
    dp[i]=0
    for j in range(i):
        dp[i]+=(dp[j]*dp[i-1-j])%P
    dp[i]%=P
print(dp[n])

