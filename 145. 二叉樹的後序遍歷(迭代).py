# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
      
class Solution1: # 前序遍歷的變形，但是倒轉
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[root]
        res=[]
        while stack:
            x=stack.pop()
            res.append(x.val)
            if x.left:
                stack.append(x.left)
            if x.right:
                stack.append(x.right)
        return res[::-1]

class Solution2:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack=[]
        res=[]
        while stack or root: # 確定為stack[-1]為葉節點
            while root:
                stack.append(root)
                if root.left:
                    root=root.left
                else:
                    root=root.right
            x=stack.pop()
            res.append(x.val)
            if stack and stack[-1].left==x: # 若當初為左子樹來的，就改為遍歷右子樹，否則繼續彈出上一個節點
                root=stack[-1].right
            else:
                root=None
        return res

        
