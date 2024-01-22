n,t=map(int,input().split())
L=[tuple(map(int,input().split())) for _ in range(n)]

dp=[[0,0]for _ in range(n)]
dp[0][0],dp[0][1]=abs(L[0][0]-t),abs(L[0][1]-t)
for i in range(1,n):
    dp[i][0]=min(abs(L[i-1][0]-L[i][0])+dp[i-1][0],abs(L[i-1][1]-L[i][0])+dp[i-1][1])
    dp[i][1]=min(abs(L[i-1][0]-L[i][1])+dp[i-1][0],abs(L[i-1][1]-L[i][1])+dp[i-1][1])
print(min(dp[-1]))
