class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visited[i][j]:
                    res=0
                    stack=[[i,j]]
                    while stack:
                        r,c =stack.pop()
                        if not visited[r][c]:
                            res+=1
                            visited[r][c]=True
                            for rc,cc in directions:
                                nr,nc=r+rc,c+cc
                                if inbound(nr,nc) and not visited[nr][nc] and grid[nr][nc]:
                                    stack.append([nr,nc])
                    ans=max(res,ans)
        return ans