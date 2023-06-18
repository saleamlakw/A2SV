# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sul1=[]
        sul2=[]
        while l1:
            sul1.append(str(l1.val))
            l1=l1.next
        while l2:
            sul2.append(str(l2.val))
            l2=l2.next
        print(sul1)
        print(sul2)
        sul1.reverse()
        sul2.reverse()
        dummey=temp=ListNode()
        rem=0
        while sul1 and sul2:
            su=int(sul1.pop())+int(sul2.pop())
            su+=rem
            if (su)>9:
                rem=0
                newn=ListNode(int(str(su)[-1]))
                rem+=int(str(su)[0])
                temp.next=newn
            else:
                rem=0
                newn=ListNode(su)
                temp.next=newn
            temp=temp.next
        while sul1:
            su=int(sul1.pop())
            su+=rem
            if (su)>9:
                rem=0
                newn=ListNode(int(str(su)[-1]))
                rem+=int(str(su)[0])
                temp.next=newn
            else:
                rem=0
                newn=ListNode(su)
                temp.next=newn
            temp=temp.next
        while sul2:
            su=int(sul2.pop())
            su+=rem
            if (su)>9:
                rem=0
                newn=ListNode(int(str(su)[-1]))
                rem+=int(str(su)[0])
                temp.next=newn
            else:
                rem=0
                newn=ListNode(su)
                temp.next=newn
            temp=temp.next
        while rem>0:
            if rem>9:
                newn=ListNode(int(str(rem)[-1]))
                rem=int(str(rem)[0])
                temp.next=newn
            else :
                newn=ListNode(rem)
                temp.next=newn
                rem=0
            temp=temp.next
        return dummey.next






