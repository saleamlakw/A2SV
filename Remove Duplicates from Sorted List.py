# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        left,right=head,head.next
        while right:
            if left.val==right.val:
                left.next=left.next.next
            else:
                left=left.next
            print(left.val)
            print(right.val)
            right =right.next
        return head
