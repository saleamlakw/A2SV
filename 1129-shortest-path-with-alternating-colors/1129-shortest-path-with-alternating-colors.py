class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=[[[],[]] for _ in range(n)]
        for u,v in redEdges:
            graph[u][0].append(v)
        for u,v in blueEdges:
            graph[u][1].append(v)

        answer=[-1]*n
        queue=deque([[0,0],[0,1]])
        visited=set([(0,0),(0,1)])
        dist=0
        while queue:
            for _ in range(len(queue)):
                node,color=queue.popleft()
                if answer[node]==-1:
                    answer[node]=dist
                for nb in graph[node][1-color]:
                    if (nb,1-color) not in visited:
                        visited.add((nb,1-color))
                        queue.append([nb,1-color])
            dist+=1
        return answer