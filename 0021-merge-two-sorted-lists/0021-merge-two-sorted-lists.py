# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode()

        left = list1
        right = list2

        while left and right:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        
        while left:
            temp.next = left
            left = left.next
            temp = temp.next
        while right:
            temp.next = right
            right = right.next
            temp = temp.next
        return dummy.next