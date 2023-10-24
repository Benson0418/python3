class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right


def insert(node,new_val):
    if not node:
        return TreeNode(new_val)
    if node.val>new_val:
        node.left=insert(node.left,new_val)
    else:
        node.right=insert(node.right,new_val)
    return node
        
tree=TreeNode(int(input()))

while True:
    try:
        n=int(input())
    except EOFError:
        break
    tree=insert(tree,n)


def post_order(tree):
    if not tree:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.val)
    return
post_order(tree)
    
