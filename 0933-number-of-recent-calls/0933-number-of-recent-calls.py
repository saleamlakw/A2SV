class RecentCounter:
    def __init__(self):
        self.li=deque()
        self.re=0
    def ping(self, t: int) -> int:
        self.li.append(t)
        self.re+=1
        l=0
        while self.li[0]<t-3000:
            self.li.popleft()
            self.re-=1
        return self.re
            

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)