class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    stack=[(i,j)]
                    visited=set([(i,j)])
                    ans=0
                    while stack:
                        r,c=stack.pop()
                        for rc,cc in directions:
                            nr,nc=r+rc,c+cc
                            if not inbound(nr,nc) or not grid[nr][nc]:
                                ans+=1
                            if inbound(nr,nc) and (nr,nc) not in visited and grid[nr][nc]:
                                stack.append((nr,nc))
                                visited.add((nr,nc))
                    return ans
        