# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nlist1=[]
        nlist2=[]
        while list1:
            nlist1.append(list1.val)
            list1=list1.next
        while list2:
            nlist2.append(list2.val)
            list2=list2.next
        n=nlist1+nlist2
        n.sort()
        dummy=ListNode()
        list3=dummy
        for i in n:
            dummy.next=ListNode()
            dummy=dummy.next
            dummy.val=i
        return list3.next
