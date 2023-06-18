# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=None
        cu=head
        ne=None
        while cu:
            ne=cu.next
            cu.next=pre
            pre=cu
            cu=ne
        return pre




            

 
      
