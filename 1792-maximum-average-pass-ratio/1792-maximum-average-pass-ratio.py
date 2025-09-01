class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def calculateGain(a,b):
            cur = a/b
            inc = (a+1)/(b+1)
            return inc - cur
        minHeap = []
        for a,b in classes:
            gain = calculateGain(a,b)
            heapq.heappush(minHeap,(-gain,a,b))
        
        while  extraStudents:
            val,x,y = heapq.heappop(minHeap)
            gain = calculateGain(x+1,y+1)
            heapq.heappush(minHeap,(-(gain),x+1,y+1))
            extraStudents-=1
        ans = 0
        for _,x,y in minHeap:
            ans += (x/y)
        return ans/len(minHeap)