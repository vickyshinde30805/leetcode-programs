# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp1=list1
        temp2=list2
        while temp1!=None:
            arr.append(temp1.val)
            temp1=temp1.next

        while temp2!=None:
            arr.append(temp2.val)
            temp2=temp2.next
        
        arr.sort()

        if not arr:
            return None
            
        head=ListNode(arr[0])

        for i in range(1,len(arr)):
            newNode=ListNode(arr[i])
            curr=head
            while curr.next!=None:
                curr=curr.next
            curr.next=newNode
            newNode.next=None
        
        return head

        