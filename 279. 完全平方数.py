class Solution:
    def numSquares(self, n: int) -> int:
      dp=[0]*(n+1)
      perfect=[]
      for i in range(1,n+1):
        x=i**(1/2)
        if x==int(x):
          dp[i]=1
          perfect.append(i)
        else:
          result=float('inf')
          for j in range(len(perfect)-1,-1,-1):
            result=min(result,dp[i-perfect[j]]+1)
          dp[i]=result
      return dp[-1]
