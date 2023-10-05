class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maximum=0
        left=right=0
        lenn=0
        e=0
        flag=False
        while right<n and left+lenn<n:
            if e<0:
                e=0
                lenn=0
                left=right
            else:
                e+=nums[right]
                maximum=max(maximum,e)
                lenn+=1
                right+=1
        for i in nums:
            if i>=0:
                flag=True
                break
        if not flag:
            return max(nums)
        return maximum
            
