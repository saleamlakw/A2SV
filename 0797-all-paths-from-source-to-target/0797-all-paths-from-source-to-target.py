class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        start=0
        destination=len(graph)-1

        ans=[]
        def dfs(arr,node):
            if node==destination:
                ans.append(arr)
            for nb in graph[node]:
                    dfs(arr+[nb],nb)
        dfs([start],start)
        return ans