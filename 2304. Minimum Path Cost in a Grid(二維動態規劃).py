class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        dp=[]
        for i in range(len(grid)):
            dp.append(grid[i].copy())
        for i in range(1,len(grid)):
            for j in range(len(grid[0])):
                temp=[]
                for k in range(len(grid[0])):
                    temp.append(dp[i-1][k]+moveCost[grid[i-1][k]][j])
                dp[i][j]+=min(temp)
        return min(dp[-1])
