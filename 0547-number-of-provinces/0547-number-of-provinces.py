class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def inbound(r,c):
            return 0<=r<len(isConnected) and 0<=c<len(isConnected[0])
        directions =[[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            isConnected[r][c]=0
            for rc,cc in directions:
                nr=r+rc
                nc=c+cc
                if inbound(nr,nc) and isConnected[nr][nc]==1:
                    dfs(nr,nc)
        
        result=0
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]==1:
                    result+=1
                    dfs(i,j)
        return result
