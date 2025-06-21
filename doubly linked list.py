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

    def popindex(self, idx): #idx>=0
        curr=self.head
        for i in range(idx):
            if curr.next is None:
                raise IndexError("index out of range")
            curr=curr.next
        res=curr.val
        if idx==0:
            self.head=self.head.next
            if self.head:
                self.head.pre=None
        else:
            curr.pre.next=curr.next
            curr=curr.pre
            if curr.next:
                curr.next.pre=curr.pre
        return res
    
    def index(self, idx):
        curr=self.head
        for i in range(idx):
            if curr.next is None:
                raise IndexError("index out of range")
            curr=curr.next
        return curr.val

    def remove(self, value):
        curr = self.head
        while curr:
            if curr.val == value:
                if curr.pre is None:
                    if curr.next:
                        self.head = curr.next
                        self.head.pre = None
                    else:
                        self.head = None
                        self.tail = None
                else:
                    curr.pre.next = curr.next
                    if curr.next:
                        curr.next.pre = curr.pre
                return
            curr = curr.next

    def reverse(self):
        self.head,self.tail=self.tail,self.head
        curr=self.head
        while curr:
            curr.pre,curr.next=curr.next,curr.pre
            curr=curr.next
        
    def getlength(self):
        curr=self.head
        res=0
        while curr is not None:
            res+=1
            curr=curr.next
        return res

DLL=DoublyLinkedList()
DLL.append(Node(5))
DLL.remove(5)
print(DLL)
DLL.append(Node(5))
print(DLL)
DLL.append(Node(4))
DLL.append(Node(9))
DLL.append(Node(13))
DLL.append(Node(19))
DLL.append(Node(21))
DLL.preappend(Node(15))
print(DLL)
DLL.reverse()
print(DLL)


