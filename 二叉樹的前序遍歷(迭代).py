# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            x=stack.pop()
            res.append(x.val)
            if x.right:
                stack.append(x.right)
            if x.left:
                stack.append(x.left)
        return res
            
