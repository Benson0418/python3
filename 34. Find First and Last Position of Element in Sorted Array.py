from bisect import bisect_left, bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        a = bisect(nums, target)
        if a == 0 or nums[a-1] != target:
            return [-1,-1]
        return [bisect_left(nums, target), a-1]
