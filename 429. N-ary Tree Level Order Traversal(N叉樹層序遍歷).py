from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res=[]
        temp=[]
        queue=deque([root])
        def bfs(root):
            nonlocal res,temp,queue
            while queue:
                for _ in range(len(queue)):
                    node=queue.popleft()
                    temp.append(node.val)
                    for child in node.children:
                        queue.append(child)
                res.append(temp)
                temp=[]
        bfs(root)
        return res
