class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit=[]
        projects=[(c,p) for (c,p) in zip(capital,profits)]
        heapify(projects)

        for i in range(k):
            while projects and projects[0][0]<=w:
                c,p=heapq.heappop(projects)
                heapq.heappush(profit,-p)
            if profit:
                w+=(-1*heapq.heappop(profit))
        return w