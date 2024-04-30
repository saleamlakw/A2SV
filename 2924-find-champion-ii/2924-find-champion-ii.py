class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        
        indegree=[0]*n

        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        if indegree.count(0)!=1:
            return -1

        return indegree.index(0)
        
            