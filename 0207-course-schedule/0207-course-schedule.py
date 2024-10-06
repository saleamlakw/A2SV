class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)
        for ele in prerequisites:
            graph[ele[0]].append(ele[1])
        white=1
        grey=2
        black=3
        color=[white]*numCourses
        visited=set()
        stop=False
        def dfs(node):
            nonlocal stop
            if stop:
                return 
            visited.add(node)
            color[node]=grey
            for nb in graph[node]:
                if color[nb]==grey:
                    stop=True
                if nb not in visited:
                    dfs(nb)
            # color[node]=black
        for ch in range(numCourses):
            if stop:
                return False
            if ch not in visited:
                dfs(ch)
        return True
        
