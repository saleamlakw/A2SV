class Node:
    def __init__(self, val):
        self.val = val
        self.next  =None
class MyLinkedList:

    def __init__(self):
        self.length=0
        self.head=None
    def get(self, index: int) -> int:
        if index>self.length-1 or not self.head:
            return -1
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        if not self.head:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head = newNode
        self.length+=1
    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        if not self.head:
            self.head=newNode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newNode
        self.length+=1
    def addAtIndex(self, index: int, val: int) -> None:
        newNode=Node(val)
        if index>self.length:
            pass
        elif not self.head:
            self.head=newNode
            self.length+=1
        elif index==0:
            self.addAtHead(val)
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            newNode.next=temp.next
            temp.next=newNode
            self.length+=1
        
        
    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            pass
        elif index>=self.length:
            pass
        elif index==0:
            self.head=self.head.next
            self.length-=1
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            temp.next=temp.next.next
            self.length-=1
        



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)