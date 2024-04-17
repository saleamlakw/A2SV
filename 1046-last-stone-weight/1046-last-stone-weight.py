class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-1*ele for ele in stones]
        heapify(heap)
        while len(heap)>1:
            a=-1*heappop(heap)
            b=-1*heappop(heap)
            # print(a,b)
            if a-b>0:
                heappush(heap,-1*(a-b))
            # print(heap)
        return -1*heap[0] if heap else 0
