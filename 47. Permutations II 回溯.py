class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        def DFS(curr,remaining):
            if remaining==0:
                result.append(path.copy())
                return
            hashmap=set()
            for i in range(len(curr)):
                if curr[i] in hashmap:
                    continue
                path.append(curr[i])
                hashmap.add(curr[i])
                DFS(curr[:i]+curr[i+1:],remaining-1)
                path.pop()
        DFS(nums,len(nums))
        return result
