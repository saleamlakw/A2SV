# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #intialize dummy variable and insert the first node to the dummy linked list 
        dummy=temp=ListNode()
        temp.next=ListNode(head.val)
        temp=temp.next
        start=head.next
        #traverse through the linked list starting from the second element and insert the gcd and the node into the dummy linkedlist 
        pre=head.val
        while start:
            temp.next=ListNode(gcd(start.val,pre))
            temp=temp.next
            temp.next=ListNode(start.val)
            temp=temp.next
            pre=start.val
            start=start.next
        return dummy.next
