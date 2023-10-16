class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        res=0
        stack=[] 
        for i,h in enumerate(heights):
            temp=i
            while stack and stack[-1][1]>h:
                x,y=stack.pop()
                res=max(res,y*(i-x))
                temp=x
            stack.append((temp,h))
        for a,b in stack:
            res=max(res,b*(n-a))
        return res
