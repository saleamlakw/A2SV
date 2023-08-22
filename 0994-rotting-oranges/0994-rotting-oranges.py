class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row,column=len(grid),len(grid[0])
        q=deque()
        time,fresh=0,0
        for r1 in range(row):
            for c1 in range(column):
                if grid[r1][c1]==1:
                    fresh+=1
                if grid[r1][c1]==2:
                    q.append((r1,c1))
        dire=[[0,1],[1,0],[-1,0],[0,-1]]
        while q and fresh>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in dire:
                    if min(r+dr,c+dc)<0 or r+dr==row or c+dc==column or grid[r+dr][c+dc]!=1:
                        continue
                    fresh-=1
                    grid[r+dr][c+dc]=2
                    q.append((r+dr,c+dc))
            time+=1
        return time if fresh==0 else -1 
                
        