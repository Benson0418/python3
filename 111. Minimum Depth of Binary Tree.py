from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue=deque()
        res=0
        queue.append(root)
        while queue:
            res+=1
            lenq=len(queue)
            flag=False
            for _ in range(lenq):
                x=queue.popleft()
                if x.left or x.right:
                    if x.left:
                        queue.append(x.left)
                    if x.right:
                        queue.append(x.right)
                else:
                    flag=True
                    break
            if flag:
                break
        return res
        
