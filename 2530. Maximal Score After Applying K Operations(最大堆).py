import heapq
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i]*=-1
        heapq.heapify(nums)
        res=0
        for _ in range(k):
            res-=heapq.heapreplace(nums,nums[0]//3)
        return res
    
