class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for u,v,w in times:
            graph[u].append([v,w])
        queue=[[0,k]]
        distance=[float("inf")]*(n+1)
        distance[k]=0

        while queue:
            pathlen,node=heappop(queue)
            for nb,edgelen in graph[node]:
                if pathlen+edgelen<distance[nb]:
                    distance[nb]=pathlen+edgelen
                    heappush(queue,[distance[nb],nb])
        print(distance)
        ans=max(distance[1:])
        if ans==float("inf"):
            return -1
        else:
            return ans
