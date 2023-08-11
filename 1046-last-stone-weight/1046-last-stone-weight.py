class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while True:
            if len(stones)<=1:
                return (-1*stones[0])
                break
            else:
                y=heapq.heappop(stones)
                x=heapq.heappop(stones)
                heapq.heappush(stones,(y-x))
        
        