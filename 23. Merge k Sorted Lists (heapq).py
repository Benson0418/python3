# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h=[]
        for i in lists:
            while i:
                heapq.heappush(h,i.val)
                i=i.next
        dummy=curr=ListNode(0)
        while h:
            curr.next=ListNode(heapq.heappop(h))
            curr=curr.next
        return dummy.next
