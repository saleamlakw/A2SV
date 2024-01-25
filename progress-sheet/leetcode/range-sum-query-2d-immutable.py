class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row,col=len(matrix),len(matrix[0])
        self.ps=[[0]*(col+1) for _ in range(row+1)]

        for r in range(row):
            accumulator=0
            for c in range(col):
                accumulator+=matrix[r][c]
                re=self.ps[r][c+1]+accumulator
                self.ps[r+1][c+1]=re
 

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2=row1+1, col1+1, row2+1, col2+1
        all=self.ps[row2][col2]
        left=self.ps[row2][col1-1]
        top=self.ps[row1-1][col2]
        intersection=self.ps[row1-1][col1-1]

        return all-top-left+intersection


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)