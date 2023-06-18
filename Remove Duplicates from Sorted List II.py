# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        lil=[]
        left,right=head,head.next
        while right:
            if left.val==right.val:
                lil.append(left.val)
                left.next=left.next.next
            else:
                left=left.next
            right =right.next
        temp2=head
        tail=dummey=ListNode()
        while temp2:
            nen=ListNode(temp2.val)
            if temp2.val not in lil:
                tail.next=nen
                tail=tail.next
            temp2=temp2.next
        return dummey.next
