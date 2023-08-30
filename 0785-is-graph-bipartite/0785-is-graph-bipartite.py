class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited=[]
        for u in range(len(graph)):
            if graph[u] and u not in visited:
                        stack=[u]
                        visited=set([u])
                        color=[-1]*len(graph)
                        if color[u]==-1:color[u]=0 
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
                                    # print(color)
                                print(color)
        return True
            
                        
        