class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        parent = {i:i for i in range(len(grid)*len(grid[0]))}
        size={i:0 for i in range(len(grid)*len(grid[0]))}
        tot=[]
        for ele in grid:
            tot.extend(ele)
        def find(x):
                while x!=parent[x]:
                    parent[x]=parent[parent[x]]
                    x=parent[x]
                return x
        def union(x, y):
            parentX = find(x)
            parentY = find(y)
            if parentX!= parentY:
                if size[parentX] > size[parentY]:
                    parent[parentY] = parentX
                    size[parentX] += size[parentY]
                    tot[parentX] += tot[parentY]
                else:
                    parent[parentX] = parentY
                    size[parentY] += size[parentX]
                    tot[parentY] += tot[parentX]
        def is_connected(x,y):
            return find(x)==find(y)
        
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    for rc,cc in directions:
                        nr=i+rc
                        nc=j+cc
                        if inbound(nr,nc) and grid[nr][nc]>0:
                            union(i*len(grid[0])+j,nr*len(grid[0])+nc)
        result=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]>0:
                    result=max(result,tot[find(i*len(grid[0])+j)])
        return result

        