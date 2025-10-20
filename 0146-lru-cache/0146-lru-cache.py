class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cach = OrderedDict()
   
    def get(self, key: int) -> int:
        if key in self.cach:
            self.cach.move_to_end(key)
            return self.cach[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cach:
             self.cach.move_to_end(key)
        
        self.cach[key] = value

        if len(self.cach) > self.capacity:
            self.cach.popitem(last = False)
    
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)