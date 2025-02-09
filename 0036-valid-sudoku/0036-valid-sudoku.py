class Solution(object):
    def isValidSudoku(self, board):
        directions = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        for row in range(9):
            visitedRow = set()
            visitedCol = set()
            for col in range(9):
                if board[row][col] in visitedRow:
                    return False
                if board[row][col]!="." :
                    visitedRow.add(board[row][col])

                if board[col][row] in visitedCol:
                    return False
                if board[col][row]!="." :
                    visitedCol.add(board[col][row])
               
                cube = set([board[row][col]]) if board[row][col] != "." else set()
                
                if row in {1,4,7} and col in {1,4,7}:
                    for rc,cc in directions:
                        nr = row + rc
                        nc = col + cc
                        if board[nr][nc] in cube:
                            return False
                        if board[nr][nc]!="." :
                            cube.add(board[nr][nc])

        return True
        