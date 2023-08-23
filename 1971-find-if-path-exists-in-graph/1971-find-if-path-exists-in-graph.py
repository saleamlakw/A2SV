class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)
        stack=[source]
        visit=set([source])
        while stack:
            n=stack.pop()
            if destination==n:
                return True
            for neig in graph[n]:
                if neig not in visit:
                    stack.append(neig)
                    visit.add(neig)
        return False
        