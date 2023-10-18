class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1, amount+1):
            l=float('inf')
            for c in coins:
                if i-c>=0:
                    l=min(dp[i-c]+1,l)
            dp[i]=l
        return dp[-1] if dp[-1]!=float('inf') else -1
