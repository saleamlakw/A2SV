# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = dummy = ListNode()
        dummy.next = head
        while temp:
            # print(temp.val)
            if temp.next and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp=temp.next
        return dummy.next