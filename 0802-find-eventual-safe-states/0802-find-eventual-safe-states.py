class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        g=defaultdict(list)
        color=[0]*len(graph)
        result=[]
        for i in range(len(graph)):
            g[i]=graph[i]

        
        def dfs(node):
            if color[node]==1:
                return False 
            color[node]=1
            temp=True
            for nb in graph[node]:
                if color[nb]!=2:
                    temp=temp and dfs(nb)
                if not temp:
                    return False 
            color[node]=2
            result.append(node)
            return temp
        for node in range(len(graph)):
            if color[node]==0:
                dfs(node)
        return sorted(result)