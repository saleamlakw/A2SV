"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph=defaultdict(list)
        for emp in employees:
            graph[emp.id]=[emp.importance,emp.subordinates]
        print(graph)
        visited=set()

        def dfs(node):
            visited.add(node)
            if len(graph[node][1])==0:
                return graph[node][0]
            re=0
            for nb in graph[node][1]:
                if nb not in visited:
                    re+=dfs(nb)
            return graph[node][0]+ re
        
        return dfs(id) 