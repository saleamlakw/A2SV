class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #changing the reprsentaion of the graph from list to adjancy list
        graph=defaultdict(list)
        for n in prerequisites:
            graph[n[0]].append(n[1])
        # print(graph)
        white,gray,black=1,2,3
        is_possible=True
        color={k:white for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            color[node]=gray
            if node in graph:
                for neighbor in graph[node]:
                    if neighbor==node:
                        is_possible=False
                    if color[neighbor]==white:
                        dfs(neighbor)
                    elif  color[neighbor]==gray:
                        is_possible=False
            color[node]=black
            # print(color)
        for n in graph:
            if color[n]==white:
                dfs(n)
        return  is_possible 
            
        
            
        
        
        