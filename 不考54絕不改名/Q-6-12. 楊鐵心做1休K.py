n,K=map(int,input().split())
dp=[0]*(K+1)+[int(x) for x in input().split()]
for i in range(K+1,n+K+1):
    dp[i]=max(dp[i-K-1]+dp[i],dp[i-1])
print(dp[-1])
