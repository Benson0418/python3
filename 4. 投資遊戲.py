n,k=map(int,input().split())
profit=[int(x) for x in input().split()]
dp_prev=[0]*n
dp_curr=[0]*n

dp_prev[0]=max(0,profit[0])
for i in range(1,n):
    dp_prev[i]=max(0,dp_prev[i-1]+profit[i])

for _ in range(k):
    dp_curr[0]=dp_prev[0]
    for j in range(1,n):
        dp_curr[j]=max(dp_curr[j-1]+profit[j],dp_prev[j-1]) #max(不使用金牌,使用金牌)
    dp_curr,dp_prev=dp_prev,dp_curr

print(max(dp_prev))
