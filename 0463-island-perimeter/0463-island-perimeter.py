class Solution:
    def dfs(self,grid,r,c,visited,directions,re):
        visited[r][c]=2
        if grid[r][c]==1:
             for rn,cn in directions:
                rrr=rn+r
                ccc=cn+c
                if (0>rrr or rrr>=len(grid) or 0>ccc or ccc>=len(grid[0])):
                    re.append(1)
                if (0<=rrr <len(grid) and 0<=ccc<len(grid[0])) and grid[rrr][ccc]!=1:
                    re.append(1)
        for rn,cn in directions:
            rr=rn+r
            cc=cn+c
            if (0<=rr<len(grid) and 0<=cc<len(grid[0]) and visited[rr][cc]!=2):
                self.dfs(grid,rr,cc,visited,directions,re)
        return
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited=[[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        re=[]
        self.dfs(grid,0,0,visited,directions,re)
        print(re)
        return sum(re)
        
        