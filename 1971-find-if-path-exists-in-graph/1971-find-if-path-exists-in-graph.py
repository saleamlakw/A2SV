class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for ed in edges:
            graph[ed[0]].append(ed[1])
            graph[ed[1]].append(ed[0])
        visited=set()
        def dfs(node):
            if node==destination:
                return True
            visited.add(node)
            for nb in graph[node]:
                if nb not in visited:
                    found=dfs(nb)
                    if found:
                        return True

        return dfs(source)