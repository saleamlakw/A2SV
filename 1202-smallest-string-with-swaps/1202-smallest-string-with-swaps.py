class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        graph=defaultdict(list)
        for u,v in pairs:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(node):
            visited.add(node)
            temp.append(s[node])
            ind.append(node)
            for nb in graph[node]:
                if nb not in visited:
                    dfs(nb)
    
        visited=set()
        re=[0]*len(s)
        for i in range(len(s)):
            if i not in visited:
                temp=[]
                ind=[]
                dfs(i)
                temp.sort()
                ind.sort()
                for k in range(len(ind)):
                    re[ind[k]]=temp[k]
        return ("".join(re))

