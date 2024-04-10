class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        fresh=0
        time=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    queue.append([i,j])
        
        directions=[[0,1], [1,0], [0,-1], [-1,0]]
        def inbound(r,c):
            return 0<=r<len(grid) and 0<=c<len(grid[0])
        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c=queue.popleft()
                for rc,cc in directions:
                    nr=r+rc
                    nc=c+cc
                    if inbound(nr,nc) and grid[nr][nc]==1:
                        fresh-=1
                        grid[nr][nc]=2
                        queue.append([nr,nc])
            time+=1
        return time if fresh==0 else -1
