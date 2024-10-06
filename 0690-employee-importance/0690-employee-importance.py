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

        stack=[id]
        visited=set()
        ans=0
        while stack:
            node=stack.pop()
            if node not in visited:
                visited.add(node)
                ans+=graph[node][0]
                for nb in graph[node][1]:
                    if nb not in visited:
                        stack.append(nb)
                        
        return ans 