class Node:
    def __init__(self, val=0, pre=None, next=None):
        self.val=val
        self.pre=pre
        self.next=next

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __str__(self):
        if self.head is None:
            return "empty"
        result=[]
        curr=self.head
        while curr:
            result.append(str(curr.val))
            curr=curr.next
        return " <-> ".join(result)

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def append(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.pre=self.tail
            self.tail=node

    def preappend(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.head.pre=node
            node.next=self.head
            self.head=node

    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty doubly linked list")
        else:
            res=self.tail.val
            if self.tail.pre is None:
                self.head=None
                self.tail=None
            else:
                self.tail=self.tail.pre
                self.tail.next=None
            return res
    def prepop(self):
        if self.head is None:
            raise IndexError("prepop from empty doubly linked list")
        else:
            res=self.head.val
            if self.head.next is None:
                self.head=None
                self.tail=None
            else:
                self.head=self.head.next
                self.head.pre=None
            return res

    def clear(self):
        self.head=None
        self.tail=None

    def popindex(self, idx):
        curr=self.head
        for i in range(idx):
            if curr.next is None:
                raise IndexError("index out of range")
            curr=curr.next
        pass
    
    def index(self, idx):
        pass

    def delete(self, value):
        pass

    def reverse(self):
        pass

    def getlength(self):
        curr=self.head
        res=0
        while curr is not None:
            res+=1
            curr=curr.next
        return res

DLL=DoublyLinkedList()
DLL.append(Node(5))
DLL.append(Node(4))
DLL.append(Node(9))
DLL.append(Node(13))
DLL.preappend(Node(15))
print(DLL.pop())
print(DLL.prepop())
print(DLL.head.val)
print(DLL.tail.val)
print(DLL)
print(DLL.getlength())
DLL.clear()
print(DLL)
