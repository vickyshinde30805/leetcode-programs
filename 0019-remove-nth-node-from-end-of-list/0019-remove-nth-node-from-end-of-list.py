# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy=ListNode(0,head)
        slow=fast=dummy
        for _ in range(n+1):
            fast=fast.next
        while fast:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next








        """curr=head
        l=0
        while curr:
            l+=1
            curr=curr.next

        if n==l:
            return head.next
        steps=l-n-1
        curr=head
        for i in range(steps):
            curr=curr.next
        curr.next=curr.next.next

        return head"""

        