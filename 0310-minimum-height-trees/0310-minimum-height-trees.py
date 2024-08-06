class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        def topological_sort(n,edgelist):
            graph=defaultdict(list)
            indegree=[0]*n
            for u ,v in edgelist:
                graph[v].append(u)
                graph[u].append(v)
                indegree[u]+=1
                indegree[v]+=1

            
            result=[]
            
            queue=deque()
            for node in range(n):
                if indegree[node]==1:
                    queue.append(node)
            prev=queue.copy()
            while queue:
                prev=queue.copy()
                for _ in range(len(queue)):
                    node=queue.popleft()
                    result.append(node)

                    for nb in graph[node]:
                        indegree[nb]-=1

                        if indegree[nb]==1:
                            queue.append(nb)
                            
                
            return prev
        return topological_sort(n,edges)