from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res=[]
        temp=[]
        queue=deque([root])
        def bfs(root):
            nonlocal res,temp,queue
            while queue:
                for _ in range(len(queue)):
                    new=queue.popleft()
                    temp.append(new.val)
                    if new.left:
                        queue.append(new.left)
                    if new.right:
                        queue.append(new.right)
                res.append(temp)
                temp=[]
        bfs(root)
        return res
                
