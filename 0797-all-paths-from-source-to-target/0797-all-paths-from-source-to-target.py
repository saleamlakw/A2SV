class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        all_routes = []
        route = []
        start = 0
        destination = len(graph)-1
        def dfs(node):
            route.append(node)
            if node == destination:
                all_routes.append(route[:])
            for nb in graph[node]:
                dfs(nb)
            route.pop()
        dfs(start)
        return all_routes