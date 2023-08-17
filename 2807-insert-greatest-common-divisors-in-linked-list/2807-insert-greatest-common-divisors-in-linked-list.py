# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from math import gcd
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        li=dummy=ListNode()
        temp=head
        if not head and not head.next:
            return head
        li.next=ListNode(temp.val)
        li=li.next
        while temp.next:
            x=gcd(temp.val,temp.next.val)
            li.next=ListNode(x)
            li=li.next
            li.next=ListNode(temp.next.val)
            li=li.next
            temp=temp.next
        return dummy.next
            
            
        
        