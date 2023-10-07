class Solution:
    # all set to -k. Then +2k from small to large
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums = sorted([x-k for x in nums]) # all -k
        k += k # 2k
        maxi = nums[-1]
        result = maxi - nums[0]
        temp = nums[0]+k # cannot smaller than 
        for e in nums:
            if e>=temp: 
                result = min(result,maxi-temp)
                break
            result = min(result,maxi-e)
            maxi = max(maxi,e+k)
        return result
