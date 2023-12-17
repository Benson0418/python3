# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue=deque([root])
        res=float('-inf')
        level=0
        cur_level=0
        while queue:
            cur_level+=1
            level_res=0
            for i in range(len(queue)):
                r=queue.popleft()
                level_res+=r.val
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
            if res<level_res:
                res=level_res
                level=cur_level
        return level
                
        
