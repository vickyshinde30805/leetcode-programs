# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return head
        curr=head
        arr=[]
        while curr:
            arr.append(curr.val)
            curr=curr.next
        
        arr[left-1:right]=arr[left-1:right][::-1]

        head=ListNode(arr[0])
        curr=head
        for i in range(1,len(arr)):
            curr.next=ListNode(arr[i])
            curr=curr.next
        
        return head
            
