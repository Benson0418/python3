class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=0
        b=float('-inf')
        l=r=0
        temp=0
        while r<len(nums):
            b=max(b,nums[r])
            if temp+nums[r]<=0:
                l=r=r+1
                temp=0
            else:
                temp+=nums[r]
                r+=1
                res=max(res,temp)
        return b if b<0 else res
