class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        path=[]
        def backtracking(idx,tar):
            if tar==0:
                res.append(path.copy())
                return
            for i in range(idx,len(candidates)):
                if candidates[i]>tar:
                    return
                path.append(candidates[i])
                backtracking(i,tar-candidates[i])
                path.pop()
        backtracking(0,target)
        return res
