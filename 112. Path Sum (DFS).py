class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sum):
            if not root:
                return False
            sum+=root.val
            if not root.left and not root.right:
                return sum==targetSum
            return dfs(root.left,sum) or dfs(root.right,sum)
        return dfs(root,0)

# 以下的程式碼為初稿，程式寫的不規範，所以又寫了一個優化版本
# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val=val
#         self.left=left
#         self.right=right
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         if not root:
#             return False
#         flag=False
#         def dfs(root,res):
#             nonlocal flag,targetSum
#             if flag:
#                 return
#             res+=root.val
#             if not root.left and not root.right:
#                 if res==targetSum:
#                     flag=True
#                     return
#             if root.left:
#                 dfs(root.left,res)
#             if root.right:
#                 dfs(root.right,res)
#             return
#         dfs(root,0)
#         return flag
