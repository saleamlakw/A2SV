class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        indegree=[0]*n
        graph=defaultdict(list)
        result=[set() for _ in range(n)]
        
        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        queue=deque()
        for node in range(n):
            if indegree[node]==0:
                queue.append(node)
            
        while queue:
            node=queue.popleft()

            for nb in graph[node]:
                indegree[nb]-=1
                result[nb].add(node)
                result[nb]=result[nb].union(result[node])

                if indegree[nb]==0:
                    queue.append(nb)
        return [sorted(list(x)) for x in result]