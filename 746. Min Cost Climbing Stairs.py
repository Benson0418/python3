class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[0]*n
        for i in range(n-1,-1,-1):
            if i+2>=n:
                dp[i]=cost[i]
            else:
                dp[i]=min(dp[i+1],dp[i+2])+cost[i]
        return min(dp[0],dp[1])
