class Solution:      
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row,column=len(grid),len(grid[0])
        visit=set((0,0))
        queue=deque([(0,0,1)])
        neig=[[0,1],[0,-1],[1,0],[-1,0],[-1,-1],[1,1],[0,0],[-1,1],[1,-1]]
        while queue:
            for i in range(len(queue)):
                r,c,length=queue.popleft()
                if (min(r,c)<0   or r==row or c==column or grid[r][c]==1) :
                        continue
                if r==row-1 and c==column-1:
                    return length
                for dr ,dc in neig:
                    if (r+dr,c+dc) not in visit:
                        queue.append((r+dr,c+dc,length+1))
                        visit.add((r+dr,c+dc))
        return -1