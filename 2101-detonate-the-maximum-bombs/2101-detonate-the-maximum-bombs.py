class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph=defaultdict(list)
        def distance(p1,p2):
            return sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i!=j:
                   if distance(bombs[i],bombs[j])<=bombs[i][2]:
                    graph[i].append(j)
     
        def dfs(bomb):
            stack=[bomb]
            visited=set()
            count=0
            while stack:
                node=stack[-1]
                if node not in visited:
                    count+=1
                    visited.add(node)
                    for nb in graph[node]:
                        if nb not in visited:
                            stack.append(nb)
                else:
                    stack.pop()
            return count


        ans=0
        for bomb in range(len(bombs)):
            ans=max(ans,dfs(bomb))
        return ans


        
