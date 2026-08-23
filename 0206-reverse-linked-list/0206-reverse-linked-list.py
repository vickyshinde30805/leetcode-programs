# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:  
        curr,nxt,prev=head,None,None
        while curr !=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head=prev
        return head

        