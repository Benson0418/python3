N,M,D=map(int,input().split())
dp=[[False]*(D+1) for _ in range(3)]
for i in dp:i[0]=True
for j in range(1,D+1):
    if dp[0][j]:
        dp[1][j]=True
    elif j<N:
        continue
    else:
        dp[1][j]=dp[1][j-N]
for j in range(1,D+1):
    if dp[1][j]:
        dp[2][j]=True
    elif j<M:
        continue
    else:
        dp[2][j]=dp[2][j-M]
if dp[2][D]:
    print("YES")
else:
    print("NO")
