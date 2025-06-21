m,n=map(int,input().split())
L=[[int(x) for x in input().split()] for _ in range(m)]
dp=L[0]
for i in range(1,n):
    dp[i]+=dp[i-1]
for i in range(1,m):
    dp[0]+=L[i][0]
    for j in range(1,n):
        dp[j]=max(dp[j-1],dp[j])+L[i][j]
print(dp[-1])
    
        
