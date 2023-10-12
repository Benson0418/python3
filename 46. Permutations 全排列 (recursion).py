class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        def backtrack(curr,remaining):
            if remaining==0:
                result.append(path.copy())
            for i in range(len(curr)):
                path.append(curr[i])
                backtrack(curr[:i]+curr[i+1:],remaining-1)
                path.remove(curr[i])
        backtrack(nums,len(nums))
        return result
            

