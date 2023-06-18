# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow,fast=head,head
        while fast.next and fast.next.next:
            temp=slow
            slow=slow.next
            fast=fast.next.next
        if (self.length(head))%2:
            return slow
        else:
            return slow.next
    def length(self,head):
        tem=head
        co=0
        while tem:
            co+=1
            tem=tem.next
        return co
        
