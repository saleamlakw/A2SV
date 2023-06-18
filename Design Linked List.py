class ListNode:
    def __init__(self, val):
        self.val=val
        self.next=None
      
class MyLinkedList:
    def __init__(self):
       self.head=None
       self.length=0 
    def get(self, index: int) -> int:
       if index>(self.length-1):
           return -1
       else:
           temp=self.head
           co=0
           while temp:
               if co==index:
                   return temp.val
               co+=1
               temp=temp.next
    def addAtHead(self, val: int) -> None:
        newn=ListNode(val)
        if self.head is None:
            self.head=newn
        else:
            newn.next=self.head
            self.head=newn
        self.length+=1
    def addAtTail(self, val: int) -> None:
        newn=ListNode(val)
        if self.head is None:
            self.head=newn
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newn
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
          if index>self.length:
              pass
          elif index==self.length:
              self.addAtTail(val)
          elif index==0:
              self.addAtHead(val)
          else:
              newn=ListNode(val)
              temp=self.head
              co=0
              while temp:
                  if co==index-1:
                      newn.next=temp.next
                      temp.next=newn
                      self.length+=1
                      break
                  co+=1
                  temp=temp.next
    def deleteAtIndex(self, index: int) -> None:
          if index>(self.length-1):
              pass
          elif index==0:
              self.head=self.head.next
              self.length-=1
          else:
              temp=self.head
              co=0
              while temp:
                  if co==index-1:
                      temp.next=temp.next.next
                      self.length-=1
                      break
                  co+=1
                  temp=temp.next
                
       
        
        
    
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
