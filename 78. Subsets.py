class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[[]]
        for i in nums:
            new_subsets=[j+[i] for j in result]
            result.extend(new_subsets)
        return result
