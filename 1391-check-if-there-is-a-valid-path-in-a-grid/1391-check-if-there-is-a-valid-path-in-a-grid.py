class Solution:
    def inbound(self,grid,r,c):
        return (0<=r<len(grid) and 0<=c<len(grid[0]))
    def dfs(self,grid,visited,directions,r,c):
        # print(r,c)
        # print(len(grid)-1,len(grid[0])-1)
        if (r==len(grid)-1) and c==(len(grid[0])-1):
            print(True)
            return True
        for rn,cn in directions[grid[r][c]]:
            rr=rn+r
            cc=cn+c
            if self.inbound(grid,rr,cc) and (rr,cc) not in visited and (-rn,-cn) in directions[grid[rr][cc]]:
                visited.add((rr,cc))
                found=self.dfs(grid,visited,directions,rr,cc)
                if found:
                    return True
        return False
     
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        directions = {1: [(0,-1),(0,1)], 2: [(-1,0),(1,0)], 3: [(0,-1),(1,0)], 4: [(0,1),(1,0)], 5: [(0,-1),(-1,0)], 6: [(0,1),(-1,0)]}
        visited=set([(0,0)])
        return self.dfs(grid,visited,directions,0,0)

        