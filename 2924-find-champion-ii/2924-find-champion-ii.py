class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        
        indegree=[0]*n

        for u,v in edges:
            graph[u].append(v)
            indegree[v]+=1

        if indegree.count(0)!=1:
            return -1

        def dfs(node):
            nonlocal num_nodes
            visited.add(node)
            num_nodes+=1
            for nb in graph[node]:
                if  nb not in visited:
                    dfs(nb)
        
        for i in range(len(indegree)):
            if indegree[i]==0:
                visited=set()
                num_nodes=0
                dfs(i)
                # print(num_nodes)
                if num_nodes==(n):
                    return i
        return -1
        
            