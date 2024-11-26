class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        indegree=[0]*n

        for u,v in edges:
            indegree[v]+=1

        if indegree.count(0)!=1:
            return -1

        return indegree.index(0)
        
            