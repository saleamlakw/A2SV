class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans=list(range(len(quiet)))
        al={quiet[i]:i for i in range(len(quiet))}
        graph=defaultdict(list)
        memo=Counter()
        visited=set()

        for u,v in richer:
            graph[v].append(u)
          

        def dfs(node):
            if len(graph[node])==0:
                return quiet[node]
            visited.add(node)
            temp=quiet[node]
            for nb in graph[node]:
                    if nb in memo:
                        temp=min(temp,memo[nb])
                    else:
                        temp=min(temp,dfs(nb))
            ans[node]=al[temp]
            memo[node]=temp
            return temp
        
        for  child in range(len(quiet)):
            if child not in visited:
                dfs(child)
        return ans
            
