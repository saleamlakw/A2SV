class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph=defaultdict(list)
        for u,v in prerequisites:
            graph[u].append(v)
           
        def shorest_path(source ,destination):
            queue=deque([source])
            visited=set([source])
            while queue:
                node=queue.popleft()
                if node==destination:
                    return True
                for nb  in graph[node]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            return False   
        result=[] 
        for a,b in queries:
            if shorest_path(a,b):
                result.append(True)
            else:
                result.append(False) 
        return result

            
        