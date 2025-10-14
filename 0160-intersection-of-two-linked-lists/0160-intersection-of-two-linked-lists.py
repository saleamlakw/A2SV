# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        hashmapA = set()
        hashmapB = set()
        while headA or headB:
            if headA:
                hashmapA.add(headA)
                if headA in hashmapB:
                    return headA
                headA = headA.next
            if headB:
                hashmapB.add(headB)
                if headB in hashmapA:
                    return headB
                headB = headB.next
        return None
