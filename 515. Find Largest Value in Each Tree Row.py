from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        queue=deque()
        queue.append(root)
        while queue:
            lenq=len(queue)
            temp=float('-inf')
            for _ in range(lenq):
                x=queue.popleft()
                temp=max(temp,x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            res.append(temp)
        if res[-1]==float('-inf'):
            res.pop()
        return res
