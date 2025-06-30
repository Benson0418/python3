class Node:
    def __init__(self, key = 0, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1


class AVLTree:
    
    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # 平衡因子
    def get_bf(self, node):
        """
        平衡因子：左子樹高減右子樹高，絕對值大於1為失衡
        """
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_left(self, root):
        """
        左旋，右子樹根當新根，原根節點變為右子樹，衝突的左孩變右孩
        """
        #右孩當新根
        new_root = root.right
        
        # left subtree of new root
        temp = new_root.left
        new_root.left = root
        root.right = temp
        self.update_height(root)
        self.update_height(new_root)
            
        return new_root
    
    def rotate_right(self, root):
        """
        右旋，左子樹根當新根，原根節點變為左子樹，衝突的右孩變左孩
        """
        #左孩當新根
        new_root = root.left

        #right subtree of new root
        temp = new_root.right
        new_root.right = root
        root.left = temp
        self.update_height(root)
        self.update_height(new_root)
        
        return new_root

    def insert(self, root, key):
        """
        節點插入後，若祖先節點失衡，會有四種情況
        LL型:失衡節點平衡因子等於2，且左子節點平衡因子等於1
            右旋失衡節點
        RR型:失衡節點平衡因子等於-2，且右子節點平衡因子等於-1
            左旋祖先節點
        LR型:失衡節點平衡因子等於2，且左子節點平衡因子等於-1
            左旋左子節點，接著右旋失衡節點
        RL型:失衡節點平衡因子等於-2，且右子節點平衡因子等於1
            右旋右子節點，接著左旋失衡節點
        """
        if root==None:
            return Node(key)
        if key>root.key:
            root.right = self.insert(root.right, key)
        else:
            root.left = self.insert(root.left, key)

        self.update_height(root)

        bf = self.get_bf(root)

        if bf>1: 
            if self.get_bf(root.left)>0: #LL型
                return self.rotate_right(root)
            else: #LR型
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            
        elif bf<-1:
            if self.get_bf(root.right)<0: #RR型
                return self.rotate_left(root)
            else: #RL型
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def find_decessor(self, root):
        """當有左子樹時，找predecessor"""
        curr = root.left
        while curr.right:
            curr = curr.right
        return curr
        
    def erase(self, root, key):
        """
        刪除一個節點時，若該節點僅有其中一種子樹或兩邊子樹為空
        直接將該點刪除，後續子樹替補
        
        若該節點有左右子樹，找到他的前驅節點，將前驅節點與待刪除節點值交換
        採相同方式刪除前驅節點即可
        刪除節點後，沿路返回調整祖先節點的平衡
        """

        if root==None:
            return root

        if root.key>key:
            root.left = self.erase(root.left, key)
        elif root.key<key:
            root.right = self.erase(root.right, key)
        else:
            if root.left==None:
                return root.right
            elif root.right==None:
                return root.left
            else:
                predecessor = self.find_decessor(root)
                # 兩數交換
                predecessor.key^=root.key
                root.key^=predecessor.key
                predecessor.key^=root.key
                
                root.left = self.erase(root.left, key)

        self.update_height(root)
        bf = self.get_bf(root)

        if bf>1: 
            if self.get_bf(root.left)>0: #LL型
                return self.rotate_right(root)
            else: #LR型
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)
            
        elif bf<-1:
            if self.get_bf(root.right)<0: #RR型
                return self.rotate_left(root)
            else: #RL型
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root
                
                

    # 前序遍歷
    def preorder(self, root):
        if root:
            print(root.key,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key,end=" ")
            self.inorder(root.right)

        


avl=AVLTree()
root = None
keys = [14, 9, 5, 17, 11, 12, 7, 19, 16, 27]
for key in keys:
    root = avl.insert(root, key)

avl.preorder(root)
print()
avl.inorder(root)

print()
avl.erase(root,17)
avl.erase(root,19)
avl.erase(root,12)
avl.inorder(root)
