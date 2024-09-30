class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize=maxSize
        self.stack=[]
        self.length=0
       

    def push(self, x: int) -> None:
        if self.length<self.maxSize:
            self.stack.append(x)
            self.length+=1

    def pop(self) -> int:
        if self.stack:
            self.length-=1
            return self.stack.pop()
        else:
            return -1    
            
            

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i<len(self.stack):
                self.stack[i]+=val
            else:
                break
                
# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)