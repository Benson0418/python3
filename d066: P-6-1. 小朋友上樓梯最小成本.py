n=int(input())
L=[0]+[int(x) for x in input().split()]
if n==1:
    print(L[1])
elif n==2:
    print(L[2])
else:
    dp=[0]*(n+1)
    dp[1]=L[1]
    dp[2]=L[2]
    for i in range(3,n+1):
        dp[i]=min(dp[i-1],dp[i-2])+L[i]
    print(dp[-1])
