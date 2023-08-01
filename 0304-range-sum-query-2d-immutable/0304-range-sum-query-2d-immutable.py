class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
            self.row,self.column=len(matrix),len(matrix[0])
            self.Nmatrix= [[0]*(self.column+1) for i in range(self.row+1)]
            for k in range(self.row):
                self.curr=0
                for j in range(self.column):
                    self.curr+=matrix[k][j]
                    self.Nmatrix[k+1][j+1]+=(self.Nmatrix[k][j+1]+self.curr)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2=row1+1, col1+1, row2+1, col2+1
        full=self.Nmatrix[row2][col2]
        left=self.Nmatrix[row2][col1-1]
        top=self.Nmatrix[row1-1][col2]
        common=self.Nmatrix[row1-1][col1-1]
        return (full-left-top)+common
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)