class MedianFinder:

    def __init__(self):
        self.small_max,self.large_min=[],[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max,-1*num)
        if self.small_max and self.large_min and -1*self.small_max[0]>self.large_min[0]:
            heapq.heappush(self.large_min,-1*heapq.heappop(self.small_max))
        if len(self.small_max)>len(self.large_min)+1:
            heapq.heappush(self.large_min,-1*heapq.heappop(self.small_max))
        if len(self.large_min)>len(self.small_max)+1:
            heapq.heappush(self.small_max,-1*heapq.heappop(self.large_min))

    def findMedian(self) -> float:
        if len(self.small_max) > len(self.large_min):
            return -1*self.small_max[0]
        elif len(self.large_min)>len(self.small_max):
            return self.large_min[0]
        else:
            return ((-1*self.small_max[0])+self.large_min[0])/2
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()