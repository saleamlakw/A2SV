class DSU:
    def __init__(self,n):
        self.parent={i:i for i in range(n)}
        self.size={i:0 for i in range(n)}
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def union(self,x,y):
        parentX=self.find(x)
        parentY=self.find(y)
        if parentX!=parentY:
            if self.size[parentX]>self.size[parentY]:
                self.size[parentX]+=self.size[parentY]
                self.parent[parentY]=parentX
            else:
                self.size[parentY]+=self.size[parentX]
                self.parent[parentX]=parentY
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        dsu=DSU(n)
        dsu.union(0,firstPerson)
        time=set()
        all=defaultdict(lambda : defaultdict(list))
        for x,y,t in meetings:
            all[t][x].append(y)
            all[t][y].append(x)
            time.add(t)
       
        time=sorted(list(time))
        result=set([0,firstPerson])
        def dfs(node):
            visited.add(node)
            dsu.union(firstPerson,node)
            result.add(node)
            for nb in all[tt][node]:
                if nb not in visited:
                   dfs(nb)
        
        
        for tt in time:
            visited=set()
            for node in all[tt]:
                if node in result:
                    if node not in visited:
                        visited.add(node)
                        dfs(node)

        return list(result)
            
