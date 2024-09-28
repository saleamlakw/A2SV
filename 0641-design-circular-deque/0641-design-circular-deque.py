class MyCircularDeque:

    def __init__(self, k: int):
        self.deque=[]
        self.k=k
        self.length=0
    def insertFront(self, value: int) -> bool:
        if self.k>self.length:
            self.deque.insert(0,value)
            self.length+=1
            return True
        else:
            return False
    def insertLast(self, value: int) -> bool:
        if self.k>self.length:
            self.deque.append(value)
            self.length+=1
            return True
        else:
            return False
    def deleteFront(self) -> bool:
        if self.deque:
            self.deque.pop(0)
            self.length-=1
            return True
        else:
            return False
    def deleteLast(self) -> bool:
        if self.deque:
            self.deque.pop()
            self.length-=1
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.deque:
            return self.deque[0]
        else:
            return -1
    def getRear(self) -> int:
        if self.deque:
            return self.deque[-1]
        else:
            return -1
    def isEmpty(self) -> bool:
        if self.deque:
            return False
        else:
            return True
    def isFull(self) -> bool:
        if self.length==self.k:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()