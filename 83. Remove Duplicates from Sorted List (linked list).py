# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        di=-999
        dummy=head
        if not head:
            return None
        while True:
            if head.val!=di:
                di=head.val
                current=head
            else:
                current.next=head.next
            if not head.next:
                break
            head=head.next
        return dummy
