class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        row,col=len(board),len(board[0])
        directions=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
        visited=set()
        def inbound(r,c):
            return 0<=r<row and 0<=c<col
        def reval(r,c):
            count=0
            for rc,cc in directions:
                nr,nc=r+rc,c+cc
                if inbound(nr,nc):
                    if board[nr][nc]=="M":
                        count+=1
            return count
        def dfs(r,c):
            visited.add((r,c))
            if  board[r][c]=="M":
                    board[r][c]="X"
            elif board[r][c]=="E":
                    re=reval(r,c)
                    if re!=0:
                       board[r][c]=str(re)
                    else:
                        board[r][c]="B"
                        for rc,cc in directions:
                            nr=r+rc
                            nc=c+cc
                            if inbound(nr,nc) and (nr,nc) not in visited:
                                dfs(nr,nc)
        dfs(click[0],click[1])
        return board
