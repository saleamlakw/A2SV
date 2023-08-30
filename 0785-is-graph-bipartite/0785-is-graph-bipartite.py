class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=set()
        for node in range(len(graph)):
            if graph[node] and node not in visited:
                stack=[node]
                visited=set([node])
                color=[-1]*len(graph)
                color[node]=0 
                while stack:
                        node=stack.pop()
                        for n in graph[node]:
                            if color[n]==color[node]:
                                return False
                            if color[n]==-1:
                                if color[node]==1:
                                    color[n]=0
                                else:
                                    color[n]=1
                            if n not in visited:
                                stack.append(n)
                                visited.add(n)
        return True
            
                        
        