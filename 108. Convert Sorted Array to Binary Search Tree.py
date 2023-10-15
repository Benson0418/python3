# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l,r):  
            if l>r:
                return
            mid=(l+r)//2
            res=TreeNode(nums[mid])
            res.left=dfs(l,mid-1)
            res.right=dfs(mid+1,r)
            return res
        return dfs(0,len(nums)-1)
