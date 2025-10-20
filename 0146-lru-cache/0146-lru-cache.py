class ListNode:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cach = {} 
        self.head = ListNode(-1,-1)
        self.tail =  ListNode(-1,-1)
        self.head.next ,  self.tail.prev = self.tail , self.head
    def insert(self,node):
        prev , nxt = self.tail.prev , self.tail
        prev.next = nxt.prev = node
        node.next = nxt
        node.prev = prev
    def remove(self,node):
       
        prev, nxt = node.prev , node.next 
        prev.next = nxt 
        nxt.prev = prev
    def get(self, key: int) -> int:
        if key in self.cach:
            self.remove(self.cach[key])
            self.insert(self.cach[key])
            return self.cach[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cach:
            self.remove(self.cach[key])
        newNode = ListNode(key,value)
        self.cach[key] = newNode
        self.insert(self.cach[key])

        if len(self.cach)>self.capacity:
            self.cach.pop(self.head.next.key)
            self.remove(self.head.next)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)