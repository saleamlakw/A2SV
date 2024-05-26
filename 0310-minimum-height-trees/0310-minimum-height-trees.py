class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def findOrder(n,edgelist):
            graph=defaultdict(list)
            indegree=[0]*n
            for cor ,pre in edgelist:
                graph[pre].append(cor)
                graph[cor].append(pre)
                indegree[cor]+=1
                indegree[pre]+=1
            # print(indegree)
            
            result=[]
            
            queue=deque()
            for node in range(n):
                if indegree[node]==1:
                    queue.append(node)
            pe=queue.copy()
            while queue:
                pe=queue.copy()
                for _ in range(len(queue)):
                    node=queue.popleft()
                    result.append(node)

                    for nb in graph[node]:
                        indegree[nb]-=1

                        if indegree[nb]==1:
                            queue.append(nb)
                
            return pe
        return findOrder(n,edges)