class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]
        for a,b in enumerate(temperatures):
            while stack and stack[-1][1]<b:
                x=stack.pop()[0]
                res[x]=a-x
            stack.append((a,b))
        return res
