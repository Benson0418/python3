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
        path=deque([root])
        def bfs(root):
            nonlocal res,temp,path
            while path:
                for _ in range(len(path)):
                    new=path.popleft()
                    temp.append(new.val)
                    if new.left:
                        path.append(new.left)
                    if new.right:
                        path.append(new.right)
                res.append(temp)
                temp=[]
        bfs(root)
        return res
                
