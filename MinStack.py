class MinStack:

    def __init__(self):
        self.stack=[]
        self.minm=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minm:
            self.minm.append(val)
        else:
            self.minm.append(min(self.minm[-1],val))
    def pop(self) -> None:
        self.stack.pop()
        self.minm.pop()
    def top(self) -> int:
        return self.stack[-1]
    def getMin(self) -> int:
        return self.minm[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
