class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for cor ,pre in prerequisites:
            graph[pre].append(cor)
            indegree[cor]+=1

        
        result=[]

        queue=deque()
        for node in range(numCourses):
            if indegree[node]==0:
                queue.append(node)
        
        while queue:
            course=queue.popleft()
            result.append(course)

            for nb in graph[course]:
                indegree[nb]-=1

                if indegree[nb]==0:
                    queue.append(nb)
        if len(result)!=numCourses:
            return []
        return result