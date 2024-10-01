class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
           
        visited=set()
        def dfs(node):
            print(node)
            visited.add(node)
            if node==destination:
                return True
            temp=False
            for nb in graph[node]:
                if nb not in visited:
                    temp=temp or dfs(nb)
            return temp
        return dfs(source)


