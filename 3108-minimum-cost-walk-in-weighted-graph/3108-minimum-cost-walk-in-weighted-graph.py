class DSU:
    def __init__(self,n):
        self.parent = {i:i for i in range(n)}
        self.size = {i:1 for i in range(n)}
        self.And = {i:-1 for i in range(n)}
    def find(self,x):
        while x!=self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self,x,y,w):
        parentX = self.find(x)
        parentY = self.find(y)

        if parentX != parentY:
            if self.size[parentX] > self.size[parentY]:
                self.size[parentX]+=self.size[parentY]
                self.parent[parentY]=parentX
                self.And[parentX]&=self.And[parentY]
            else:
                self.size[parentY]+=self.size[parentX]
                self.parent[parentX]=parentY
                self.And[parentY]&=self.And[parentX]
                
        
        self.And[self.find(x)]&=w
    def isConnected(self,x,y):
        return self.find(x)==self.find(y)






class Solution(object):
    def minimumCost(self, n, edges, query):
        dsu = DSU(n)
        ans = []
        
        for u,v,w in edges:
            dsu.And[u]=w
            dsu.And[v]=w
           
        for u,v,w in edges:
            dsu.union(u,v,w)
            # print(u,v,w,dsu.And)
        
        for u,v in query:
            if dsu.isConnected(u,v):
                ans.append(dsu.And[dsu.find(u)])
            else:
                ans.append(-1)
        return ans


        