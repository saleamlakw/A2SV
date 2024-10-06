class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j]=="1":
                    ans+=1
                    stack=[[i,j]]
                    visited[i][j]=True
                    while stack:
                        r,c =stack.pop()
                        for rc,cc in directions:
                            nr,nc=r+rc,c+cc
                            if inbound(nr,nc) and not visited[nr][nc] and grid[nr][nc]=="1":
                                stack.append([nr,nc])
                                visited[nr][nc]=True
        return ans
