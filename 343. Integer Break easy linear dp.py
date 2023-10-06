class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[0]*(n+1)
        if n==2:
            return 1
        elif n==3:
            return 2
        dp[2]=1
        dp[3]=2
        for i in range(4,n+1):
            a,b=1,i-1
            res=set()
            while a<=b:
                res.add(max(dp[a],a)*max(dp[b],b))
                a+=1
                b-=1
            dp[i]=max(res)
        return dp[-1]
