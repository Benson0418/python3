# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution_1: 
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      res=0
      def dfs(root,idx):
        nonlocal res
        if not root:
          return 
        res=max(res,idx+1)
        dfs(root.left,idx+1)
        dfs(root.right,idx+1)
      dfs(root,0)
      return res

class Solution_2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))
