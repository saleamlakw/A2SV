class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(node, parent):
            if node in visited: return True
            visited.add(node)
            nx,ny = node
            childs = [(cx,cy) for cx,cy in [[nx+1,ny],[nx-1, ny],[nx,ny+1],[nx,ny-1]] 
                      if 0 <= cx < m and 0 <= cy < n 
                      and grid[cx][cy] == grid[nx][ny] and (cx,cy) != parent]
            for x in childs:
                if dfs(x, node): return True 
            return False  
    
        m, n = len(grid), len(grid[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i,j) in visited: continue 
                if dfs((i,j), None): return True
        return False 
        