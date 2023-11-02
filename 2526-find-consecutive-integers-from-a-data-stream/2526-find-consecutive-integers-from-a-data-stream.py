class DataStream:

    def __init__(self, value: int, k: int):
        self.k=k
        self.value=value
        self.li=deque()
        self.ch=0
    def consec(self, num: int) -> bool:
        self.li.append(num)
        if num==self.value:
            self.ch+=1
        while len(self.li)>self.k:
            if self.li.popleft()==self.value:
                self.ch-=1
        if len(self.li)==self.k and self.ch==self.k:
            return True
        else:
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)