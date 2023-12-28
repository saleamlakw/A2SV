class OrderedStream:

    def __init__(self, n: int):
        self.stream=[0]*n
        self.n=n
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1]=value
        
        re=[]
        for i in range(0,idKey-1):
            if self.stream[i]==0:
                return []
        for k in range(idKey-1,self.n):
            if self.stream[k]==0:
                break
            else:
                re.append(self.stream[k])
        return re


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)