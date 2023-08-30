class Solution:
    def inbound(self,grid,r,c):
        return (0<=r<len(grid) and 0<=c<len(grid[0]))
    def dfs(self,grid,r,c,visited):
        visited[r][c]=1
        directions=[(1,0),[0,1],(0,-1),(-1,0)]
        for rn,cn in directions:
            new_row=r+rn
            new_col=c+cn
            if (self.inbound(grid,new_row,new_col) and grid[new_row][new_col]=="1") and visited[new_row][new_col]==0:
                self.dfs(grid,new_row,new_col,visited)
    def numIslands(self, grid: List[List[str]]) -> int:
        no_island=0
        visited=[[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if visited[r][c]==0 and grid[r][c]=="1":
                    no_island+=1
                    self.dfs(grid,r,c,visited)
        return no_island
                    
        