class Solution:
    def jump(self, nums: List[int]) -> int:
      if len(nums)==1:
        return 0
      n=len(nums)
      count=0
      jump=0
      while jump<n:
        count+=1
        far=0
        idx=0
        for i in range(jump+1,jump+nums[jump]+1):
          if i==n-1:
            return count
          if i+nums[i]>=far:
            far=i+nums[i]
            idx=i
        jump=idx
