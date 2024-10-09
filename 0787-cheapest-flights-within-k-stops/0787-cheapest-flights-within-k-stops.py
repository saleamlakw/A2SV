class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in flights:
            graph[u].append([v,w])
         
        queue=deque([[-1,0,src]])
        distance=[float("inf")]*n
        distance[src]=0
        while queue:
            stops,pathlen,node=queue.popleft()
            for nb,edgelen in graph[node]:
                if stops+1<=k and pathlen+edgelen<distance[nb]:
                    distance[nb]=pathlen+edgelen
                    queue.append([stops+1,distance[nb],nb])
        return distance[dst] if distance[dst]!=float("inf") else -1