# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack=[]
        n=self.length(head)
        ans=[0]*n
        temp=head
        al=[]
        i=0
        while temp:
            while stack and al[stack[-1]]<temp.val:
                ans[stack.pop()]=temp.val
            stack.append(i)
            i+=1
            al.append(temp.val)
            temp=temp.next
        return ans
    def length(self,head):
        temp=head
        co=0
        while temp:
            co+=1
            temp=temp.next
        return co
