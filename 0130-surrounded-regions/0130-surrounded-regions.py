class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(r,c):
            return 0<=r<len(board) and 0<=c<len(board[0])
        visited=set()
        def dfs(r,c):
            visited.add((r,c))
            board[r][c]="#"
            for rc,cc in directions:
                nr,nc =r+rc,c+cc
                if inbound(nr,nc) and (nr,nc) not in visited and board[nr][nc]=="O":
                    dfs(nr,nc)
           
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O" and (i in [0,len(board)-1 ] or j in [0,len(board[0])-1]):

                        dfs(i,j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="#":
                    board[i][j]="O"
                
            