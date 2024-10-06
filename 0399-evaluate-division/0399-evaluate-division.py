class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph=defaultdict(list)
        for i in range(len(equations)):
            graph[equations[i][0]].append([values[i],equations[i][1]])
            graph[equations[i][1]].append([1/values[i],equations[i][0]])
        re=[]
        for u,v in queries:
            if u not in graph:
                re.append(-1.00000)
            else:
                stack=[[u,1]]
                visited=set()
                found=False
                while stack:
                    node,ans=stack[-1]
                    if node not in visited:
                        visited.add(node)
                        if node==v:
                            re.append(ans)
                            found=True
                            break 
                        for nb in graph[node]:
                            if nb[1] not in visited:
                                stack.append([nb[1],ans*nb[0]])
                    else:
                        stack.pop()
                if not found:
                    re.append(-1.00000)
        return re
                
