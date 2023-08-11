# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self,left,right):
        temp=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                temp.next=left
                left=left.next
            else:
                temp.next=right
                right=right.next
            temp=temp.next
        if left:
                temp.next=left
        if right:
            temp.next=right
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        n=len(lists)
        left=lists[0]
        for i in range(1,n):
            right=lists[i]
            left=self.merge(left,right)
        return left





