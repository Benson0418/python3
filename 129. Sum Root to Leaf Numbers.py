# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        path = []
        def DFS(root):
            nonlocal res
            path.append(root.val)
            if not root.left and not root.right:
                res += int("".join([str(i) for i in path]))
            else:
                if root.left:
                    DFS(root.left)
                if root.right:
                    DFS(root.right)
            path.pop()
        DFS(root)
        return res
