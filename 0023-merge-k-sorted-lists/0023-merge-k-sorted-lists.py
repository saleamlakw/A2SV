# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def prep(lists):
            n=len(lists)
            if not lists:
                return None
            s=lists[0]
            for i in range(1,n):
                s=merge(s,lists[i])
            return s
        def merge(f,s):
            dummy=ListNode()
            tem=dummy
            while f and s:
                if f.val<s.val:
                    tem.next=f
                    f=f.next
                else:
                    tem.next=s
                    s=s.next
                tem=tem.next
            if f:
                tem.next=f
            if s:
                tem.next=s
            return dummy.next
        return prep(lists)





