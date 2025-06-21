n=int(input())
L=[int(x) for x in input().split()]
if n==1:
    print(L[0])
elif n==2:
    print(min(L[0],L[1]))
else:
    dp=[0]*n
    dp[0]=L[0]
    dp[1]=L[1]
    dp[2]=L[2]+min(dp[1],dp[0])
    for k in range(3,n):
        dp[k]=L[k]+min(dp[k-1],dp[k-2],dp[k-3])
    print(min(dp[-1],dp[-2]))
