class Bitset:

    def __init__(self, size: int):
        self.bitset=[0]*size
        self.bitInverse=[1]*size
        self.one_count=0
        self.zero_count=size
        self.size=size


    def fix(self, idx: int) -> None:
        if not self.bitset[idx]:
            self.one_count+=1
            self.zero_count-=1
        self.bitset[idx]=1
        self.bitInverse[idx]=0


    def unfix(self, idx: int) -> None:
        if self.bitset[idx]:
            self.one_count-=1
            self.zero_count+=1
        self.bitset[idx]=0
        self.bitInverse[idx]=1
            

    def flip(self) -> None:
        self.one_count,self.zero_count=self.zero_count,self.one_count
        self.bitset,self.bitInverse=self.bitInverse,self.bitset
    def all(self) -> bool:
        return self.one_count==self.size

    def one(self) -> bool:
        return (self.one_count>0)

    def count(self) -> int:
        return self.one_count
    def toString(self) -> str:
        result=[]
        for ele in self.bitset:
            result.append(str(ele))
        return "".join(result)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()