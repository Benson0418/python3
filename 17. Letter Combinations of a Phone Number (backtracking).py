class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        L={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        res=[]
        def backtracking(count,path):
            if count==len(digits):
                res.append(path)
                return
            for i in L[digits[count]]:
                backtracking(count+1,path+i)
        backtracking(0,'')
        return res
