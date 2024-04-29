class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent={i:i for i in range(1,n+1)}
        size={i:1 for i in range(1,n+1)}
        min_={i:float("inf") for i in range(1,n+1)}
        def find(x):
            while x!=parent[x]:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        def union(x,y,d):
            parentX=find(x)
            parentY=find(y)

            if parentX!=parentY:
                if size[parentX]>size[parentY]:
                    parent[parentY]=parentX
                    size[parentX]+=size[parentY]
                    min_[parentX]=min([min_[parentX],min_[parentY],d])
                  
                else:
                    parent[parentX]=parentY
                    size[parentY]+=size[parentX]
                    min_[parentY]=min([min_[parentY],min_[parentX],d])
                    
        def is_connected(x,y):
                return find(x)==find(y)
        for u,v,w in roads:
            union(u,v,w)
        root=find(n)
        return min_[root]