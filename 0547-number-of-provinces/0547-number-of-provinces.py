class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph=defaultdict(list)
        visited=set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    graph[i].append(j)
        print(graph)
        no_provience=0
        for node in graph:
            if node not in visited:
                no_provience+=1
                stack=[node]
                while stack:
                    new_node=stack.pop()
                    visited.add(new_node)
                    for new_node in graph[new_node]:
                        if new_node not in visited:
                            stack.append(new_node)
        return no_provience
                    