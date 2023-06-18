# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cl=0
        te=head
        le=self.length(head)
        if le==1 or le==0:
                return None
        if (le-n)==0:
            head=head.next
            return head
        while te:
            if (le-n)-1==cl:
                te.next=te.next.next
            cl+=1
            te=te.next
        return head
    def length(self,head):
        temp=head
        co=0
        while temp:
            co+=1
            temp=temp.next
        return co
