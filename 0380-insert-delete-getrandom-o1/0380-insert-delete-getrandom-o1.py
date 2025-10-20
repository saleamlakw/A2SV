class RandomizedSet(object):

    def __init__(self):
        self.arr = []
        self.index = {}
    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.index:
            self.arr.append(val)
            self.index[val] = len(self.arr)-1
            return True
        else:
            return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.index:
            idx = self.index[val]
            self.arr[idx] , self.arr[-1] = self.arr[-1] , self.arr[idx]
            self.index[self.arr[idx]]= idx
            self.arr.pop()
            self.index.pop(val)
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()