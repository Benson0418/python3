# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def post_order(root):
            if not root:
                return (0,0)
            l=post_order(root.left)
            r=post_order(root.right)
            with_root=root.val+l[1]+r[1]
            without_root=max(l)+max(r)
            return (with_root,without_root)
        a=post_order(root)
        return max(a)
