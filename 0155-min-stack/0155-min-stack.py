class MinStack:

    def __init__(self):
        self.stack=[]
        self.getmin=[]
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.getmin:
            self.getmin.append(min(self.getmin[-1],val))
        else:
            self.getmin.append(val)
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.getmin:
            self.getmin.pop()
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    def getMin(self) -> int:
        return self.getmin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()