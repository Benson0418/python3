# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        temp=[]
        dummy=head
        while head:
            temp.append(head.val)
            head=head.next
        head=dummy
        for i in range(len(temp)-1,-1,-1):
            dummy.val=temp[i]
            dummy=dummy.next
        return head
